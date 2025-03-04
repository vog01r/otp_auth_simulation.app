import requests
import random
import time
import os
from dotenv import load_dotenv
import logging

load_dotenv()

# Configuration de la journalisation
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OTPService:
    def __init__(self):
        load_dotenv()
        self.sms_api_url = os.getenv("SMS_API_URL")

    def generate_otp(self):
        """Génère un OTP aléatoire à 6 chiffres."""
        return str(random.randint(100000, 999999))

    def send_otp(self, phone_number, otp):
        """Envoie un OTP par SMS à un numéro de téléphone donné."""
        try:
            url = f"{self.sms_api_url}/send_sms"
            payload = {"phone_number": phone_number, "message": f"Votre code OTP est: {otp}"}
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Erreur lors de l'envoi de l'OTP: {e}")
            return None

    def verify_otp(self, expected_otp, user_otp):
        """Vérifie si l'OTP fourni par l'utilisateur est correct."""
        if expected_otp == user_otp:
            logging.info("✅ Code OTP validé avec succès !")
            return True
        logging.warning("❌ Code OTP incorrect.")
        return False

    def run(self):
        """Point d'entrée principal pour l'envoi et la vérification de l'OTP."""
        phone_number = input("Entrez votre numéro de téléphone : ")
        otp = self.generate_otp()
        logging.info(f"Envoi du code OTP ******* à {phone_number}...")
        if self.send_otp(phone_number, otp) is None:
            logging.error("Échec de l'envoi de l'OTP.")
            return
        
        user_otp = input("Entrez le code OTP reçu : ")
        success = self.verify_otp(otp, user_otp)
        
        if success:
            logging.info("Authentification réussie !")
        else:
            logging.error("Authentification échouée.")

if __name__ == "__main__":
    # Exécuter les tests unitaires
    
    # Lancer le service OTP
    otp_service = OTPService()
    otp_service.run()
