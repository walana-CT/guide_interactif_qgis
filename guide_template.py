# -*- coding: utf-8 -*-
"""
TEMPLATE : Utilisez ce fichier comme modèle pour créer vos propres guides

Instructions :
1. Copiez cette fonction
2. Modifiez le nom de la fonction (ex: create_guide_mon_operation)
3. Remplissez les étapes avec vos instructions
4. Ajoutez la fonction dans guides_predefined.py > get_all_guides()
"""

from .guide_step import Guide, GuideStep


def create_guide_template():
    """DESCRIPTION : Décrivez brièvement ce que ce guide apprend à faire"""
    
    steps = [
        # ========== ÉTAPE 1 ==========
        GuideStep(
            title="Étape 1 : [Titre de l'action]",
            description=(
                "Instructions claires pour cette étape.\n\n"
                "Vous pouvez ajouter plusieurs paragraphes.\n\n"
                "💡 Astuce : Ajoutez des conseils utiles\n"
                "⚠️ Attention : Signalez les pièges courants"
            ),
            # OPTIONNEL : Mettre en évidence un élément
            # target_widget_name="nom_du_widget"     # Pour un widget spécifique
            # target_action="Nom de l'action"        # Pour un bouton de toolbar
        ),
        
        # ========== ÉTAPE 2 ==========
        GuideStep(
            title="Étape 2 : [Titre de l'action]",
            description=(
                "Instructions pour la deuxième étape...\n\n"
                "N'hésitez pas à être précis et détaillé."
            ),
            # Exemple de highlight d'un bouton de toolbar :
            # target_action="Gestionnaire de sources de données"
        ),
        
        # ========== ÉTAPE 3 ==========
        GuideStep(
            title="Étape 3 : [Titre de l'action]",
            description=(
                "Instructions pour la troisième étape...\n\n"
                "Expliquez ce qui va se passer."
            ),
            # Exemple de highlight d'un panneau :
            # target_widget_name="mLayerTreeView"  # Panneau des couches
        ),
        
        # ========== ÉTAPE FINALE ==========
        GuideStep(
            title="✓ Félicitations !",
            description=(
                "Vous avez terminé cette opération avec succès !\n\n"
                "Résumez ce qui a été accompli et les prochaines étapes possibles."
            ),
        ),
    ]
    
    return Guide(
        name="[NOM DU GUIDE]",  # Ce qui apparaîtra dans la liste
        description="[DESCRIPTION COURTE du guide]",  # Description affichée
        steps=steps
    )


# ============================================================
# EXEMPLES DE WIDGETS QGIS COURANTS À METTRE EN ÉVIDENCE
# ============================================================

"""
Widgets principaux :
- mLayerTreeView        : Panneau des couches (à gauche)
- mMapCanvas           : Zone de la carte
- mCoordsEdit          : Affichage des coordonnées (en bas)

Actions de toolbar courantes :
- "Gestionnaire de sources de données"
- "Ouvrir le projet"
- "Enregistrer le projet"
- "Sélectionner des entités"
- "Identifier les entités"
- "Mesurer une ligne"
- "Mesurer une surface"
- "Ajouter une couche vecteur"
- "Ajouter une couche raster"

Pour trouver d'autres noms de widgets/actions :
1. Ouvrez la console Python dans QGIS
2. Exécutez ce code :
   for widget in iface.mainWindow().findChildren(QWidget):
       if widget.objectName():
           print(widget.objectName())
"""


# ============================================================
# CONSEILS POUR DE BONS GUIDES
# ============================================================

"""
✅ BONNES PRATIQUES :

1. Étapes courtes : 1 action = 1 étape
2. Titres explicites : "Étape 1 : Ouvrir X" plutôt que "Première étape"
3. Instructions détaillées : Précisez où cliquer, quel menu ouvrir, etc.
4. Feedback visuel : Utilisez des émojis (✓, ⚠️, 💡, 📖, 🎯)
5. Contexte : Expliquez POURQUOI faire cette action
6. Validation : Dites à l'utilisateur comment vérifier que ça a marché
7. Étape finale positive : Terminez par des félicitations

❌ À ÉVITER :

1. Étapes trop longues (>5 actions dans une étape)
2. Jargon technique sans explication
3. Instructions vagues ("cliquez quelque part", "faites un truc")
4. Trop d'étapes (>10-12 étapes = trop long)
5. Oublier de mentionner les pièges courants
"""


# ============================================================
# EXEMPLE COMPLET : GUIDE POUR CRÉER UN POINT
# ============================================================

def create_guide_example_create_point():
    """Exemple complet : Créer un point sur la carte"""
    
    steps = [
        GuideStep(
            title="Étape 1 : Créer une nouvelle couche ponctuelle",
            description=(
                "Pour ajouter des points sur la carte, vous devez d'abord créer une couche.\n\n"
                "Allez dans le menu :\n"
                "**Couche** > **Créer une couche** > **Nouvelle couche GeoPackage...**\n\n"
                "💡 Un GeoPackage est un format moderne qui stocke vos données géographiques."
            ),
        ),
        
        GuideStep(
            title="Étape 2 : Configurer la couche",
            description=(
                "Dans la fenêtre qui s'ouvre, configurez :\n\n"
                "1. **Base de données** : Choisissez où sauvegarder (ex: mes_points.gpkg)\n"
                "2. **Nom de la table** : Donnez un nom (ex: points_interet)\n"
                "3. **Type de géométrie** : Sélectionnez **Point**\n"
                "4. **SCR** : Gardez le système de coordonnées par défaut\n\n"
                "Cliquez sur **OK** pour créer la couche."
            ),
        ),
        
        GuideStep(
            title="Étape 3 : Activer le mode édition",
            description=(
                "Maintenant que la couche est créée, vous devez activer le mode édition.\n\n"
                "1. Sélectionnez votre nouvelle couche dans le panneau des couches\n"
                "2. Cliquez sur le bouton **Basculer en mode édition** (icône crayon)\n\n"
                "⚠️ Le mode édition permet de modifier la couche. N'oubliez pas de sauvegarder à la fin !"
            ),
            target_widget_name="mLayerTreeView"
        ),
        
        GuideStep(
            title="Étape 4 : Ajouter un point",
            description=(
                "Cliquez sur le bouton **Ajouter une entité ponctuelle** dans la barre d'outils.\n\n"
                "Ensuite, cliquez n'importe où sur la carte pour placer un point.\n\n"
                "Une fenêtre s'ouvre pour saisir les attributs. Cliquez sur **OK**."
            ),
        ),
        
        GuideStep(
            title="Étape 5 : Sauvegarder les modifications",
            description=(
                "Pour que vos modifications soient enregistrées :\n\n"
                "Cliquez sur le bouton **Sauvegarder les modifications** (icône disquette).\n\n"
                "✓ Votre point est maintenant sauvegardé !"
            ),
        ),
        
        GuideStep(
            title="✓ Bravo !",
            description=(
                "Vous avez créé votre premier point sur QGIS ! 🎉\n\n"
                "Vous pouvez maintenant :\n"
                "- Ajouter d'autres points de la même manière\n"
                "- Modifier la symbologie pour changer l'apparence\n"
                "- Ajouter des champs pour stocker plus d'informations\n\n"
                "💡 N'oubliez pas de désactiver le mode édition quand vous avez fini."
            ),
            target_widget_name="mLayerTreeView"
        ),
    ]
    
    return Guide(
        name="Créer un point sur la carte",
        description="Apprenez à créer une couche ponctuelle et à y ajouter des points.",
        steps=steps
    )
