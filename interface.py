# L'utilisateur saisit son prénom :
prenom = input("Renseignez votre prénom : ")

# L'utilisateur saisit son nom:
nom = input("Renseignez votre nom : ")

# L'utilisateur saisit son email:
email = input("Renseignez votre mail : ")

# L'utilisateur saisit son téléphone :
telephone = input("Renseigner votre numéro de téléphone : ")

# L'utilisateur saisit son adresse:
adresse = input("Renseignez votre adresse postale : ")



# L'utilisateur saisit son poids (en kg)
poids = int(input("Veuillez saisir votre poids (en Kg) : ")) 

# l'utilisateur saisit sa taille
taille = float(input("Veuillez saisir votre taille (en cm) : "))
taille = taille / 100 






    

    

    # Formule de l'imc
def imc(poids,taille):
        

        # Formule de l'IMC
        result = round(poids / (taille * taille), 1)

        # Classification
        obesite_morbide =  " Obésité morbide (classe III). Attention risque cardio-vasculaire extrêmement élevé"
        obesite_moderee_II = "Obésité sévère (classe II). Attention risque cardio-vasculaire très élevé !"
        obesite_moderee_I = "Obésité modérée (classe I). Attention risque cardio-vasculaire élevé !"
        surpoids = "Surpoids ou pré-obésité. Attention risque cardio-vasculaire accru !"
        normal = "Corpulence normale. Risque cardio-vasculaire faible !"
        maigreur = " Maigreur. Attention risque cardio-vasculaire accru !"
        maigreur_extreme = "Maigreur extrême - dénutrition. Attention risque cardio-vasculaire élevé !"

        # Affichage de la catégorie de l'IMC
        if result > 40:
                print(f"Votre IMC est de {result} , {obesite_morbide}")
        elif 35 < result < 40:
                print(f"Votre IMC est de {result}, {obesite_moderee_II}")
        elif 30 < result < 35:
                print(f"Votre IMC est de {result}, {obesite_moderee_I}")
        elif 25< result < 30:
                print(f"Votre IMC est de {result}, {surpoids} ")
        elif 18.5 < result < 25:
                print(f"Votre IMC est de {result}, {normal}")
        elif 16.5 < result < 18.5:
                print(f"Votre IMC est de {result}, {maigreur}")
        elif result < 16.5:
                print(f"Votre IMC est de {result}, {maigreur_extreme}")

imc(poids,taille)