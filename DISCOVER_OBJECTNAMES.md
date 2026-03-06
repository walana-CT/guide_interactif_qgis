# Comment découvrir les objectName des éléments de l'interface QGIS

## Pourquoi les objectName ?

Les `objectName` sont des identifiants uniques donnés à chaque widget Qt/QGIS. C'est la **méthode la plus précise et la plus fiable** pour identifier un élément d'interface, car :
- Pas dépendante du texte affiché (multilingue) ✓
- Pas de fausse correspondance comme avec les heuristiques ✓
- Stable entre les versions QGIS (généralement) ✓

## Exemple : Découvrir les objectName de la boîte d'Options

### Étape 1 : Ouvrir la console Python QGIS

1. Dans QGIS, allez dans **Extensions** > **Console Python**
2. Vous devriez voir une fenêtre Python en bas

### Étape 2 : Importer le nécessaire

```python
from qgis.PyQt.QtWidgets import QWidget, QApplication
from guide_interactif.guide_step import GuideStep

# Obtenir la fenêtre des Préférences/Options
app = QApplication.instance()
dlg = None
for widget in app.topLevelWidgets():
    if "options" in widget.windowTitle().lower() or "preferences" in widget.windowTitle().lower():
        dlg = widget
        break

if dlg:
    print("Dialog trouvée !")
    print(GuideStep.introspect_widget_tree(dlg))
else:
    print("Ouvrez d'abord Édition > Préférences")
```

### Étape 3 : Interprétation de l'output

L'output affichera une arborescence comme ceci :

```
✓ [QgsOptionsDialog] <QgsOptionsDialog>
  ✓ [mOptionsListWidget] <QListWidget>
  ✓ [mOptionsStackedWidget] <QStackedWidget>
  ✓ [mLangComboBox] <QComboBox>
  ✓ [mLangLabel] <QLabel>
  ✓ [horizontalLayout] <QHBoxLayout>
  ✗ [someHiddenWidget] <QPushButton>
```

Explication :
- `[objectName]` : C'est ce que vous voulez copier dans votre code !
- `<ClassName>` : Le type du widget (QComboBox, QLabel, etc.)
- `✓` : Widget visible, `✗` : Widget caché

## Exemple concret pour le guide "Changer la langue"

### Découverte des éléments

1. Ouvrez Édition > Préférences
2. Exécutez le script ci-dessus
3. Notez les objectName pertinents :

```python
# De la output découverte
QGIS_OBJECT_NAMES = {
    "OPTIONS_DIALOG": "QgsOptionsDialog",
    "LANGUAGE_COMBOBOX": "mLangComboBox",
    "LANGUAGE_LABEL": "mLangLabel",
    "OK_BUTTON": "buttonBox",  # Exemple hypothétique
}
```

### Utilisation dans un guide

```python
from .guide_step import Guide, GuideStep

def create_guide_example():
    steps = [
        GuideStep(
            title="Étape 1 : Ouvrir les options",
            description="...",
            target_object_name="QgsOptionsDialog",  # ← objectName exact
        ),
        GuideStep(
            title="Étape 2 : Changer la langue",
            description="...",
            target_object_name="mLangComboBox",  # ← Cible précise de la combobox
        ),
    ]
    return Guide("...", "...", steps)
```

## Commandes utiles pour la console

### 1. Lister tous les widgets visibles et leurs objectName

```python
from qgis.PyQt.QtWidgets import QApplication, QWidget

app = QApplication.instance()
for widget in app.topLevelWidgets():
    if widget.isVisible():
        print(f"{widget.windowTitle()}: {widget.objectName()}")
```

### 2. Chercher un widget par texte

```python
from qgis.PyQt.QtWidgets import QApplication

def find_widget_by_text(search_text):
    app = QApplication.instance()
    results = []
    for widget in app.topLevelWidgets():
        for child in widget.findChildren(QWidget):
            if hasattr(child, 'text') and search_text.lower() in child.text().lower():
                results.append((child.text(), child.objectName(), child.__class__.__name__))
    return results

print(find_widget_by_text("interface"))
```

### 3. Inspecter une fenêtre spécifique

```python
from guide_interactif.guide_step import GuideStep

# Trouver un dialog par titre
dlg = None
for w in app.topLevelWidgets():
    if "Options" in w.windowTitle():
        dlg = w
        break

if dlg:
    print(GuideStep.introspect_widget_tree(dlg, max_depth=5))
```

## Différences entre les versions QGIS

Les `objectName` peuvent varier légèrement entre les versions de QGIS :

| Version QGIS | OPTIONS_DIALOG | LANGUAGE_COMBOBOX |
|---|---|---|
| QGIS 3.20+ | `QgsOptionsDialog` | `mLangComboBox` |
| QGIS 3.18-3.19 | `QgsPreferencesDialog` | `mLangComboBox` |
| QGIS 3.16- | Peut différer | Peut différer |

**À faire** : Mettre à jour les constantes `QGIS_OBJECT_NAMES` dans `guides_predefined.py` selon votre version !

## Fallback et robustesse

Dans le code, utilisez toujours une stratégie hybride :

```python
def _resolve_language_combobox(iface):
    """Resolution intelligente : objectName + fallback texte."""
    dlg = _resolve_options_dialog(iface)
    if not dlg:
        return None
    
    # Étape 1 : Essayer par objectName (ULTRA-FIABLE)
    combo = dlg.findChild(QComboBox, "mLangComboBox")
    if combo and combo.isVisible():
        return combo
    
    # Étape 2 : Fallback sur recherche textuelle si objectName ne marche pas
    return GuideStep.find_child_by_text(dlg, ["langue", "language", "locale"])
```

Cela assure que votre guide fonctionne même si les objectName changent entre versions.

## Pour plus d'informations

- [Documentation Qt sur objectName](https://doc.qt.io/qt-5/qobject.html#objectName-prop)
- [Méthode GuideStep.introspect_widget_tree()](/guide_step.py)
- [Constantes QGIS_OBJECT_NAMES](/guides_predefined.py)
