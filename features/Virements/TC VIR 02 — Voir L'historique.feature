Feature: Consultation de l’historique des virements
  Cette fonctionnalité permet à un utilisateur de consulter l’ensemble
  des virements effectués depuis ses comptes. L’objectif est de vérifier
  que l’historique est accessible, que les informations affichées sont
  correctes et que l’utilisateur peut visualiser ses opérations passées.

  Contexte:
    Étant donné que l’utilisateur possède au moins un compte bancaire
    Et qu’il est authentifié sur l’application

  Scenario: TC VIR 02 — Voir l’historique
    Given l’utilisateur est connecté
    When utilisateur se rend sur account
    Then clique sur le bouton historique
    And l’utilisateur voir l'historique