Feature: US AUTH 05 — Les nouveaux mots de passe ne correspondent pas
  Cette fonctionnalité vérifie que l’application empêche la modification
  du mot de passe lorsque le nouveau mot de passe et sa confirmation
  ne correspondent pas. L’objectif est de garantir l’intégrité du processus
  de sécurité et d’éviter toute mise à jour incorrecte.

  Contexte:
    Étant donné que l’utilisateur est authentifié
    Et qu’il souhaite modifier son mot de passe

  Scenario: TC AUTH 12 — Mots de passe ne correspondent pas
    Given utilisateur est connecte
    When Clique sur le bouton mot de passe
    And saisit le mot de passe actuel correct
    And saisit un nouveau mot de passe
    And saisit un mot de passe de confirmation différent
    And soumet
    Then le mot de passe actuel doit être validé
    And le système doit détecter la non correspondance
    And aucun changement ne doit être sauvegardé