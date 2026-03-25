Feature: Email inconnu
  Cette fonctionnalité permet de vérifier le comportement de l'application
  lorsque l'utilisateur tente de se connecter avec des identifiants  invalides.

  Contexte:
    Étant donné que l’utilisateur possède un compte actif
    Et qu’il connaît ses identifiants de connexion

  Scenario: TC AUTH 06 — Email inconnu
    Given l’utilisateur met sur la page de connexion
    And aucun compte n’existe avec cet email
    When l’utilisateur saisit un email inconnu et un mot de passe incorrect
    Then clique sur le bouton de connexion
    Then un message d’erreur doit être affiché 'Email ou mot de passe incorrect
    And aucune session ne doit être créée
