# Projet de Simulation d'Authentification par OTP

Ce projet propose une simulation d'authentification par mot de passe à usage unique (OTP) en utilisant des SMS et des QR Codes. Il illustre des compétences techniques avancées en matière de sécurité et de communication.

## Guide d'Installation

1. **Clonez le dépôt :**
   ```bash
   git clone https://github.com/vog01r/otp_auth_simulation.app.git
   cd otp_auth_simulation
   ```

2. **Créez et activez un environnement virtuel :**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows utilisez `venv\Scripts\activate`
   ```

3. **Installez les bibliothèques nécessaires :**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurez votre fichier `.env` :**
   ```plaintext
   SMS_API_URL=http://serveur_sms:5000
   ```

## Instructions d'Utilisation

### Envoi d'OTP via SMS

Pour envoyer un OTP par SMS, exécutez le script suivant :

```bash
python OTP_SMS/otp_auth_simulation_SMS.py
```

Ce script utilise l'API SMS pour envoyer un OTP à un numéro de téléphone spécifié. Il génère un OTP aléatoire à 6 chiffres et l'envoie via une requête HTTP POST.

### Génération et Vérification d'OTP via QR Code

Pour générer et vérifier un OTP via QR Code, exécutez les scripts suivants :

Pour générer un OTP via QR Code, exécutez le script suivant :

```bash
python OTP_APP/otp_auth_simulation_qrcode_gen.py
```

Pour vérifier un OTP via QR Code, exécutez le script suivant :

```bash
python OTP_APP/otp_auth_simulation_qrcode_use.py
```

Ce script utilise la bibliothèque `pyotp` pour générer un OTP basé sur le temps et le vérifie en comparant avec l'entrée utilisateur.

## Structure du Projet

- **OTP_SMS** : Contient le serveur API pour l'envoi et la vérification des OTP par SMS.
   - **server_api_sms.py** : Simule le serveur API pour l'envoi et la vérification des OTP par SMS.
   - **otp_auth_simulation_SMS.py** : Simule l'utilisation de l'OTP par SMS.
- **OTP_APP** : Contient l'application pour la génération et la vérification des OTP via QR Code.
   - **otp_auth_simulation_qrcode_gen.py** : Simule la génération d'un OTP via QR Code.
   - **otp_auth_simulation_qrcode_use.py** : Simule l'utilisation d'un OTP via QR Code.

## Dépendances

Le projet utilise les bibliothèques suivantes, listées dans `requirements.txt` :

- `requests`
- `python-dotenv`
- `pyotp`
- `qrcode`

## Configuration

Assurez-vous que le fichier `secret.json` contient une clé secrète valide pour la génération des OTP. Le fichier `.env` doit être configuré avec l'URL de l'API SMS.

## Remarques

- **Sécurité** : Assurez-vous que votre environnement est sécurisé et que les secrets ne sont pas exposés.
- **Synchronisation** : Vérifiez que l'heure du serveur est synchronisée pour garantir la validité des OTP basés sur le temps.

Pour toute question ou assistance, veuillez contacter l'équipe de développement.  
