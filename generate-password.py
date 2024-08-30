import os
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    new_password = generate_password()
    os.environ['NEW_PASSWORD'] = new_password
    print(f"new pass : {new_password}")
    print(f"Password generated and stored in environment variable.")
    print(f"new pass1 in env : {os.environ['NEW_PASSWORD']}")
    print(f"new pass2 in env : {os.environ.get('NEW_PASSWORD')}")
    sys.exit(4)
