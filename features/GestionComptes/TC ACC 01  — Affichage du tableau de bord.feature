Feature: Gestion des comptes
  Cette fonctionnalité permet à l’utilisateur de consulter ses comptes
  et de visualiser le solde total consolidé.

  Scenario: TC ACC 01 - Affichage du tableau de bord
    Given utilisateur est connecte
    When utilisateur se rend sur account
    Then le solde total consolidé doit être affiché