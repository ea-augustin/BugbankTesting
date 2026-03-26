Feature: Gestion des comptes
  Cette fonctionnalité permet à l’utilisateur de consulter l’ensemble
  de ses comptes bancaires ainsi que le solde total consolidé. L’objectif
  est de vérifier que le tableau de bord s’affiche correctement après
  connexion et que les informations financières sont visibles et cohérentes.

  Contexte:
    Étant donné que l’utilisateur possède au moins un compte bancaire
    Et qu’il est authentifié sur l’application

  Scenario: TC ACC 01 — Affichage du tableau de bord
    Given utilisateur est connecte
    When utilisateur se rend sur account
    Then le solde total consolidé doit être affiché