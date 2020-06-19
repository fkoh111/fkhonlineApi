import pytest
from commons.helpers import MailConfig, set_subject


def test_sanity():
    """Sanity checking"""
    assert 2 + 2 == 4


def test_mail_config():
    """Testing mail config attributes"""
    mailconfig = MailConfig
    assert mailconfig.SENDER == "fkhonlinemail@gmail.com"
    assert mailconfig.RECEIVER == "frederik_kok@icloud.com"


def test_set_subject():
    """Testing if we can set subject"""
    subject = set_subject("foo", "bar")
    assert subject == "FKHONLINE | From: foo | bar"


def test_set_subject_type_error():
    with pytest.raises(TypeError):
        set_subject()
