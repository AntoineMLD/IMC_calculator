from schema import User, engine, Bmi, History
from sqlalchemy.orm import sessionmaker

# Fonction pour enregistrer les données de l'utilisateur
def enregistrer_donnees_utilisateur(username, first_name, last_name, email, telephone, adresse, poids, taille):
        user = User(username=username, first_name=first_name, last_name=last_name, adresse=adresse, telephone=telephone, email=email)

        

# Formule de l'imc
def imc(poids,taille):
     taille_m = taille / 100
     imc_resultat = round(poids / (taille_m * taille_m), 1)
     return imc_resultat

# Créer la session SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()


if __name__ == "__main__":

    
        username = input("Veuillez saisir votre nom d'utilisateur : ")
        first_name = input("Renseignez votre prénom : ")
        last_name = input("Renseignez votre nom : ")
        email = input("Renseignez votre mail : ")
        telephone = input("Renseigner votre numéro de téléphone : ")
        adresse = input("Renseignez votre adresse postale : ")
        poids = int(input("Veuillez saisir votre poids (en Kg) : ")) 
        taille = float(input("Veuillez saisir votre taille (en cm) : "))
        taille = taille / 100 

        user = enregistrer_donnees_utilisateur(username, first_name, last_name, email, telephone, adresse, poids, taille)

        # Résultat de la fonction imc
        imc_resultat = imc(poids,taille) 

        # Récupère l'IMC précedent de l'utilisateur s'il existe
        previous_bmi = None

        existing_user = session.query(User).filter_by(username=username).first()
        if existing_user:
            previous_bmi = existing_user.bmi.imc_resultat
        else:
            previous_bmi = None

        # Récupère l'IMC précédent de l'utilisateur s'il existe
        previous_bmi = None
        existing_user = session.query(User).filter_by(username=username).first()
        if existing_user:
            previous_bmi = existing_user.bmi.imc_resultat

        # Créer les objets user,bmi et history
        user = User(username=username, first_name=first_name, last_name=last_name, adresse=adresse, telephone=telephone, email=email)

        bmi = Bmi(poids=poids, taille=taille, imc_resultat=imc(poids, taille))
        user.bmi = bmi

        history = History(user_id=user.user_id, previous_bmi=previous_bmi, current_bmi=bmi.imc_resultat)



        # Ajoute les objets à la session et commit
        session.add(user)
        session.add(bmi)
        session.add(history)
        session.commit()

 

    

    



    

