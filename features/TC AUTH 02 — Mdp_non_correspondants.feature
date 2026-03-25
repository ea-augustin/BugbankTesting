Feature: Inscription – Mots de passe ne correspondent pas
  Cette fonctionnalité permet d’empêcher la création d’un compte
  lorsque les mots de passe saisis ne correspondent pas.
  L’objectif est de vérifier que l’erreur est correctement détectée,
  qu’un message d’erreur est affiché et qu’aucun compte n’est créé.

  Contexte:
    Étant donné que l’utilisateur n’a pas encore de compte
    Et qu’il souhaite créer un accès à l’application

  Scenario: TC AUTH 02 - Inscription - Mots de passe ne correspondent pas
  When l’utilisateur se rend sur /auth/register
  And saisit un nom d’utilisateur, un mot de passe et un mot de passe de confirmation différent
  Then clique sur le bouton 'Créer mon compte'
  Then  un message d’erreur doit être affiché 'les mots de passe ne correspondent pas'