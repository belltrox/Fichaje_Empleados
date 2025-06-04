import hashlib
import binascii
import os

def hash_password(password):
    """Genera un hash seguro de la contraseña usando PBKDF2"""
    salt = os.urandom(16)
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000
    )
    return f"{binascii.hexlify(salt).decode()}:{binascii.hexlify(key).decode()}"

def verify_password(stored_password, provided_password):
    """Verifica si la contraseña proporcionada coincide con el hash almacenado"""
    salt, key = stored_password.split(":")
    salt = binascii.unhexlify(salt.encode())
    new_key = hashlib.pbkdf2_hmac(
        'sha256',
        provided_password.encode('utf-8'),
        salt,
        100000
    )
    return binascii.hexlify(new_key).decode() == key