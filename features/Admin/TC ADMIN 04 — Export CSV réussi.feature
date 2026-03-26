# Created by elite at 26/03/2026
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: TC ADMIN 04 - Export CSV réussi
  Given l’utilisateur est un admin
  When l’utilisateur se rend sur /admin/export/users
  Then tous les utilisateurs doivent être récupérés
  And un fichier CSV doit être généré
  And le fichier users_export.csv doit être téléchargé