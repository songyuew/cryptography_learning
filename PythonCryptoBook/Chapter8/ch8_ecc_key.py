from Crypto.PublicKey import ECC
key = ECC.generate(curve='P-256')
f = open('myprivatekey.pem','wt')
f.write(key.export_key(format='PEM'))
f.close()
f = open('myprivatekey.pem','rt')
key = ECC.import_key(f.read())
print (key)
