Feature: US AUTH 04 — Mot de passe actuel incorrect
  Cette fonctionnalité permet de vérifier le comportement de l'application
  lorsqu’un utilisateur tente de modifier son mot de passe
  mais saisit un mot de passe actuel erroné.

  Contexte:
    Étant donné que l’utilisateur possède un compte actif
    Et qu’il connaît son mot de passe actuel


Scenario: TC AUTH 11 - Mot de passe actuel incorrect
  Given l'utilisateur est connecte
  When Clique sur le bouton mot de passe
  When saisit un mot de passe actuel incorrect
  When saisit un nouveau mot de passe
  When saisit un mot de passe de confirmation identique
  When soumet
  Then un message d'erreur doit être affiché
  And aucun changement ne doit être sauvegardé


