from schema import User, engine, Bmi, History
from sqlalchemy.orm import sessionmaker

# Fonction pour enregistrer les données de l'utilisateur
def enregistrer_donnees_utilisateur(username, first_name, last_name, email, telephone, adresse, poids, taille):

    # Créer une session SQLAlchemy
    Session = sessionmaker(bind=engine)
    session = Session()

    # Créer l'objet User
    user = User(username=username, first_name=first_name, last_name=last_name, adresse=adresse, telephone=telephone, email=email)

    # Formule de l'IMC
    taille_m = taille / 100
    imc = round(poids / (taille_m * taille_m), 1)
    
    

    # Récupére l'utilisateur existant s'il y en a un
    existing_user = session.query(User).filter_by(username=username).first()

    # Si l'utilisateur existe, récupére son IMC précédent
    previous_bmi = None
    if existing_user:
        previous_bmi = existing_user.bmi.imc_resultat

    # Crée les objets User, Bmi et History
    bmi = Bmi(poids=poids, taille=taille, imc_resultat=imc)
    user.bmi = bmi
    history = History(user_id=user.user_id, previous_bmi=previous_bmi, current_bmi=bmi.imc_resultat)

    # Ajoute les objets à la session et commit
    session.add(user)
    session.add(bmi)
    session.add(history)
    session.commit()

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

    
