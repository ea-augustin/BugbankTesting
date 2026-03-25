Feature: Authentification – Connexion utilisateur
  Cette fonctionnalité permet à un utilisateur de se connecter à l'application
  en saisissant une adresse email et un mot de passe valides.
  L'objectif est de vérifier que l'accès au tableau de bord fonctionne correctement
  lorsque les identifiants sont corrects.

  Contexte:
    Étant donné que l’utilisateur possède un compte actif
    Et qu’il connaît ses identifiants de connexion


  Scenario: TC AUTH 05 — Connexion réussie
  Given l’utilisateur est sur la page de connexion
  When l’utilisateur saisit un email valide 'steve@bugbank.fr' et un mot de passe valide 'T9m#Q4v!Rp'
  Then clique sur le bouton de connexion
  Then l’utilisateur doit être redirigé vers le tableau de bord