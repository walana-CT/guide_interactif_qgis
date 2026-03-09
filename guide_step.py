# -*- coding: utf-8 -*-
"""
Système de guidage pas à pas pour QGIS
"""

from qgis.PyQt.QtCore import Qt, QRect, QPoint, QTimer
from qgis.PyQt.QtGui import QPainter, QColor, QPen
from qgis.PyQt.QtWidgets import QWidget, QApplication


class HighlightOverlay(QWidget):
    """Widget transparent qui met en évidence un élément de l'interface"""
    
    def __init__(self, target_widget, parent=None):
        super().__init__(parent)
        self.target_widget = target_widget
        self.target_window = self.target_widget.window() if self.target_widget else None
        
        # Superposition non bloquante au-dessus de la fenetre cible.
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)

        # Utiliser des coordonnees locales de la fenetre cible pour un mapping stable.
        if self.target_window:
            self.setParent(self.target_window)
            self.setGeometry(self.target_window.rect())
        else:
            main_window = QApplication.instance().activeWindow()
            if main_window:
                self.setGeometry(main_window.rect())

        # Fermer automatiquement pour ne pas laisser un voile persistant.
        self._hide_timer = QTimer(self)
        self._hide_timer.setSingleShot(True)
        self._hide_timer.timeout.connect(self.close)
        self._hide_timer.start(1800)
        
        self.show()
    
    def paintEvent(self, event):
        """Dessine l'overlay avec un trou pour mettre en évidence l'élément"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Voile tres leger pour guider l'oeil sans masquer l'interface.
        painter.fillRect(self.rect(), QColor(0, 0, 0, 18))
        
        # Créer un "trou" pour l'élément cible
        if self.target_widget and self.target_widget.isVisible():
            # Calculer la position dans le repere local de l'overlay.
            target_rect = self.target_widget.rect()
            if self.target_window:
                local_pos = self.target_widget.mapTo(self.target_window, QPoint(0, 0))
            else:
                target_pos = self.target_widget.mapToGlobal(QPoint(0, 0))
                local_pos = self.mapFromGlobal(target_pos)
            highlight_rect = QRect(local_pos, target_rect.size())

            if not highlight_rect.isValid() or highlight_rect.width() < 2 or highlight_rect.height() < 2:
                return
            
            # Agrandir legerement le rectangle pour un meilleur effet
            highlight_rect.adjust(-6, -6, 6, 6)

            # Eclaircir legerement la zone cible
            painter.setCompositionMode(QPainter.CompositionMode_SourceOver)
            painter.fillRect(highlight_rect, QColor(255, 255, 255, 25))

            # Dessiner un double contour lumineux bien visible
            pen = QPen(QColor(255, 193, 7), 4)
            painter.setPen(pen)
            painter.drawRect(highlight_rect)

            inner_rect = QRect(highlight_rect)
            inner_rect.adjust(3, 3, -3, -3)
            pen2 = QPen(QColor(255, 255, 255), 2)
            painter.setPen(pen2)
            painter.drawRect(inner_rect)
    
    def mousePressEvent(self, event):
        """Fermer l'overlay au clic"""
        self.close()


class GuideStep:
    """Représente une étape du guide"""

    def __init__(
            self,
            title,
            description,
            target_widget_name=None,
            target_action=None,
            target_resolver=None,
            target_object_name=None):
        """
        Args:
            title: Titre de l'étape
            description: Description détaillée
            target_widget_name: Nom du widget à mettre en évidence (optionnel)
            target_action: Action QAction à mettre en évidence (optionnel)
            target_resolver: Fonction callable qui retourne un QWidget cible (optionnel)
            target_object_name: objectName exakt du widget (optionnel, technique QGIS)
        """
        self.title = title
        self.description = description
        self.target_widget_name = target_widget_name
        self.target_action = target_action
        self.target_resolver = target_resolver
        self.target_object_name = target_object_name
        self.highlight_overlay = None

    def has_target(self):
        """Indique si l'etape contient une cible potentielle de highlight."""
        return bool(self.target_widget_name or self.target_action or self.target_resolver or self.target_object_name)
    
    def show_highlight(self, iface):
        """Affiche la mise en evidence de l'element.

        Returns:
            bool: True si un element a pu etre surligne, sinon False.
        """
        self.hide_highlight()
        target_widget = None
        
        # Trouver le widget cible (priorite : objectName > resolver > action > widget_name)
        if self.target_object_name:
            # Methode ultra-fiable : chercher par objectName exact
            main_window = iface.mainWindow()
            target_widget = self._find_widget_by_object_name(main_window, self.target_object_name)
            # Fallback: chercher aussi dans les fenetres top-level
            if not target_widget:
                from qgis.PyQt.QtWidgets import QApplication
                app = QApplication.instance()
                for widget in app.topLevelWidgets():
                    if widget.isVisible():
                        target_widget = self._find_widget_by_object_name(widget, self.target_object_name)
                        if target_widget:
                            break
        elif self.target_resolver:
            try:
                target_widget = self.target_resolver(iface)
            except Exception:
                target_widget = None
        elif self.target_action:
            # Trouver le bouton associé à l'action
            target_widget = self._find_action_widget(iface.mainWindow(), self.target_action)
        elif self.target_widget_name:
            target_widget = self._find_widget_by_name(iface.mainWindow(), self.target_widget_name)
        
        if target_widget and target_widget.isVisible():
            self.highlight_overlay = HighlightOverlay(target_widget)
            return True

        return False
    
    def hide_highlight(self):
        """Cache la mise en évidence"""
        if self.highlight_overlay:
            self.highlight_overlay.close()
            self.highlight_overlay = None
    
    def _find_widget_by_name(self, parent, name):
        """Recherche récursive d'un widget par son nom"""
        widget = parent.findChild(QWidget, name)
        return widget

    def _find_widget_by_object_name(self, parent, object_name):
        """Recherche un widget par son objectName exact (technique QGIS).

        Args:
            parent: Widget parent (fenetre ou boite de dialogue)
            object_name: objectName du widget cible

        Returns:
            QWidget ou None si non trouve
        """
        if not parent or not object_name:
            return None

        widget = parent.findChild(QWidget, object_name)
        return widget if widget and widget.isVisible() else None

    @staticmethod
    def normalize_text(value):
        """Normalise un texte pour comparaison souple."""
        if not value:
            return ""
        return value.replace('&', '').replace('...', '').strip().lower()

    @staticmethod
    def widget_text(widget):
        """Recupere le texte principal d'un widget si disponible."""
        if widget is None:
            return ""
        getter = getattr(widget, 'text', None)
        if callable(getter):
            try:
                return getter() or ""
            except Exception:
                return ""
        return ""

    @classmethod
    def find_child_by_text(cls, parent, texts):
        """Trouve un widget enfant dont le texte correspond a une liste de motifs."""
        if not parent:
            return None

        wanted = [cls.normalize_text(t) for t in texts if t]
        for child in parent.findChildren(QWidget):
            text = cls.normalize_text(cls.widget_text(child))
            if not text:
                continue
            for candidate in wanted:
                if candidate and candidate in text:
                    return child
        return None

    @staticmethod
    def _normalize_action_label(label):
        """Normalise les libelles Qt pour faciliter la comparaison."""
        return GuideStep.normalize_text(label)
    
    def _find_action_widget(self, parent, action_text):
        """Trouve le widget associé à une action (bouton de toolbar)"""
        from qgis.PyQt.QtWidgets import QToolBar

        wanted = self._normalize_action_label(action_text)
        if not wanted:
            return None
        
        # Chercher dans toutes les toolbars
        toolbars = parent.findChildren(QToolBar)
        for toolbar in toolbars:
            for action in toolbar.actions():
                action_text_norm = self._normalize_action_label(action.text())
                icon_text_norm = self._normalize_action_label(action.iconText())
                if wanted in (action_text_norm, icon_text_norm):
                    # Trouver le bouton associé
                    widget = toolbar.widgetForAction(action)
                    if widget:
                        return widget
        return None

    @staticmethod
    def introspect_widget_tree(widget, indent=0, max_depth=4):
        """Utilitaire pour decouvrir les objectName d'une fenetre.

        Utilise ceci dans la console Python QGIS pour explorer :
            from guide_interactif.guide_step import GuideStep
            dlg = iface.mainWindow().findChild(QWidget, "QgsOptionsDialog")
            print(GuideStep.introspect_widget_tree(dlg))

        Args:
            widget: Widget a inspecter
            indent: Profondeur d'indentation (interne)
            max_depth: Profondeur max avant truncature

        Returns:
            str: Arborescence formatee avec objectName et type
        """
        if indent > max_depth:
            return ""

        result = []
        prefix = "  " * indent
        obj_name = widget.objectName() or "(no name)"
        class_name = widget.__class__.__name__
        visible = widget.isVisible()
        vis_str = "✓" if visible else "✗"

        result.append(f"{prefix}{vis_str} [{obj_name}] <{class_name}>")

        for child in widget.children():
            if isinstance(child, QWidget):
                result.append(
                    GuideStep.introspect_widget_tree(child, indent + 1, max_depth)
                )

        return "\n".join(filter(None, result))


class Guide:
    """Classe qui gère un guide complet avec plusieurs étapes"""
    
    def __init__(self, name, description, steps):
        """
        Args:
            name: Nom du guide
            description: Description du guide
            steps: Liste d'objets GuideStep
        """
        self.name = name
        self.description = description
        self.steps = steps
        self.current_step_index = 0
    
    def get_current_step(self):
        """Retourne l'étape actuelle"""
        if 0 <= self.current_step_index < len(self.steps):
            return self.steps[self.current_step_index]
        return None
    
    def next_step(self):
        """Passe à l'étape suivante"""
        current = self.get_current_step()
        if current:
            current.hide_highlight()
        
        self.current_step_index += 1
        return self.get_current_step()
    
    def previous_step(self):
        """Retourne à l'étape précédente"""
        current = self.get_current_step()
        if current:
            current.hide_highlight()
        
        self.current_step_index = max(0, self.current_step_index - 1)
        return self.get_current_step()
    
    def reset(self):
        """Réinitialise le guide"""
        current = self.get_current_step()
        if current:
            current.hide_highlight()
        self.current_step_index = 0
    
    def is_finished(self):
        """Vérifie si le guide est terminé"""
        return self.current_step_index >= len(self.steps)
    
    def get_progress(self):
        """Retourne la progression (étape actuelle / total)"""
        return self.current_step_index, len(self.steps)
