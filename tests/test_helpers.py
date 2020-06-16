from commons.helpers import MailConfig


def test_smoke():
    """Smoke test"""
    assert 2 + 2 == 4


def test_mail_config():
    """Testing mail config attributes"""
    mailconfig = MailConfig
    assert (mailconfig.SENDER) == "fkhonlinemail@gmail.com"
    assert (mailconfig.RECEIVER) == "frederik_kok@icloud.com"
