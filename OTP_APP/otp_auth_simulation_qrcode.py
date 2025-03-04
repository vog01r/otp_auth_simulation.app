import pyotp
import json
import os
from dotenv import load_dotenv
import logging
import qrcode
import unittest


# Configuration de la journalisation
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QRCodeService:
    def __init__(self):
        load_dotenv()
        # Générer un nouveau secret encodé en base32
        self.secret = pyotp.random_base32()
        logging.info(f"Nouveau secret: {self.secret}")
        print(f"Merci de récupérer votre secret : {self.secret}")
        self.save_secret_to_json()

    def save_secret_to_json(self):
        """Sauvegarde le secret dans un fichier secret.json."""
        secret_data = {"secret": self.secret}
        with open("secret.json", "w") as secret_file:
            json.dump(secret_data, secret_file)
        logging.info("Secret sauvegardé dans secret.json.")

    def generate_qr_code(self):
        """Génère un QR Code pour Google Authenticator."""
        uri = pyotp.totp.TOTP(self.secret).provisioning_uri(name="user@example.com", issuer_name="MonService")
        qr = qrcode.make(uri)
        qr.show()  # Afficher le QR Code
        logging.info("QR Code généré et affiché.")

    def verify_otp(self):
        """Vérifie un OTP fourni par l'utilisateur."""
        totp = pyotp.TOTP(self.secret)
        otp = input("Entrez votre OTP: ")
        if totp.verify(otp):
            logging.info("OTP valide ✅")
        else:
            logging.warning("OTP invalide ❌")

    def run(self):
        """Point d'entrée principal pour la génération et la vérification de l'OTP via QR Code."""
        try:
            self.generate_qr_code()
            self.verify_otp()
        except Exception as e:
            logging.error(f"Erreur dans le processus de génération ou de vérification de l'OTP: {e}")

if __name__ == "__main__":
    
    # Lancer le service QR Code
    qr_code_service = QRCodeService()
    qr_code_service.run()
