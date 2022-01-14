import random

def generateNum(no_bits):
    """
    Generates a random non-negative with no-bits many random bits. If the number is even, 1 is added to ensure it's odd.
    Uses SystemRandom() for more secure random bit generation.
    """
    num = random.SystemRandom().getrandbits(no_bits)
    if num%2==0:
        num +=1
    return num

def millerTest(n, d, r):
    """
    Use the Miller-Rabin probabilistic primality test to first check if n a composite integer.
    """
    a = random.SystemRandom().randint(2, n - 2)
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for t in range(r - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True
    return False

def isPrime(n, k):
    """
    Decomposes n-1 into d*(2^r) where d is odd. Uses r and d to run the Miller-Rabin primality on n.
    The Miller-Rabin is run k times on n. The higher k is, the more certain it is that n is not composite (i.e it's prime).
    """
    
    if n < 3:
        return False
    if n % 2 == 0:
        return False

    d = n-1
    r = 0
    while d % 2 == 0:
        d = d // 2
        r += 1

    for i in range(k):
        answer = millerTest(n, d, r)
        if answer == False:
            return False
    return True

def findPrimes(no_bits, k):
    """
    Find two random primes each of which uses no_bits many random bits.
    Randomly generates non-negative integers until two different primes, p,q are found.
    k is the number of iterations to run the Miller-Rabin test.
    """
    p_is_prime = False
    while not p_is_prime:
        p = generateNum(no_bits)
        p_is_prime = isPrime(p, k)

    q_is_prime = False
    while not q_is_prime or p == q:
        q = generateNum(no_bits)
        q_is_prime = isPrime(q, k)

    return p, q

def findKeyD(phi,e):
    """
    Finds the private key d using the extended Euclidean algorithm
    """
    x = 0
    old_x = 1
    y = 1
    old_y = 0
    r = e
    old_r = phi
    
    while not r == 0:
        q = old_r // r
        old_r, r = r, old_r - q*r
        old_x, x = x, old_x - q*x
        old_y, y = y, old_y - q*y
    
    d = old_y
    return d

def generateKeys(no_bits, k, e = 65537):
    """
    Generate a public key, private key pair.
    """
    p, q = findPrimes(no_bits, k)
    n = p*q
    phi = (p-1)*(q-1)
    d = findKeyD(phi,e)
    keys = { "PUBLIC_KEY": {"n":n, "e":e}, "PRIVATE_KEY": d}
    return keys

def encrypt(public_key, message):
    """
    Takes a non-negative integer message encrypts it using the public key
    """
    if message >= public_key["n"]:
        raise ValueError("Message is too long. Consider generating larger keys.")
    return pow(message, public_key["e"], public_key["n"])

def decrypt(public_key, private_key, message):
    """
    Takes a non-negative integer message encrypts it using the public key
    """
    return pow(message, private_key, public_key["n"])

def stringToInt(message):
    """
    Convert input string message into an integer 
    """
    string_to_binary = message.encode('utf8')
    return int.from_bytes(string_to_binary, byteorder='big', signed=False)
    

def intToString(message):
    """
    Convert input integer message into a string 
    """
    int_to_bytes = message.to_bytes((message.bit_length() + 7) // 8, byteorder='big', signed=False)
    return int_to_bytes.decode()

def test(message, verbose=False, no_bits=512, e=65537, k=12):
    """
    Takes a string message, generates a public, private key pair.
    Enrcypts message then decrypts it to compare to the original message.
    """
    keys = generateKeys(no_bits, k, e)
    public_key = keys["PUBLIC_KEY"]
    private_key = keys["PRIVATE_KEY"]
    if verbose:
        print("Public key:")
        print("n: ", public_key["n"])
        print("e: ", public_key["e"])
        print("\n")
        print("Private key: ", private_key)
        print("\n")

    msg_encrypted = encrypt(public_key, stringToInt(message))
    if verbose:
        print("Encrypted Message:")
        print(msg_encrypted)
        print("\n")

    msg_decrypted = decrypt(public_key, private_key, msg_encrypted)
    if verbose:
        print("Decrypted Message as Int:")
        print(msg_decrypted)
        print("\n")
        print("Original Message:")
        print(message)
        print("\n")

    msg_final = intToString(msg_decrypted)
    if verbose:
        print("Final Message:")
        print(msg_final)

    return msg_final

test("Hello, this is RSA program", True)
