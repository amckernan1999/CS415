# A collection of functions that together form the RSA algorithm
# Written By: Max vonBlankenburg, Andrew McKernan
# Date: 9/20/21

from Crypto.Util.number import getPrime # For testing our prime_number_generator function
import random

# extended_euclidean(a,b)
# summary: recursive GCD function as shown in book
# param a: first value we are searching for a GCD of
# param b: Second value we are searching for a GCD of
# returns: GCD of a and b
def extended_euclidean(a, b):
    if b == 0 : 
        return 1, 0, a
    x1, y1, d = extended_euclidean(b, a%b)
    return y1, x1 - ((a//b) * y1), d

# egcd_iterative(a,b)
# summary: used to calculate GCD, executes faster than recursive gcd
# param a: first value we are searching for a GCD of
# param b: Second value we are searching for a GCD of
# returns: GCD of a and b
def egcd_iterative(a,b):
	while b != 0:
		temp = b
		b = a % b
		a = temp
	return a


# modexp(x, y, n)
# Summary: This is a recursive algorithm that calculates
# the value of x^y mod n
# param x: base of exponent
# param y: degree of exponent
# param n: operand to mod
# Returns: x to the y degree mod n
def modexp(x, y, n):
    if y == 0:
        return 1
    z = modexp(x, y // 2 , n)
    if y % 2 == 0:
        return (z*z) % n
    else:
        return (z*z*x) % n

# primality(n)
# Summary: This function leverages Fermat's test and modexp
# to determine if a given int is prime.
# param n: the value we test to see if it is prime
# Returns: true if prime, else false
def primality(n):
    rand = random.randint(1,n-1)

    if modexp(rand, n - 1, n) == 1:
        return True
    else:
        return False

# primality2(n,k)
# Summary: This function leverages primality and a confidence
# paremter k to execute k times so that primality is reasonably consistent
# param n: the value we test to see if it is prime
# param k: the number of times we test n for primality
# Returns: true if primality(n) is true k times, else false
def primality2(n,k):
    for i in range(k):
        if not primality(n):
            return False
    return True

# primality3(n,k)
# Summary: This function leverages primality2 in addition, speeds
# up the algorithm by first checking for simple divisible factors,
# as well as evaluates edge cases like n = 2,3,5,7.
# param n: the value we test to see if it is prime
# param k: the number of times we test n for primality
# Returns: true if primality(n) is true k times or edge case, else false
def primality3(n,k):
    if n % 2 == 0 and n != 2:
        return False
    if n % 3 == 0 and n != 3:
        return False
    if n % 5 == 0 and n != 5:
        return False
    if n % 7 == 0 and n != 7:
        return False
    return primality2(n,k)

# prime_number_generator(N,k)
# Summary: Given an integer N <= 50 and k <= 20, generates a random prime number with N digits.
# param N: number of digits in returned prime
# param k: confidence parameter of the primality value
# Returns: prime number with N digits
def prime_number_generator(N, k):
    num = random.randint(10**(N-1), (10**N)-1)
    while not primality3(num, k):
        num = random.randint(10**(N-1), (10**N)-1)
    return num

# RSA_keygen(n,k)
# Summary: Given n & k as "entropy" values, generates public key N & E and private key D.
# param n: number of digits in pre multiplcand generated primes
# param k: confidence parameter in generated primes
# returns: public key N and E, private key D
def RSA_keygen(n, k):
    # Generate N
    p = prime_number_generator(n, k)
    q = prime_number_generator(n, k)
    # p = getPrime(16)
    # q = getPrime(16)
    N = p * q

    # Generate E
    d = 0
    while d != 1:
        E = random.randint(10**(n-1), (10**n)-1)
        x, y, d = extended_euclidean(E, (p-1)*(q-1))
    
    # Generate D
    # Need to find the inverse of (E) % (p-1)(q-1)
    # By extended euclidean algorithm calculated earlier, (E)x + (p-1)(q-1)y = 1
    # By definition of modulo inverse, x % (p-1)(q-1) is the inverse of (E) % (p-1)(q-1)
    D = x % ((p-1)*(q-1))

    return N, E, D

# RSA_encrypt(N,E,M)
# Summary: Given a number and an RSA public key, encrypts the number
# param N: Public key passed to modexp
# param E: public Key passed to modecp
# Param M: int that is to be encrypted
# Returns: encrypted int
def RSA_encrypt(N, E, M):
    return modexp(M, E, N)
	
# RSA_encrypt(N,E,M)
# Summary: Given a number and an RSA public key, encrypts the number
# param N: Public key passed to modexp
# param D: private key passed to modecp
# Param C: encrypted message passed to modexp
# returns: decrypted int
def RSA_decrypt(N, D, C):
    return modexp(C, D, N)
 
# frac_add(a,b)
# Summary: Function to implement fraction addition a and b are represented as an integer pair
# Param a: first integer pair fraction representation
# Param b: second integer pair fraction representation, b != 0
# Returns: integer pair fraction representing a + b
def frac_add(a, b):
    # Multiply denominators and add
    c = [(a[0] * b[1]) + (b[0] * a[1]), a[1] * b[1]]
    return c

# frac_mult(a,b)
# Summary: Function to implement fraction multiplication a and b are represented as an integer pair
# Param a: first integer pair fraction representation
# Param b: second integer pair fraction representation
# Returns: integer pair fraction representing a * b
def frac_mult(a, b):
    c = [a[0] * b[0], a[1] * b[1]]
    return c

# frac_mult(a,b)
# Summary: Function to implement fraction division a and b are represented as an integer pair
# Param a: first integer pair fraction representation
# Param b: second integer pair fraction representation
# Returns: integer pair fraction representing a / b
def frac_div(a, b):
    c = [a[0] * b[1], a[1] * b[0]]
    return c

# frac_format(a)
# Summary: implements egcd to reduce the fraction iteratively
# Param a: unreduced fraction
# returns: reduced fraction
def frac_format(a):
    # Check for 0s
    if a[0] == 0 or a[1] == 0:
        return [0, 1]
    # Deal with negatives
    if a[1] < 0:
        a[0] = -a[0]
        a[1] = -a[1]
    # Reduce
    d = 0
    while d != 1:
        d = egcd_iterative(a[0], a[1])
        a[0] //= d
        a[1] //= d
    return a

# frac_equal(a,b)
# Summary: evaluates a and b for eqaulity based on value
# Param a: first integer pair fraction representation
# Param b: second integer pair fraction representation
# Returns: true if the fractions are equal, false otherwise
def frac_equal(a, b):
    if a[0] == b[0] and a[1] == b[1]:
        return True
    return False
	
# frac_equal(a,b)
# Summary: evaluates a and b for eqaulity based on value
# Param a: first integer pair fraction representation
# Param b: second integer pair fraction representation
# Returns: true if the fractions are equal, false otherwise
def frac_less(a, b):
    # Multiply denominators to compare, like with addition
    if (a[0] * b[1]) < (b[0] * a[1]):
        return True
    return False

# hsum(n)
# Summary: calculates value of j such that 1 + 1/2 + 1/3 + 1/4 + 1/5 + ... 1/j > n
# Param n: positive integer which the summation surpasses
# Returns: the smallest j such that the summation > n
def hsum(n):
    j = 1
    sum1 = [0, 1]
    while frac_less(sum1, [n, 1]):
        sum1 = frac_add(sum1, [1, j])
        j += 1
    return j - 1

# gsum(n)
# Summary: Takes a positive integer n and outputs the nth number of the sequence Gn = (3/2)Gn-1 + Gn-2
# Initial values are G0 = 1/19 and G1 = 3/7
# Param n: which number in the sequence we are to select
# returns: nth number in Gn
def gsum(n):
    G0 = [1, 19]
    G1 = [3, 7]
    j = 2
    if n == 0:
        return G0
    if n == 1:
        return G1
    while j <= n:
        G = frac_format(frac_add(frac_mult([3, 2], G1), G0))
        G0 = G1
        G1 = G
        j += 1
    return G
	

# main()
# Summary: Entry point, allows user to interact with RSA encrytption, gsum, and hsum,
# reads in from user input to receive inputs for calculations and outputs to the display
def main():
    message = 0
    while message != 4:
        message = int(input("1) Demonstrate RSA encryption and Decryption\n\
2) Solve hsum sequence\n\
3) Solve gsum sequence\n\
4) Quit\n\
Enter your choice as a number (1-4): "))
        # RSA Generation fails on a small percentage of cases, and I'm not sure why
        if message == 1:
            n = int(input("Enter number of digits for the primes: "))
            k = int(input("Enter number of tries for primality test: "))
            M = int(input("Enter your number to encrypt: "))
			
            N, E, D = RSA_keygen(n, k)  
            C = RSA_encrypt(N, E, M)
            M = RSA_decrypt(N, D, C)
			
            print("Encrypted message: " + str(C))
            print("Decrypted message: " + str(M))

        elif message == 2:
            n = int(input("Enter positive integer (7 or less): "))
            print("Smallest j: " + str(hsum(n)))

        elif message == 3:
            n = int(input("Enter positive integer: "))
            frac = gsum(n)
            print("Gn = " + str(frac[0]) + '/' + str(frac[1]))

#used to skip main in test file
if __name__ == "__main__" :
    main()
