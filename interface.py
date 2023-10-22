from schema import User, engine, Bmi, History
from sqlalchemy.orm import sessionmaker


# Nom de l'utilisateur :
username = input("Veuillez saisir votre nom d'utilisateur : ")

# L'utilisateur saisit son prénom :
first_name = input("Renseignez votre prénom : ")

# L'utilisateur saisit son nom:
last_name = input("Renseignez votre nom : ")

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
        imc_resultat= round(poids / (taille * taille), 1)
        return imc_resultat


# Résultat de la fonction imc
imc_resultat = imc(poids,taille) 


# Fonction pour afficher la catégorisation de imc_resultat
def affichage(imc):
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
        if min_range < imc_resultat < max_range:
            print(f"Votre IMC est de {imc_resultat}, {category}")



# Créer la session SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()

# Récupère l'IMC précedent de l'utilisateur s'il existe
previous_bmi = None

existing_user = session.query(User).filter_by(username=username)
if existing_user:
     previous_bmi = existing_user.bmi.imc_resultat

     
# Crée les objets user, bmi et history
user = User(username=username, first_name=first_name, last_name=last_name, adresse=adresse, telephone=telephone, email=email)

bmi = Bmi(poids=poids, taille=taille, imc_resultat=imc_resultat)
user.bmi = bmi

history = History(user_id=user.user_id, previous_bmi=previous_bmi, current_bmi=imc_resultat)





# Ajoute les objets à la session et commit
session.add(user)
session.add(bmi)
session.add(history)
session.commit()





imc(poids, taille)
affichage(imc)



