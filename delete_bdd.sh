DB_NAME="bdd_imc_calculator.db"

# Vérification que le fichier de base de données existe
if [ -f "$DB_NAME" ]; then

  # Suppression du fichier de base de données
  rm "$DB_NAME"
  if [ $? -eq 0 ]; then
    echo "La base de données $DB_NAME a été supprimée avec succès."
  else
    echo "Erreur lors de la suppression de la base de données $DB_NAME."
  fi
else
  echo "La base de données $DB_NAME n'existe pas."
fi