import random
import math
import logging
import os


"""setting up logger, and dynamically setting the path variable"""
# Get the path, directory, and filename of the current Python file
current_file_path = os.path.abspath(__file__)
log_directory = os.path.dirname(current_file_path)
log_filename = os.path.splitext(os.path.basename(current_file_path))[0]

# Set the log file name as 'filename.log' in the same directory as the Python file, and configure the logger
log_file = os.path.join(log_directory, log_filename + '.log')
logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)


"""Calculating the public and private keys"""
def is_prime(num):
    """Check if a random large number generated below is prime."""
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def generate_prime_number():
    """Generate a random large number, check if it is prime using the is_prime function."""
    while True:
        num = random.randint(100, 1000)
        if is_prime(num):
            return num


def gcd(a, b):
    """Calculate the greatest common divisor of two generated prime numbers."""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def mod_inverse(a, m):
    """Calculate the modular inverse of a prime number."""
    m0 = m
    y = 0
    x = 1

    if m == 1:
        return 0

    while a > 1:
        q = a // m
        t = m

        m = a % m
        a = t
        t = y

        y = x - q * y
        x = t

    if x < 0:
        x = x + m0

    return x


def generate_rsa_key_pair():
    """Generate RSA key pair"""
    p = generate_prime_number()
    q = generate_prime_number()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = mod_inverse(e, phi)

    return n, e, d


def encrypt(text_fron_user, n, e):
    """Encrypt text_fron_user using RSA encryption."""
    encrypted_text = ''
    for char in text_fron_user:
        char_ascii = ord(char)
        encrypted_char = pow(char_ascii, e, n)
        encrypted_text += str(encrypted_char) + ' '
    return encrypted_text.strip()


"""log results"""
# Main program
logger.info("RSA Encryption Program")
text_fron_user = input("Enter text to encrypt: ")

# Generate RSA key pair
n, e, d = generate_rsa_key_pair()
logger.info("Generated RSA key pair:")
logger.info("Public key (n, e): {}".format((n, e)))
logger.info("Private key (n, d): {}".format((n, d)))

# Encrypt the input text from the user
encrypted_text = encrypt(text_fron_user, n, e)
logger.info("Encrypted text: {}".format(encrypted_text))