# Guide Interactif QGIS - Documentation

## Description

Ce plugin fournit un système de guides interactifs pas à pas pour apprendre à utiliser QGIS. Chaque guide met en évidence les éléments de l'interface nécessaires et guide l'utilisateur étape par étape.

## Guides disponibles

1. **Ajouter une couche vecteur** - Apprendre à importer des données vecteur
2. **Créer une zone tampon** - Utiliser les outils de géotraitement
3. **Modifier la symbologie** - Changer l'apparence des couches

## Comment créer un nouveau guide

### 1. Structure d'un guide

Un guide est composé de :
- Un **nom** et une **description**
- Une liste d'**étapes** (`GuideStep`)

Chaque étape contient :
- Un **titre**
- Une **description** détaillée
- (Optionnel) Un **élément d'interface** à mettre en évidence

### 2. Créer un nouveau guide

Ouvrez le fichier `guides_predefined.py` et ajoutez une nouvelle fonction :

```python
def create_guide_mon_nouveau_guide():
    """Description de mon guide"""
    steps = [
        GuideStep(
            title="Étape 1 : Titre de l'étape",
            description="Instructions détaillées pour cette étape.\n\n"
                       "Vous pouvez utiliser plusieurs lignes.",
            target_widget_name="nom_du_widget"  # Optionnel
        ),
        GuideStep(
            title="Étape 2 : Autre étape",
            description="Autres instructions...",
            target_action="Nom de l'action"  # Pour cibler un bouton de toolbar
        ),
        # ... autres étapes
    ]
    
    return Guide(
        name="Nom de mon guide",
        description="Description courte du guide",
        steps=steps
    )
```

### 3. Enregistrer le guide

Ajoutez votre guide dans la fonction `get_all_guides()` :

```python
def get_all_guides():
    """Retourne tous les guides disponibles"""
    return [
        create_guide_add_vector_layer(),
        create_guide_create_buffer(),
        create_guide_change_symbology(),
        create_guide_mon_nouveau_guide(),  # ← Ajoutez le vôtre ici
    ]
```

### 4. Mettre en évidence des éléments de l'interface

Pour mettre en évidence un élément, vous avez deux options :

#### Option A : Par nom de widget
```python
target_widget_name="mLayerTreeView"  # Nom du widget Qt
```

Widgets courants dans QGIS :
- `mLayerTreeView` : Panneau des couches
- `mMapCanvas` : Zone de carte
- `mCoordsEdit` : Affichage des coordonnées

#### Option B : Par action de toolbar
```python
target_action="Gestionnaire de sources de données"  # Texte de l'action
```

Actions courantes :
- "Gestionnaire de sources de données"
- "Ouvrir le projet"
- "Enregistrer le projet"
- etc.

### 5. Conseils pour de bons guides

#### ✅ Bonnes pratiques

- **Titres clairs** : Indiquez clairement l'action à effectuer
- **Descriptions détaillées** : N'hésitez pas à être verbeux
- **Étapes logiques** : Divisez les tâches complexes en petites étapes
- **Émojis** : Utilisez ✓, 💡, 📖, etc. pour rendre le texte plus vivant
- **Feedback positif** : Terminez par une étape de félicitations

#### ❌ À éviter

- Étapes trop longues ou complexes
- Instructions vagues
- Trop d'étapes (max 8-10 recommandé)

## Exemples d'utilisation

### Exemple 1 : Guide simple sans highlight

```python
def create_guide_export_map():
    steps = [
        GuideStep(
            title="Étape 1 : Ouvrir le composeur d'impression",
            description="Allez dans Projet > Nouveau composeur d'impression"
        ),
        GuideStep(
            title="Étape 2 : Ajouter la carte",
            description="Cliquez sur 'Ajouter une carte' et dessinez un rectangle"
        ),
        GuideStep(
            title="Étape 3 : Exporter",
            description="Cliquez sur Composeur > Exporter en tant que PDF"
        ),
    ]
    return Guide("Exporter une carte", "Guide d'export de carte", steps)
```

### Exemple 2 : Guide avec highlights

```python
def create_guide_selection():
    steps = [
        GuideStep(
            title="Étape 1 : Activer l'outil de sélection",
            description="Cliquez sur l'outil de sélection dans la barre d'outils",
            target_action="Sélectionner des entités"
        ),
        GuideStep(
            title="Étape 2 : Sélectionner des entités",
            description="Cliquez sur des entités sur la carte pour les sélectionner",
            target_widget_name="mMapCanvas"
        ),
    ]
    return Guide("Sélectionner des entités", "Sélection interactive", steps)
```

## Structure des fichiers

```
guide_interactif/
├── guide_step.py           # Classes principales (Guide, GuideStep, HighlightOverlay)
├── guides_predefined.py    # Guides prédéfinis
├── guide_interactif_dialog.py  # Interface utilisateur
└── guide_interactif.py     # Plugin principal
```

## Débogage

### Le guide ne s'affiche pas
- Vérifiez que vous avez ajouté votre guide dans `get_all_guides()`
- Rechargez le plugin avec Plugin Reloader

### Le highlight ne fonctionne pas
- Le nom du widget peut être incorrect
- Utilisez l'outil de débogage Qt pour trouver le bon nom
- Certains éléments ne sont pas accessibles avant qu'ils ne soient créés

### Comment trouver le nom d'un widget ?
Vous pouvez utiliser ce code dans la console Python de QGIS :

```python
# Lister tous les widgets enfants de la fenêtre principale
for widget in iface.mainWindow().findChildren(QWidget):
    if widget.objectName():
        print(widget.objectName())
```

## Améliorations futures

Idées pour étendre le plugin :

- [ ] Ajouter des vidéos ou GIF dans les étapes
- [ ] Permettre de marquer les étapes comme "complétées"
- [ ] Ajouter des quiz/validations
- [ ] Historique des guides complétés
- [ ] Guides conditionnels (selon le contexte)
- [ ] Export/import de guides personnalisés
- [ ] Traductions multilingues

## Support

Pour toute question ou problème, contactez :
- Robin FICHT (robin.ficht@onf.fr)
