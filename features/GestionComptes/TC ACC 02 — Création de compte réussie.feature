Feature: Création d’un nouveau compte bancaire
  Cette fonctionnalité permet à un utilisateur déjà authentifié
  d’ouvrir un nouveau compte bancaire au sein de l’application.
  L’objectif est de vérifier que le formulaire de création fonctionne
  correctement, qu’un IBAN unique est généré et que le compte est
  ajouté avec un solde initial de 0.00 EUR.

  Contexte:
    Étant donné que l’utilisateur possède déjà un accès valide
    Et qu’il est authentifié sur l’application

  Scenario: TC ACC 02 — Création de compte réussie
    Given l’utilisateur est connecté
    When utilisateur se rend sur account
    Then clique sur le bouton Creer le compte
    And saisit un libellé ou garde celui par défaut
    And clique sur le bouton Creer le compte
    And l’utilisateur doit être redirigé vers le tableau de bord
    And un message de succès doit être affiché
    Then un IBAN unique doit être généré
    And le compte doit être créé avec un solde de 0.00 EUR
