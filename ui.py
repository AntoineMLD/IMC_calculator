import tkinter as tk
from tkinter import font, ttk
from PIL import Image, ImageTk
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schema import User
from interface import enregistrer_donnees_utilisateur

# Configuration de la base de données
engine = create_engine('sqlite:///bdd_imc_calculator.db')

# Création de la fenêtre
root = tk.Tk()
root.config(bg='ivory')
root.title("Application IMC-Calculator")

# Chargement de l'image depuis le fichier.gif
background_image = Image.open('giphy.gif')
background_photo = ImageTk.PhotoImage(background_image)

# Police Matrix
matrix_font = font.Font(family='Courier', size=18)

# Canvas pour les animations
canvas = tk.Canvas(root, bg='grey', highlightthickness=0)
canvas.pack(fill='both', expand=True)

# Ajout de l'image au canevas
background = canvas.create_image(0, 0, image=background_photo, anchor='nw')

# Labels
label_username = tk.Label(root, text="Nom d'utilisateur", bg="ivory", fg="grey", font=matrix_font)
label_nom = tk.Label(root, text="Nom :", bg="ivory", fg="grey", font=matrix_font)
label_prenom = tk.Label(root, text="Prénom :", bg="ivory", fg="grey", font=matrix_font)
label_email = tk.Label(root, text="Email :", bg="ivory", fg="grey", font=matrix_font)
label_telephone = tk.Label(root, text="Téléphone :", bg="ivory", fg="grey", font=matrix_font)
label_adresse = tk.Label(root, text="Adresse :", bg="ivory", fg="grey", font=matrix_font)
label_poids = tk.Label(root, text="Poids (kg) :", bg="ivory", fg="grey", font=matrix_font)
label_taille = tk.Label(root, text="Taille (cm) :", bg="ivory", fg="grey", font=matrix_font)
label_resultat = tk.Label(root, text="", bg="ivory", fg="grey", font=matrix_font)
label_categories_imc = tk.Label(root, text="", bg="ivory", fg="grey", font=matrix_font)

# Champs de saisie
input_username = tk.Entry(root, bg="ivory", fg="grey", insertbackground="grey")
input_nom = tk.Entry(root, bg="ivory", fg="grey", insertbackground="grey")
input_prenom = tk.Entry(root, bg="ivory", fg="grey", insertbackground="grey")
input_email = tk.Entry(root, bg="ivory", fg="grey", insertbackground="grey")
input_telephone = tk.Entry(root, bg="ivory", fg="grey", insertbackground="grey")
input_adresse = tk.Entry(root, bg="ivory", fg="grey", insertbackground="grey")
input_poids = tk.Entry(root, bg="ivory", fg="grey", insertbackground="grey")
input_taille = tk.Entry(root, bg="ivory", fg="grey", insertbackground="grey")

# Fonction de calcul de l'IMC
def calculer_imc():
    username = input_username.get()
    first_name = input_nom.get()
    last_name = input_prenom.get()
    email = input_email.get()
    telephone = input_telephone.get()
    adresse = input_adresse.get()
    poids = float(input_poids.get())
    taille = float(input_taille.get())
    enregistrer_donnees_utilisateur(username, first_name, last_name, email, telephone, adresse, poids, taille)

    # Calcul de l'IMC
    taille_m = taille / 100
    imc_resultat = round(poids / (taille_m * taille_m), 1)

    # Fonction pour afficher la catégorisation de l'IMC
    def affichage(imc_resultat):
        categories_imc = {
            (40, 100): "Obésité morbide (classe III). Attention risque cardio-vasculaire extrêmement élevé",
            (35, 40): "Obésité sévère (classe II). Attention risque cardio-vasculaire très élevé !",
            (30, 35): "Obésité modérée (classe I). Attention risque cardio-vasculaire élevé !",
            (25, 30): "Surpoids ou pré-obésité. Attention risque cardio-vasculaire accru !",
            (18.5, 25): "Corpulence normale. Risque cardio-vasculaire faible !",
            (16.5, 18.5): "Maigreur. Attention risque cardio-vasculaire accru !",
            (-100, 16.5): "Maigreur extrême - dénutrition. Attention risque cardio-vasculaire élevé !"
        }

        for (min_range, max_range), category in categories_imc.items():
            if min_range <= imc_resultat <= max_range:
                return category

    # Appel de la fonction pour obtenir la catégorie
    categorie_imc = affichage(imc_resultat)

    # Création du texte avec le résultat de l'IMC
    result_text = f"IMC de {last_name} {first_name} : {imc_resultat}\nCatégorie IMC : {categorie_imc}"

    # Mise à jour de label_resultat avec le texte et une police et un style spécifiques
    label_resultat.config(text=result_text, font=("votre_police", 12, "normal"))

# Bouton "Calculer"
btn_calculer = tk.Button(root, text="Calculer", bg="ivory", fg="grey", command=calculer_imc)

# Placement des widgets
label_username.pack()
input_username.pack()

label_nom.pack()
input_nom.pack()

label_prenom.pack()
input_prenom.pack()

label_email.pack()
input_email.pack()

label_telephone.pack()
input_telephone.pack()

label_adresse.pack()
input_adresse.pack()

label_poids.pack()
input_poids.pack()

label_taille.pack()
input_taille.pack()

btn_calculer.pack(pady=20)
label_resultat.pack()

label_categories_imc.pack()

# Bouton "Quitter"
btn_quitter = tk.Button(root, text="Quitter", bg="ivory", fg="grey", command=root.quit)
btn_quitter.pack(pady=20)

root.mainloop()
