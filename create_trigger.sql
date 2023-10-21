-- Création d'un déclencheur BEFORE INSERT sur la table bmi
CREATE TRIGGER IF NOT EXISTS trigger_bmi_association
BEFORE INSERT ON bmi
FOR EACH ROW
BEGIN
    -- Rechercher l'utilisateur associé dans la table user
    SELECT user_id INTO NEW.user_id FROM user WHERE username = NEW.username;
END;