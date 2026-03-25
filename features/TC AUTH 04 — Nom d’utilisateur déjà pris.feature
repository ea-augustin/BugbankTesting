Feature: TC AUTH 04 — Nom d’utilisateur déjà pris
  Cette fonctionnalité vérifie qu’un utilisateur ne peut pas créer un compte
  avec un nom d’utilisateur déjà existant. L’objectif est de s’assurer que
  l’application affiche un message d’erreur et recharge le formulaire.

  Contexte:
    Étant donné qu’un compte existe déjà avec ce nom d’utilisateur

  Scenario: TC AUTH 04 — Nom d’utilisateur déjà pris
    When l’utilisateur est sur la page /auth/register
    And saisit un nom d’utilisateur déjà pris
    Then clique sur le bouton Créer mon compte
    Then un message d’erreur 'nom d’utilisateur déjà pris' doit être affiché
    And le formulaire doit être affiché à nouveau