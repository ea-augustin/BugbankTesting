Feature: Mot de passe incorrect
  Cette fonctionnalité permet de vérifier le comportement de l'application
  lorsqu’un utilisateur tente de se connecter avec un mot de passe erroné.
  L’objectif est de s’assurer qu’un message d’erreur approprié est affiché
  et qu’aucune session ne peut être ouverte avec des identifiants invalides.

  Contexte:
    Étant donné qu’un compte utilisateur existe
    Et que l’utilisateur connaît son adresse email

Scenario: TC AUTH 07 — Mot de passe incorrect
  Given un compte existant
  And l’utilisateur est sur la page de connexion
  When l’utilisateur saisit un email valide
  And saisit un mot de passe incorrect
  And l’utilisateur tente de se connecter
  Then un message d’erreur doit être affiché 'Mot de passe incorrect.'
  And session ne doit être créée
