def power(a, b, p):
    if (b == 1):
        return a;
    else:
        return pow(a,b,p)


def main():

    print ("DH Example for Chapter 8")
    print ()

    P = 0; G = 0; x = 0; a = x;
    y = 0; b = 0;
    ka = 0; kb = 0;
  
    # Both the users will be agreed upon the  public keys G and P  
    P = 23; # A prime number P is taken 
    print("The value of P:", P);  
  
    G = 9; # A primitve root for P, G is taken 
    print("The value of G:", G);  
  
    # Alice will choose the private key a  
    a = 4; # a is the chosen private key  
    print("The private key a for Alice:", a); 
    x = power(G, a, P); # gets the generated key 
      
    # Bob will choose the private key b 
    b = 3; # b is the chosen private key 
    print("The private key b for Bob:", b); 
    y = power(G, b, P); # gets the generated key 
  
    # Generating the secret key after the exchange of keys 
    ka = power(y, a, P); # Secret key for Alice 
    kb = power(x, b, P); # Secret key for Bob 
      
    print("Secret key for the Alice is:", ka); 
    print("Secret Key for the Bob is:", kb); 

    print()
      


if __name__ == '__main__':
    main()
    


