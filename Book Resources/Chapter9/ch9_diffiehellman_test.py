import hashlib, os
from binascii import hexlify
from Chapter9.ch9_diffiehellman import DiffieHellman


if __name__ == "__main__":
    """
    Test Diffie-Hellman exchange.
    """

    def exchageTest (generator, group, keyLenght, testLenght = 50):
        misses = 0

        for i in range(0,testLenght):
            alice = DiffieHellman(generator, group, keyLenght)
            bob = DiffieHellman(generator, group, keyLenght)

            alice.generateSharedKey(bob.publicKey)
            bob.generateSharedKey(alice.publicKey)

            print("============= EXCHANGE RESULT:", i, "of", testLenght)
            if (alice.getSharedKey() == bob.getSharedKey()):
                print("Shared keys match!!!")
            else:
                print("Shared keys didn't match...")
                misses+= 1

        print ("\n>>>>> TOTAL MISMATCHES:", misses, "\n")

    
    alice = DiffieHellman(2,17,1024)
    bob = DiffieHellman(2,17,1024)

    
    alice.generateSharedKey(bob.publicKey)
    bob.generateSharedKey(alice.publicKey)

    print ("\n============= ALICE:\n")
    alice.displayParameters()
    alice.displayShared()
    print("\n")
    
    print ("\n============= BOB:\n")
    bob.displayParameters()
    bob.displayShared()
    print("\n")

    print("============= EXCHANGE RESULT:")
    if (alice.getSharedKey() == bob.getSharedKey()):
        print("Shared keys match!!!")
        print("Key:", hexlify(alice.key))
    else:
        print("Shared keys didn't match...")
        print("\nAlice's Shared Secret:", alice.generateSharedSecret(alice.privateKey,bob.publicKey))
        print("\nBob's Shared Secret:", bob.generateSharedSecret(bob.privateKey,alice.publicKey))
    print("\n")

