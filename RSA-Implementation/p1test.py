# A collection of tests measuring the proper behavior of assorted RSA_algorithm functions
# include modexp, primality, prime number generator, encrypt, and decryption
# Written by: Andrew McKernan
# Date: 10/3/2021

import unittest
from RSA_algorithm import *

class P1tests(unittest.TestCase):

    ### BEGIN MODEXP TESTS ###

    def test_lower(self):
        self.assertEqual(modexp(1,1,1), 0)

    def test_middle1(self):
        self.assertEqual(modexp(12,24,17), 16)

    def test_middle2(self):
        self.assertEqual(modexp(289, 182, 12), 1)

    def test_upper(self):
        self.assertEqual(modexp(999999999,999999999,827842), 469305)

    def test_greater_mod(self):
        self.assertEqual(modexp(10, 2, 523), 100)
	
	### BEGIN PRIMALITY2 TESTS ###
	
	#checks prime values return true
    def test_prime1_p2(self):
        self.assertTrue(primality2(17,20))

    def test_prime2_p2(self):
        self.assertTrue(primality2(67,20))

    def test_prime3_p2(self):
        self.assertTrue(primality2(131,20))

    def test_prime4_p2(self):
        self.assertTrue(primality2(2731,20))

    def test_prime5_p2(self):
        self.assertTrue(primality2(48799,20))

    def test_prime6_p2(self):
        self.assertTrue(primality2(20010079,20))

	#checks composite values return false
    def test_composite1_p2(self):
        self.assertFalse(primality2(28,20))

    def test_composite2_p2(self):
        self.assertFalse(primality2(99,20))

    def test_composite3_p2(self):
        self.assertFalse(primality2(940,20))

    def test_composite4_p2(self):
        self.assertFalse(primality2(4858,20))

    def test_composite5_p2(self):
        self.assertFalse(primality2(41553,20))

    ### BEGIN PRIMALITY3 TESTS ###
	
	#checks for equal to mod values
    def test_equalTo_2(self):
    	self.assertTrue(primality3(2,10000))

    def test_equalTo_3(self):
        self.assertTrue(primality3(3,10000))

    def test_equalTo_5(self):
        self.assertTrue(primality3(5, 10000))

    def test_equalTo_7(self):
        self.assertTrue(primality3(7,10000))
			
	#checks that divis by n values dont execute modexp
    def test_divis_2_p3(self):
        self.assertFalse(primality3(12838192,10000))

    def test_divis_3_p3(self):
        self.assertFalse(primality3(721,10000))

    def test_divis_5_p3(self):
        self.assertFalse(primality3(19238415, 10000))

    def test_divis_7_p3(self):
        self.assertFalse(primality3(889,10000))

	#checks prime values return true
    def test_prime1_p3(self):
        self.assertTrue(primality3(17,20))

    def test_prime2_p3(self):
        self.assertTrue(primality3(67,20))

    def test_prime3_p3(self):
        self.assertTrue(primality3(131,20))

    def test_prime4_p3(self):
        self.assertTrue(primality3(2731,20))

    def test_prime5_p3(self):
        self.assertTrue(primality3(48799,20))

    def test_prime6_p3(self):
        self.assertTrue(primality3(20010079,20))

	#checks composite values return false
    def test_composite1_p3(self):
        self.assertFalse(primality3(28,20))

    def test_composite2_p3(self):
        self.assertFalse(primality3(99,20))

    def test_composite3_p3(self):
        self.assertFalse(primality3(940,20))

    def test_composite4_p3(self):
        self.assertFalse(primality3(4858,20))

    def test_composite5_p3(self):
        self.assertFalse(primality3(41553,20))

    ###BEGIN prime_number_generator TESTS###

    def test_prime_gen1(self):
        n = 10
        prime = prime_number_generator(n,20)
        self.assertTrue(primality3(prime,20) and len(str(prime)) == n)

    def test_prime_gen2(self):
        n = 22
        prime = prime_number_generator(n,20)
        self.assertTrue(primality3(prime,20) and len(str(prime)) == n)

    def test_prime_gen3(self):
        n = 33
        prime = prime_number_generator(n,20)
        self.assertTrue(primality3(prime,20) and len(str(prime)) == n)

    def test_prime_gen2(self):
        n = 44
        prime = prime_number_generator(n,20)
        self.assertTrue(primality3(prime, 20) and len(str(prime)) == n)

    def test_prime_gen2(self):
        n = 50
        prime = prime_number_generator(n,20)
        self.assertTrue(primality3(prime,20) and len(str(prime)) == n)
        
		
	###BEGIN encryption and decryption tests###
	
    def test_encrypt_decrypt1(self):
        n = 3
        k = 10
        M = 24
        N, E, D = RSA_keygen(n, k)
        C = RSA_encrypt(N, E, M)
        M2 = RSA_decrypt(N, D, C)
        self.assertEqual(M,M2)

    def test_encrypt_decrypt2(self):
        n = 5
        k = 11
        M = 142
        N, E, D = RSA_keygen(n, k)
        C = RSA_encrypt(N, E, M)
        M2 = RSA_decrypt(N, D, C)
        self.assertEqual(M,M2)
	
    def test_encrypt_decrypt3(self):
        n = 10
        k = 12
        M = 1921
        N, E, D = RSA_keygen(n, k)
        C = RSA_encrypt(N, E, M)
        M2 = RSA_decrypt(N, D, C)
        self.assertEqual(M,M2)
	
    def test_encrypt_decrypt4(self):
        n = 15
        k = 13
        M = 1829182
        N, E, D = RSA_keygen(n, k)
        C = RSA_encrypt(N, E, M)
        M2 = RSA_decrypt(N, D, C)
        self.assertEqual(M,M2)

    def test_encrypt_decrypt5(self):
        n = 20
        k = 14
        M = 812843187123578129
        N, E, D = RSA_keygen(n, k)
        C = RSA_encrypt(N, E, M)
        M2 = RSA_decrypt(N, D, C)
        self.assertEqual(M,M2)
	
    def test_encrypt_decrypt6(self):
        n = 25
        k = 15
        M = 1241291200512
        N, E, D = RSA_keygen(n, k)
        C = RSA_encrypt(N, E, M)
        M2 = RSA_decrypt(N, D, C)
        self.assertEqual(M,M2)

    def test_encrypt_decrypt7(self):
        n = 50
        k = 20
        M = 9192959129312
        N, E, D = RSA_keygen(n, k)
        C = RSA_encrypt(N, E, M)
        M2 = RSA_decrypt(N, D, C)
        self.assertEqual(M,M2)
	
    def test_encrypt_decrypt8(self):
        n = 50
        k = 20   
        M = 1827489012374890123749081237489071230489712389047123890471238904712390847
        N, E, D = RSA_keygen(n, k)
        C = RSA_encrypt(N, E, M)
        M2 = RSA_decrypt(N, D, C)
        self.assertEqual(M,M2)
	
    def test_encrypt_decrypt9(self):
        n = 50
        k = 20
        M = 124
        N, E, D = RSA_keygen(n, k)
        C = RSA_encrypt(N, E, M)
        M2 = RSA_decrypt(N, D, C)
        self.assertEqual(M,M2)
	
    def test_encrypt_decrypt10(self):
        n = 50
        k = 20
        M = 1
        N, E, D = RSA_keygen(n, k)
        C = RSA_encrypt(N, E, M)
        M2 = RSA_decrypt(N, D, C)
        self.assertEqual(M,M2)


if __name__ == '__main__':
    unittest.main()
