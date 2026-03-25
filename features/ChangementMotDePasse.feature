Feature: US AUTH 04 — Changer le mot de passe
  En tant qu’utilisateur authentifié,
  Je souhaite pouvoir modifier mon mot de passe,
  Afin de sécuriser mon compte et mettre à jour mes informations d’accès.

  Contexte:
    Étant donné que l’utilisateur possède un compte actif
    Et qu’il connaît son mot de passe actuel


  Scenario: TC AUTH 10 - Changement de mot de passe réussi
    Given l’utilisateur est connecté
    Then L’utilisateur doit être redirigé vers le tableau de bord.
    When Clique sur le bouton “mot de passe
    Then L’utilisateur doit être redirigé vers le page Changer le mot de passe
    And saisit le mot de passe actuel correct, Nouveau mot de passe et Confirmer le nouveau mot de passe
    Then Clique sur le bouton Enregistrer
    Then redirigé vers le tableau de bord
    Then message de succès doit être affiché

