# -*- coding: utf-8 -*-
"""
Guides prédéfinis pour différentes opérations dans QGIS
"""

from .guide_step import Guide, GuideStep


def create_guide_change_language():
    """Guide pour changer la langue de QGIS - Guide de test simple"""
    steps = [
        GuideStep(
            title="Étape 1 : Ouvrir les préférences",
            description=(
                "Allez dans le menu **Édition** > **Préférences** (ou **Options** selon votre version).\n\n"
                "Une fenêtre de configuration s'ouvre avec plusieurs onglets."
            ),
        ),
        
        GuideStep(
            title="Étape 2 : Aller dans l'onglet Interface",
            description=(
                "Dans le menu de gauche, cliquez sur **Interface**.\n\n"
                "Cet onglet contient les paramètres de présentation de QGIS."
            ),
        ),
        
        GuideStep(
            title="Étape 3 : Trouver la section Langue",
            description=(
                "Cherchez la section **Langue** ou **Language**.\n\n"
                "Vous devriez voir un menu déroulant avec les langues disponibles.\n\n"
                "💡 Les langues disponibles dépendent de ce qui est installé sur votre système."
            ),
        ),
        
        GuideStep(
            title="Étape 4 : Changer la langue",
            description=(
                "Cliquez sur le menu déroulant de la langue.\n\n"
                "Sélectionnez une autre langue (par exemple : English, Español, Deutsch, etc.).\n\n"
                "⚠️ La nouvelle langue s'appliquera après redémarrage de QGIS."
            ),
        ),
        
        GuideStep(
            title="Étape 5 : Appliquer les changements",
            description=(
                "Cliquez sur le bouton **OK** ou **Appliquer** pour sauvegarder les changements.\n\n"
                "La fenêtre de préférences se ferme."
            ),
        ),
        
        GuideStep(
            title="Étape 6 : Redémarrer QGIS (optionnel)",
            description=(
                "Pour que le changement de langue prenne effet, vous devez redémarrer QGIS.\n\n"
                "Allez dans **Fichier** > **Quitter** pour fermer QGIS.\n\n"
                "Puis relancez QGIS. L'interface s'affichera dans la nouvelle langue ! 🌍"
            ),
        ),
        
        GuideStep(
            title="✓ Langue changée !",
            description=(
                "Bravo ! Vous avez réussi à changer la langue de QGIS.\n\n"
                "Vous pouvez maintenant :\n"
                "- Recommencer pour essayer une autre langue\n"
                "- Revenir à votre langue préférée\n"
                "- Explorer QGIS dans une nouvelle langue\n\n"
                "💡 **Astuce** : Ce guide fonctionne aussi pour tester le plugin avec différentes interfaces !"
            ),
        ),
    ]
    
    return Guide(
        name="Changer la langue de QGIS",
        description="Guide simple pour changer la langue de l'interface QGIS (idéal pour tester le plugin).",
        steps=steps
    )


def get_all_guides():
    """Retourne tous les guides disponibles"""
    return [
        create_guide_change_language(),  # Guide de test simple
        create_guide_add_vector_layer(),
        create_guide_create_buffer(),
        create_guide_change_symbology(),
        create_guide_create_point(),  # Guide d'exemple
    ]


def create_guide_add_vector_layer():
    """Guide pour ajouter une couche vecteur"""
    steps = [
        GuideStep(
            title="Étape 1 : Ouvrir le gestionnaire de sources de données",
            description="Cliquez sur le bouton 'Gestionnaire de sources de données' dans la barre d'outils principale.\n\n"
                       "Vous pouvez aussi utiliser le raccourci Ctrl+L.",
            target_action="Gestionnaire de sources de données"
        ),
        GuideStep(
            title="Étape 2 : Sélectionner le type de source",
            description="Dans la fenêtre qui s'ouvre, sélectionnez 'Vecteur' dans le menu de gauche.\n\n"
                       "Cela vous permettra d'ajouter des fichiers de type Shapefile, GeoJSON, etc.",
            target_widget_name=None  # On pourrait cibler le bouton Vecteur
        ),
        GuideStep(
            title="Étape 3 : Parcourir et sélectionner votre fichier",
            description="Cliquez sur le bouton '...' à côté de 'Jeu de données vecteur'.\n\n"
                       "Naviguez jusqu'au fichier que vous voulez ajouter (ex: .shp, .geojson).\n\n"
                       "Sélectionnez le fichier et cliquez sur 'Ouvrir'.",
            target_widget_name=None
        ),
        GuideStep(
            title="Étape 4 : Ajouter la couche",
            description="Cliquez sur le bouton 'Ajouter' en bas de la fenêtre.\n\n"
                       "Votre couche apparaîtra dans le panneau des couches à gauche et sur la carte.",
            target_widget_name=None
        ),
        GuideStep(
            title="✓ Félicitations !",
            description="Vous avez ajouté avec succès une couche vecteur à votre projet QGIS.\n\n"
                       "La couche est maintenant visible dans le panneau des couches et sur la carte.",
            target_widget_name="mLayerTreeView"  # Le panneau des couches
        ),
    ]
    
    return Guide(
        name="Ajouter une couche vecteur",
        description="Apprenez à ajouter une couche vecteur (Shapefile, GeoJSON, etc.) à votre projet QGIS.",
        steps=steps
    )


def create_guide_create_buffer():
    """Guide pour créer une zone tampon"""
    steps = [
        GuideStep(
            title="Étape 1 : Ouvrir la boîte à outils",
            description="Cliquez sur le menu 'Traitement' > 'Boîte à outils'.\n\n"
                       "La boîte à outils contient tous les algorithmes de géotraitement.",
            target_widget_name=None
        ),
        GuideStep(
            title="Étape 2 : Rechercher 'Tampon'",
            description="Dans la barre de recherche de la boîte à outils, tapez 'tampon' ou 'buffer'.\n\n"
                       "L'algorithme s'appelle 'Tampon' dans la section 'Géométrie vectorielle'.",
            target_widget_name=None
        ),
        GuideStep(
            title="Étape 3 : Configurer les paramètres",
            description="Double-cliquez sur 'Tampon' pour ouvrir la fenêtre de paramètres.\n\n"
                       "- Sélectionnez la couche source\n"
                       "- Définissez la distance du tampon (en mètres ou unités de la couche)\n"
                       "- Choisissez où sauvegarder le résultat",
            target_widget_name=None
        ),
        GuideStep(
            title="Étape 4 : Exécuter l'algorithme",
            description="Cliquez sur 'Exécuter' en bas de la fenêtre.\n\n"
                       "QGIS créera une nouvelle couche avec les zones tampons autour de vos entités.",
            target_widget_name=None
        ),
        GuideStep(
            title="✓ Zone tampon créée !",
            description="La nouvelle couche avec les zones tampons a été ajoutée à votre projet.\n\n"
                       "Vous pouvez maintenant la styliser ou l'utiliser pour d'autres analyses.",
            target_widget_name="mLayerTreeView"
        ),
    ]
    
    return Guide(
        name="Créer une zone tampon (buffer)",
        description="Apprenez à créer des zones tampons autour de vos entités vectorielles.",
        steps=steps
    )


def create_guide_change_symbology():
    """Guide pour changer la symbologie d'une couche"""
    steps = [
        GuideStep(
            title="Étape 1 : Sélectionner la couche",
            description="Dans le panneau des couches (à gauche), faites un clic droit sur la couche dont vous voulez modifier la symbologie.",
            target_widget_name="mLayerTreeView"
        ),
        GuideStep(
            title="Étape 2 : Ouvrir les propriétés",
            description="Dans le menu contextuel, cliquez sur 'Propriétés...'.\n\n"
                       "Une fenêtre s'ouvre avec tous les paramètres de la couche.",
            target_widget_name=None
        ),
        GuideStep(
            title="Étape 3 : Aller dans l'onglet Symbologie",
            description="Cliquez sur l'onglet 'Symbologie' dans le menu de gauche.\n\n"
                       "C'est ici que vous pouvez changer les couleurs, les styles, etc.",
            target_widget_name=None
        ),
        GuideStep(
            title="Étape 4 : Choisir un style",
            description="En haut, vous pouvez choisir différents types de rendu :\n\n"
                       "- Symbole unique : une seule couleur pour tous\n"
                       "- Catégorisé : couleurs différentes par catégorie\n"
                       "- Gradué : couleurs dégradées selon des valeurs\n"
                       "- etc.\n\n"
                       "Modifiez les couleurs et styles selon vos besoins.",
            target_widget_name=None
        ),
        GuideStep(
            title="Étape 5 : Appliquer les changements",
            description="Cliquez sur 'Appliquer' pour voir le résultat sans fermer la fenêtre,\n"
                       "ou sur 'OK' pour appliquer et fermer.\n\n"
                       "Vos modifications sont maintenant visibles sur la carte !",
            target_widget_name=None
        ),
        GuideStep(
            title="✓ Symbologie modifiée !",
            description="Votre couche a maintenant un nouveau style.\n\n"
                       "Vous pouvez recommencer pour affiner ou essayer d'autres styles.",
            target_widget_name=None
        ),
    ]
    
    return Guide(
        name="Modifier la symbologie d'une couche",
        description="Apprenez à changer l'apparence visuelle de vos couches (couleurs, styles, etc.).",
        steps=steps
    )


def create_guide_create_point():
    """Guide pour créer des points sur la carte"""
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
