# Created by elite at 26/03/2026
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: TC ACC 02 - Création de compte réussie
    Given l’utilisateur est connecté
    When utilisateur se rend sur account
    Then clique sur le bouton  Ouvrir un compte
    And saisit un libellé ou garde celui par défaut
    And clique sur le bouton Creer le compte
    And l’utilisateur doit être redirigé vers le tableau de bord
    And un message de succès doit être affiché
    Then un IBAN unique doit être généré
    And le compte doit être créé avec un solde de 0.00 EUR

