# Created by elite at 26/03/2026
Feature: Virement entre comptes
  Cette fonctionnalité permet à l’utilisateur d’effectuer un virement entre deux comptes.

  Scenario: TC VIR 01 - Virement réussi
    Given l’utilisateur est connecté
    When utilisateur se rend sur account
    Then clique sur le bouton Virement
    When l’utilisateur se rend sur /transfer/
    And sélectionne le compte source
    And saisit l’IBAN destinataire
    And saisit le montant
    And saisit libelle
    And soumet virement
    Then toutes les validations doivent réussir
    And le compte source doit être débité
    And le compte destinataire doit être crédité
