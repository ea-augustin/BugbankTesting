Feature: US AUTH 05 — Les nouveaux mots de passe ne correspondent pas
  Cette fonctionnalité vérifie que l'application détecte une non‑correspondance
  entre le nouveau mot de passe et sa confirmation.

  Scenario: TC AUTH 12 - Mots de passe ne correspondent pas
    Given l’utilisateur est connecté
    When Clique sur le bouton mot de passe
    And saisit le mot de passe actuel correct
    And saisit un nouveau mot de passe
    And saisit un mot de passe de confirmation différent
    And soumet
    Then le mot de passe actuel doit être validé
    And le système doit détecter la non correspondance
    And aucun changement ne doit être sauvegardé
   