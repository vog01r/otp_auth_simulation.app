import pyotp
import json
import os
from dotenv import load_dotenv
import logging
import unittest
import time

# Configuration de la journalisation
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OTPValidationService:
    def __init__(self):
        try:
            with open("secret.json", "r") as secret_file:
                secret_data = json.load(secret_file)
                self.secret = secret_data.get("secret")
                if not self.secret:
                    raise ValueError("Le secret n'est pas défini dans le fichier secret.json")
        except FileNotFoundError:
            raise FileNotFoundError("Le fichier secret.json est introuvable")
        except json.JSONDecodeError:
            raise ValueError("Erreur de décodage JSON dans le fichier secret.json")
        
        logging.info("Service de validation OTP initialisé.")

    def validate_otp(self):
        """Valide un OTP fourni par l'utilisateur."""
        try:
            # Création de l'objet TOTP
            totp = pyotp.TOTP(self.secret)

            # Génération du code attendu
            expected_otp = totp.now()
            logging.info(f"Code attendu (serveur) : {expected_otp}, Temps actuel ou la demande de code a été faite (serveur) : {time.strftime('%Y-%m-%d %H:%M:%S')}")

            # Demande du code à l'utilisateur
            user_otp = input("Entrez l'OTP affiché sur votre application : ")

            # Vérification
            if totp.verify(user_otp):
                logging.info("✅ OTP valide, la synchronisation fonctionne !")
            else:
                logging.warning("❌ OTP invalide, vérifiez votre secret ou l'heure du serveur.")
        except Exception as e:
            logging.error(f"Erreur lors de la validation de l'OTP: {e}")

if __name__ == "__main__":
    
    # Lancer le service de validation OTP
    otp_validation_service = OTPValidationService()
    otp_validation_service.validate_otp()
