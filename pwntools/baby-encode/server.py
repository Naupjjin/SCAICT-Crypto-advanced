import random
import string
import base64
from secret import FLAG

def main():
    for i in range(1,101):
        letters = string.ascii_letters
        random_string = ''.join(random.choice(letters) for _ in range(10))


        encoding_choice = random.choice(['ASCII', 'base64'])

        if encoding_choice == 'ASCII':
            encoded_string = [ord(char) for char in random_string]
            print("ASCII:")
        else:
            encoded_string = base64.b64encode(random_string.encode()).decode()
            print("base64:")
        print(encoded_string)
        ans=input()
        if random_string==ans:
            print('success!')
        else:
            exit()

        if i==100:
            print(FLAG)

try:
    main()
except:
    print("failed")
    exit()