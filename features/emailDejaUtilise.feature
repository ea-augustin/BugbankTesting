Feature: TC AUTH 03 — Email déjà utilisé
  Cette fonctionnalité vérifie qu’un utilisateur ne peut pas créer un compte
  avec une adresse email déjà existante. L’objectif est de s’assurer que
  l’application affiche un message d’erreur et recharge le formulaire.

  Contexte:
    Étant donné que l’utilisateur possède déjà un compte actif

  Scenario: TC AUTH 03 — Email déjà utilisé
    When l’utilisateur est sur la page /auth/register
    And saisit un nom d’utilisateur et un email déjà existant
    Then clique sur le bouton Créer mon compte
    Then un message d’erreur 'email déjà utilisé' doit être affiché
    And le formulaire doit être affiché à nouveau
