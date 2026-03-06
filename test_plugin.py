"""
Script de test rapide pour le Guide Interactif

À exécuter dans la console Python de QGIS pour tester les fonctionnalités.
"""

# Test 1 : Importer les modules
print("=" * 50)
print("TEST 1 : Import des modules")
print("=" * 50)

try:
    from guide_interactif.guide_step import Guide, GuideStep, HighlightOverlay
    from guide_interactif.guides_predefined import get_all_guides
    print("✓ Modules importés avec succès")
except Exception as e:
    print(f"✗ Erreur d'import : {e}")
    exit()

# Test 2 : Charger les guides
print("\n" + "=" * 50)
print("TEST 2 : Chargement des guides")
print("=" * 50)

try:
    guides = get_all_guides()
    print(f"✓ {len(guides)} guides chargés")
    for i, guide in enumerate(guides, 1):
        print(f"  {i}. {guide.name} ({len(guide.steps)} étapes)")
except Exception as e:
    print(f"✗ Erreur de chargement : {e}")
    exit()

# Test 3 : Vérifier la structure des guides
print("\n" + "=" * 50)
print("TEST 3 : Vérification de la structure")
print("=" * 50)

errors = []
for guide in guides:
    if not guide.name:
        errors.append(f"Guide sans nom trouvé")
    if not guide.steps:
        errors.append(f"Guide '{guide.name}' sans étapes")
    for i, step in enumerate(guide.steps):
        if not step.title:
            errors.append(f"Étape {i+1} du guide '{guide.name}' sans titre")
        if not step.description:
            errors.append(f"Étape {i+1} du guide '{guide.name}' sans description")

if errors:
    print("✗ Erreurs trouvées :")
    for error in errors:
        print(f"  - {error}")
else:
    print("✓ Structure des guides valide")

# Test 4 : Test de navigation dans un guide
print("\n" + "=" * 50)
print("TEST 4 : Navigation dans un guide")
print("=" * 50)

try:
    guide = guides[0]  # Premier guide
    print(f"Guide : {guide.name}")
    
    # Test progression
    current, total = guide.get_progress()
    print(f"  Position initiale : {current}/{total}")
    
    # Avancer
    guide.next_step()
    current, total = guide.get_progress()
    print(f"  Après next_step() : {current}/{total}")
    
    # Reculer
    guide.previous_step()
    current, total = guide.get_progress()
    print(f"  Après previous_step() : {current}/{total}")
    
    # Réinitialiser
    guide.reset()
    current, total = guide.get_progress()
    print(f"  Après reset() : {current}/{total}")
    
    print("✓ Navigation fonctionne correctement")
except Exception as e:
    print(f"✗ Erreur de navigation : {e}")

# Test 5 : Test du dialog
print("\n" + "=" * 50)
print("TEST 5 : Création du dialog")
print("=" * 50)

try:
    from guide_interactif.guide_interactif_dialog import GuideInteractifDialog
    
    # Créer le dialog (ne pas le montrer)
    dlg = GuideInteractifDialog(iface)
    print("✓ Dialog créé avec succès")
    print(f"  Titre : {dlg.windowTitle()}")
    print(f"  Taille : {dlg.width()}x{dlg.height()}")
    
    # Fermer le dialog
    dlg.close()
except Exception as e:
    print(f"✗ Erreur de création du dialog : {e}")
    import traceback
    traceback.print_exc()

# Résumé
print("\n" + "=" * 50)
print("RÉSUMÉ DES TESTS")
print("=" * 50)
print("Si tous les tests affichent ✓, le plugin est prêt !")
print("\nPour tester l'interface complète :")
print("1. Ouvrez le plugin depuis la barre d'outils")
print("2. Sélectionnez un guide")
print("3. Cliquez sur 'Démarrer le guide'")
print("=" * 50)
