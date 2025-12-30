-- Script SQL pour ajouter les colonnes fournisseur et nom_contact à la table charges
-- À exécuter si la migration Django ne peut pas être appliquée immédiatement

ALTER TABLE charges 
ADD COLUMN fournisseur VARCHAR(255) NULL,
ADD COLUMN nom_contact VARCHAR(255) NULL;

