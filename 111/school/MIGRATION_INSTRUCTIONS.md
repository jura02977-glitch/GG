# Instructions pour appliquer la migration

## Problème
L'erreur `Unknown column 'charges.nom_contact' in 'field list'` indique que les colonnes `fournisseur` et `nom_contact` n'existent pas encore dans la table `charges` de la base de données.

## Solution 1 : Exécuter la migration Django (Recommandé)

### Sur Railway (Production)
1. Connectez-vous à votre projet Railway
2. Ouvrez le terminal Railway ou utilisez Railway CLI
3. Exécutez la commande :
   ```bash
   python manage.py migrate
   ```
   ou spécifiquement :
   ```bash
   python manage.py migrate Schoolapp 0010_add_fournisseur_nom_contact_to_charge
   ```

### En local (si la base de données est accessible)
```bash
cd 111/school
python manage.py migrate Schoolapp 0010_add_fournisseur_nom_contact_to_charge
```

## Solution 2 : Exécuter le script SQL directement

Si vous avez accès à la base de données MySQL directement (via Railway MySQL service ou phpMyAdmin), exécutez le script SQL suivant :

```sql
ALTER TABLE charges 
ADD COLUMN fournisseur VARCHAR(255) NULL,
ADD COLUMN nom_contact VARCHAR(255) NULL;
```

Le fichier `add_charge_fields.sql` contient ce script.

## Vérification

Après avoir appliqué la migration, vérifiez que les colonnes existent :
```sql
DESCRIBE charges;
```

Vous devriez voir les colonnes `fournisseur` et `nom_contact` dans la liste.

