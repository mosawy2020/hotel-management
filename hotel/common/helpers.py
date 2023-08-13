from django.contrib.auth import get_user_model

User = get_user_model()


def validated(data=[], except_these=[]):
    return {key: value for key, value in data.items() if key not in except_these}
from django.contrib.auth.hashers import check_password

# The hashed password
hashed_password = 'pbkdf2_sha256$600000$FY8loPkW1azqecivIhzbno$kmTW6XjsJtC3w6B/g6UHXshqLEAg9e+Mt7Ii6BUTmoc='

# The password to check
password = 'ypassword'

# Check if the password matches the hashed password
if check_password(password, hashed_password):
    print('Password is correct')
else:
    print('Password is incorrect')
