Feature: Inscription réussie
  Cette fonctionnalité permet à un nouvel utilisateur de créer un compte
  en fournissant des informations valides.
  L’objectif est de vérifier que l’inscription est correctement effectuée,
  qu’un message de confirmation est affiché et que l’utilisateur est
  redirigé vers la page de connexion.

  Contexte:
    Étant donné que l’utilisateur n’a pas encore de compte
    Et qu’il souhaite créer un accès à l’application


  Scenario: TC AUTH 01 — Inscription réussie
  When l’utilisateur est sur la page d’inscription /auth/register
  And saisit un nom d’utilisateur, un email, un mot de passe et une confirmation valides
  Then clique sur le bouton Créer mon compte
  And message de succes doit être affiché
  Then l’utilisateur doit être redirigé vers /auth/login








