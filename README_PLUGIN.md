# Guide Interactif QGIS 📖

Plugin QGIS pour l'ONF offrant des guides interactifs pas à pas pour apprendre à utiliser QGIS.

## Fonctionnalités ✨

- **Guides pas à pas** : Instructions détaillées pour différentes opérations
- **Mise en évidence d'interface** : Les éléments à utiliser sont automatiquement mis en surbrillance
- **Barre de progression** : Suivez votre avancement dans le guide
- **Navigation intuitive** : Boutons Précédent/Suivant pour parcourir les étapes

## Guides disponibles 📚

1. **Ajouter une couche vecteur** - Importer des données dans QGIS
2. **Créer une zone tampon (buffer)** - Utiliser les outils de géotraitement
3. **Modifier la symbologie** - Changer l'apparence des couches
4. **Créer un point sur la carte** - Digitaliser des points

## Installation 💾

1. Copiez le dossier `guide_interactif` dans :
   ```
   ~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/
   ```

2. Redémarrez QGIS

3. Activez le plugin dans **Extensions** > **Installer/Gérer les extensions** > **Installées**

4. Le plugin apparaît dans la barre d'outils avec l'icône 📖

## Utilisation 🚀

1. Cliquez sur l'icône du plugin dans la barre d'outils
2. Sélectionnez un guide dans la liste
3. Cliquez sur **▶ Démarrer le guide**
4. Suivez les instructions étape par étape
5. Utilisez **💡 Afficher l'élément** pour voir où se trouve l'élément d'interface

## Créer vos propres guides 🛠️

Consultez le fichier [GUIDE_DEV.md](GUIDE_DEV.md) pour apprendre à créer vos propres guides personnalisés.

Un fichier template est disponible dans [guide_template.py](guide_template.py).

### Exemple rapide

```python
from .guide_step import Guide, GuideStep

def create_guide_mon_operation():
    steps = [
        GuideStep(
            title="Étape 1 : Faire quelque chose",
            description="Instructions détaillées...",
            target_widget_name="nom_du_widget"  # Optionnel
        ),
        # ... autres étapes
    ]
    
    return Guide(
        name="Mon opération",
        description="Description courte",
        steps=steps
    )
```

Ajoutez votre guide dans `guides_predefined.py` > `get_all_guides()`.

## Architecture du code 🏗️

```
guide_interactif/
├── guide_step.py           # Classes Guide, GuideStep, HighlightOverlay
├── guides_predefined.py    # Guides prédéfinis
├── guide_interactif_dialog.py  # Interface utilisateur
├── guide_interactif.py     # Plugin principal QGIS
├── guide_template.py       # Template pour créer de nouveaux guides
└── GUIDE_DEV.md           # Documentation développeur complète
```

## Développement 💻

### Tester en mode développement

1. Créez un lien symbolique vers votre dossier de développement :
   ```bash
   ln -s /chemin/vers/guide_interactif ~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/guide_interactif
   ```

2. Installez **Plugin Reloader** pour recharger le plugin sans redémarrer QGIS

3. Modifiez le code, rechargez avec Plugin Reloader, testez !

### Ajouter un nouveau guide

1. Ouvrez `guides_predefined.py`
2. Créez une nouvelle fonction `create_guide_xxx()`
3. Ajoutez-la dans `get_all_guides()`
4. Rechargez le plugin

## Dépannage 🔧

**Le plugin n'apparaît pas** :
- Vérifiez que le lien symbolique ou le dossier est au bon endroit
- Vérifiez que le plugin est activé dans le gestionnaire d'extensions
- Consultez la console Python de QGIS pour voir les erreurs

**Le highlight ne fonctionne pas** :
- Le nom du widget peut être incorrect
- Certains éléments ne sont pas toujours disponibles
- Consultez [GUIDE_DEV.md](GUIDE_DEV.md) pour trouver les noms de widgets

**Erreur au démarrage** :
- Vérifiez que tous les fichiers Python sont présents
- Vérifiez la syntaxe dans vos guides personnalisés

## À venir 🚧

- [ ] Guides avec conditions (si couche sélectionnée, alors...)
- [ ] Historique des guides complétés
- [ ] Export/import de guides personnalisés
- [ ] Support multilingue
- [ ] Intégration de vidéos/GIF dans les étapes

## Auteur ✍️

**Robin FICHT** - ONF  
📧 robin.ficht@onf.fr

## Licence 📄

GNU General Public License v2.0 ou ultérieure

---

**💡 Astuce** : Utilisez ce plugin pour former vos collègues aux opérations courantes dans QGIS !
