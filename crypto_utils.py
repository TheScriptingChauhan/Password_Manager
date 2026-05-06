from cryptography.fernet import Fernet
from pathlib import Path

KEY_PATH = Path(__file__).with_name('secret.key')


def generate_key() -> bytes:
    key = Fernet.generate_key()
    KEY_PATH.write_bytes(key)
    return key


def load_key() -> bytes:
    if not KEY_PATH.exists():
        return generate_key()
    return KEY_PATH.read_bytes()


def get_fernet() -> Fernet:
    key = load_key()
    return Fernet(key)


def encrypt(plaintext: str) -> str:
    f = get_fernet()
    token = f.encrypt(plaintext.encode())
    return token.decode()


def decrypt(token: str) -> str:
    f = get_fernet()
    try:
        # token may already be plain text; handle exceptions
        return f.decrypt(token.encode()).decode()
    except Exception:
        return token
