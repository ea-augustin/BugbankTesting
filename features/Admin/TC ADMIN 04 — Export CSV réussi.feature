Feature: Export CSV des utilisateurs
  Cette fonctionnalité permet à un administrateur de récupérer l’ensemble
  des utilisateurs enregistrés dans l’application sous forme de fichier CSV.
  L’objectif est de vérifier que l’export est accessible uniquement aux admins,
  que les données sont correctement générées et que le fichier est bien
  téléchargé sur le poste client.

  Contexte:
    Étant donné que l’utilisateur dispose d’un compte administrateur
    Et qu’il est authentifié sur l’application

  Scenario: TC ADMIN 04 — Export CSV réussi
    Given l’utilisateur est un admin
    When l’utilisateur se rend sur /admin/export/users
    Then tous les utilisateurs doivent être récupérés
    And un fichier CSV doit être généré
    And le fichier users_export.csv doit être téléchargé