import hmac
import hashlib
import base64

def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), hashlib.md5).digest()


Target = "VUL0t8zg4O4-L0p3z8OMKQ"
       
#eyJhbGciOiJNRDVfSE1BQyJ9.eyJ1c2VybmFtZSI6ImFzZGFzZCJ9.VUL0t8zg4O4-L0p3z8OMKQ
data = "eyJhbGciOiJNRDVfSE1BQyJ9.eyJ1c2VybmFtZSI6ImFzZGFzZCJ9"

# eyJhbGciOiJNRDVfSE1BQyJ9.eyJ1c2VybmFtZSI6InRlc3R0ZXN0In0.uI-1TTH5Chj0vzAdYTRKUg



with open("wordlist.txt" , "r") as f:
    wordlist = f.readlines()
    


for key in wordlist:

    key = key.replace("\n","")
    if (Target == base64.urlsafe_b64encode(hmac_md5(key,data)).rstrip(b'=').decode('utf-8')):
        
        print(f"Found key = {key}")
        
        
