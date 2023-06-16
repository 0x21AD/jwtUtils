import base64
import hashlib
import hmac

def sign_jwt(header, payload, secret):
    # Create the HMAC using the payload and header parts
    signature = hmac.new(secret.encode('utf-8'), f'{header}.{payload}'.encode('utf-8'), hashlib.md5).digest()

    # Encode the signature using Base64URL
    encoded_signature = base64.urlsafe_b64encode(signature).rstrip(b'=').decode('utf-8')

    # Construct the JWT by combining the header, payload, and signature
    jwt = f'{header}.{payload}.{encoded_signature}'

    return jwt

# Example usage
header = 'eyJhbGciOiJNRDVfSE1BQyJ9'  # Example header in Base64URL
payload = 'eyJ1c2VybmFtZSI6ImFkbWluIn0'  # Example payload in Base64URL
secret = 'fsrwjcfszegvsyfa'

jwt = sign_jwt(header, payload, secret)
print(jwt)


#eyJhbGciOiJNRDVfSE1BQyJ9.eyJ1c2VybmFtZSI6ImFzZGFzZCJ9.VUL0t8zg4O4-L0p3z8OMKQ

#eyJhbGciOiJNRDVfSE1BQyJ9.eyJ1c2VybmFtZSI6ImFzZGFzZCJ9.VUL0t8zg4O4-L0p3z8OMKQ