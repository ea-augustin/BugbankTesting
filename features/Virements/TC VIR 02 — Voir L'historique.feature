Feature: Virement entre comptes
  Cette fonctionnalité permet à l’utilisateur de voir l'historique.

  Scenario: TC VIR 02 - Voir l'historique
    Given l’utilisateur est connecté
    When utilisateur se rend sur account
    Then clique sur le bouton historique
    And l’utilisateur voir L'historique
