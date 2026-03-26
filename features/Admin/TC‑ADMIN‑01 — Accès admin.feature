Feature: Accès à l’espace d’administration
  Cette fonctionnalité permet à un utilisateur disposant du rôle administrateur
  d’accéder à l’interface dédiée à la gestion des utilisateurs et aux statistiques
  globales de l’application. L’objectif est de vérifier que l’accès est réservé
  aux administrateurs et que les informations essentielles s’affichent correctement.

  Contexte:
    Étant donné que l’utilisateur possède un rôle administrateur
    Et qu’il est authentifié sur l’application

  Scenario: TC ADMIN 01 — Accès admin
    Given l'utilisateur est connecté en rôle admin
    When l'utilisateur click sur btn admin
    And l'utilisateur se rend sur la page /admin/
    Then la liste de tous les utilisateurs doit être affichée
    And les statistiques globales doivent être affichées