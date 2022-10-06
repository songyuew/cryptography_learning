from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
#Generate Key (RSA,DSA,EC)
encryptedpass = b"Ilik32Cod3"
key = rsa.generate_private_key(
public_exponent=65537,
key_size=2048,
backend=default_backend()
)
with open("rsakey.pem", "wb") as f:
    f.write(key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.BestAvailableEncryption(encryptedpass),
))
# Generate CSR
csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"NC"),
x509.NameAttribute(NameOID.LOCALITY_NAME, u"Raleigh"),
x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Python Cryptography"),
x509.NameAttribute(NameOID.COMMON_NAME, u"shannonbray.us"),
])).add_extension(
x509.SubjectAlternativeName([
x509.DNSName(u"shannonbray.us"),
]),
critical=False,
# Sign the CSR with our private key.
).sign(key, hashes.SHA256(), default_backend())
with open("csr.pem", "wb") as f:
    f.write(csr.public_bytes(serialization.Encoding.PEM))


