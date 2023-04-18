import random
import math

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def generate_prime_number():
    """Generate a random prime number."""
    while True:
        num = random.randint(100, 1000)
        if is_prime(num):
            return num


def gcd(a, b):
    """Calculate the greatest common divisor of two numbers."""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def mod_inverse(a, m):
    """Calculate the modular inverse of a number."""
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
    """Generate RSA key pair."""
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


# Main
print("RSA Encryption Program")

text_fron_user = input("Enter text to encrypt: ")

# Generate RSA key pair
n, e, d = generate_rsa_key_pair()
print("Generated RSA key pair:")
print("Public key (n, e): {}".format((n, e)))
print("Private key (n, d): {}".format((n, d)))

# Encrypt the input text from the user
encrypted_text = encrypt(text_fron_user, n, e)
print("Encrypted text: {}".format(encrypted_text))
