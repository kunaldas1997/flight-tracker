# This module sends email via MailGun Service
# mail_gun_key -> the API key generated from MailGun Dashboard
# mail_gun_domain -> the sandbox domain provided by mailgun due to free plan
# FROM_EMAIL_ADDRESS -> main email address for which MailGun is registered for
# MAILGUN_API_URL = "https://api.mailgun.net/v3/<your mail_gun_domain stated above>/messages"

# Note: personal data use has been removed for data safety purposes. Kindly signup for MailGun to test this feature

from flask import jsonify
import requests

mail_gun_key = ""
mail_gun_domain = ""

MAILGUN_API_URL = ""
FROM_EMAIL_ADDRESS = ""


def send_mail(receiver, status, data):
    response = requests.post(
        MAILGUN_API_URL,
        auth=("api", mail_gun_key),
        data={
            "from": FROM_EMAIL_ADDRESS,
            "to": "{}".format(receiver),
            "subject": "Your Flight Status: {}".format(status),
            "html": "{}".format(data),
        },
    )

    if response.status_code == 200:
        print(jsonify({"message": "Email sent"}))
    else:
        print(jsonify({"message": "Error"}))
