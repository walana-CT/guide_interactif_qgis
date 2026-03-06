# -*- coding: utf-8 -*-
"""
Système de guidage pas à pas pour QGIS
"""

from qgis.PyQt.QtCore import Qt, QTimer, QRect, QPoint
from qgis.PyQt.QtGui import QPainter, QColor, QPen, QFont
from qgis.PyQt.QtWidgets import QWidget, QApplication


class HighlightOverlay(QWidget):
    """Widget transparent qui met en évidence un élément de l'interface"""
    
    def __init__(self, target_widget, parent=None):
        super().__init__(parent)
        self.target_widget = target_widget
        
        # Rendre le widget transparent et en plein écran
        self.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        
        # Obtenir la géométrie de la fenêtre principale QGIS
        main_window = QApplication.instance().activeWindow()
        if main_window:
            self.setGeometry(main_window.geometry())
        
        self.show()
    
    def paintEvent(self, event):
        """Dessine l'overlay avec un trou pour mettre en évidence l'élément"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Assombrir tout l'écran
        painter.fillRect(self.rect(), QColor(0, 0, 0, 150))
        
        # Créer un "trou" pour l'élément cible
        if self.target_widget and self.target_widget.isVisible():
            # Obtenir la position globale de l'élément cible
            target_rect = self.target_widget.rect()
            target_pos = self.target_widget.mapToGlobal(QPoint(0, 0))
            
            # Convertir en coordonnées locales de l'overlay
            local_pos = self.mapFromGlobal(target_pos)
            highlight_rect = QRect(local_pos, target_rect.size())
            
            # Agrandir légèrement le rectangle pour un meilleur effet
            highlight_rect.adjust(-10, -10, 10, 10)
            
            # Effacer la zone (créer le "trou")
            painter.setCompositionMode(QPainter.CompositionMode_Clear)
            painter.fillRect(highlight_rect, Qt.transparent)
            
            # Dessiner un contour lumineux
            painter.setCompositionMode(QPainter.CompositionMode_SourceOver)
            pen = QPen(QColor(52, 152, 219), 3)  # Bleu vif
            painter.setPen(pen)
            painter.drawRect(highlight_rect)
    
    def mousePressEvent(self, event):
        """Fermer l'overlay au clic"""
        self.close()


class GuideStep:
    """Représente une étape du guide"""
    
    def __init__(self, title, description, target_widget_name=None, target_action=None):
        """
        Args:
            title: Titre de l'étape
            description: Description détaillée
            target_widget_name: Nom du widget à mettre en évidence (optionnel)
            target_action: Action QAction à mettre en évidence (optionnel)
        """
        self.title = title
        self.description = description
        self.target_widget_name = target_widget_name
        self.target_action = target_action
        self.highlight_overlay = None
    
    def show_highlight(self, iface):
        """Affiche la mise en évidence de l'élément"""
        target_widget = None
        
        # Trouver le widget cible
        if self.target_widget_name:
            target_widget = self._find_widget_by_name(iface.mainWindow(), self.target_widget_name)
        elif self.target_action:
            # Trouver le bouton associé à l'action
            target_widget = self._find_action_widget(iface.mainWindow(), self.target_action)
        
        if target_widget:
            self.highlight_overlay = HighlightOverlay(target_widget)
    
    def hide_highlight(self):
        """Cache la mise en évidence"""
        if self.highlight_overlay:
            self.highlight_overlay.close()
            self.highlight_overlay = None
    
    def _find_widget_by_name(self, parent, name):
        """Recherche récursive d'un widget par son nom"""
        widget = parent.findChild(QWidget, name)
        return widget
    
    def _find_action_widget(self, parent, action_text):
        """Trouve le widget associé à une action (bouton de toolbar)"""
        from qgis.PyQt.QtWidgets import QToolBar, QToolButton
        
        # Chercher dans toutes les toolbars
        toolbars = parent.findChildren(QToolBar)
        for toolbar in toolbars:
            for action in toolbar.actions():
                if action.text() == action_text or action.iconText() == action_text:
                    # Trouver le bouton associé
                    widget = toolbar.widgetForAction(action)
                    if widget:
                        return widget
        return None


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
