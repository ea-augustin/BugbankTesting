# Created by elite at 26/03/2026
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: TC ADMIN 01 - Accès admin
    Given l'utilisateur est connecté en rôle admin
    When  l'utilisateur click sur btn admin
    When l'utilisateur se rend sur la page /admin/
    Then la liste de tous les utilisateurs doit être affichée
    And les statistiques globales doivent être affichées
