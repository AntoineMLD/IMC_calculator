import sqlite3

def inserer_donnees_utilisateur(username, first_name, last_name, email, adresse, telephone ):
    conn = sqlite3.connect('bdd_imc_calculator.db')
    cur = conn.cursor()

    # Insère les données dans la table
    insert_query = "INSERT INTO user (username, first_name, last_name, email, address, telephone) VALUES (?,?,?,?,?,?)"
    cur.execute(insert_query, (username, first_name, last_name, email, adresse, telephone))

    conn.commit()
    conn.close


def inserer_donnees_bmi(poids, taille, imc_resultat):
    conn = sqlite3.connect('bdd_imc_calculator.db')
    cur = conn.cursor()

    #insère les données dans la table
    insert_query = "INSERT INTO bmi (poids, taille, imc_resultat) VALUES (?,?,?)"
    cur.execute(insert_query, (poids, taille, imc_resultat))

    conn.commit()
    conn.close