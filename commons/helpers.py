import os
from dotenv import load_dotenv

load_dotenv()


class MailConfig:
    """Base configs for mail"""

    PSWD = os.environ.get("PSWD")
    SENDER = "fkhonlinemail@gmail.com"
    RECEIVER = "frederik_kok@icloud.com"


def set_subject(name, mail):
    """Formatting a subject header"""
    subject = f"FKHONLINE | From: {name} | {mail}"
    return subject
