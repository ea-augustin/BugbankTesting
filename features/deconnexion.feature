Feature: Déconnexion réussie
  Cette fonctionnalité permet à un utilisateur connecté
  de se déconnecter de l’application en toute sécurité.
  L’objectif est de vérifier que la session est correctement fermée
  et que l’utilisateur est redirigé vers la page de connexion.

  Contexte:
    Étant donné que l’utilisateur possède un compte actif
    Et qu’il est actuellement connecté à l’application

  Scenario: TC AUTH 06 — Déconnexion réussie
    Given l’utilisateur est déjà connecté
    When l’utilisateur clique sur le bouton de déconnexion
    Then l’utilisateur doit être redirigé vers la page de connexion