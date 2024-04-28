import secrets 
import string 
text = string.ascii_letters + string.digits 
password = ''.join(secrets.choice(text) for i in range(10)) 
print(password)