from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
import datetime

# Créez un moteur pour vous connecter à la base de données
engine = create_engine('sqlite:///bdd_imc_calculator.db')

# Déclarez une classe de base pour définir le modèle
Base = declarative_base()

# Créez la classe User
class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    adresse = Column(String)
    telephone = Column(Integer)
    timestamp = Column(DateTime, default=datetime.datetime.now)
    bmi = relationship("Bmi", backref="user", uselist=False)

# Créez la classe Bmi
class Bmi(Base):
    __tablename__ = 'bmi'

    bmi_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    poids = Column(Integer)
    taille = Column(Float)
    imc_resultat = Column(Float)

# Créez la classe History
class History(Base):
    __tablename__ = 'history'

    history_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('bmi.user_id'))
    previous_bmi = Column(Float)
    current_bmi = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.now)

# Créez toutes les tables
Base.metadata.create_all(engine)
