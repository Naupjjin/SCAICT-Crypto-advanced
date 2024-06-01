import random
from secret import FLAG

def main():
    for i in range(1,101):
        a=random.randint(1,50000)
        b=random.randint(1,50000)
        operations = ['+', '-', '*']
        operation = random.choice(operations)
        if operation == '+':
            correct_answer = a + b
        elif operation == '-':
            correct_answer = a - b
        elif operation == '*':
            correct_answer = a * b

        print(f"Round {i}")
        print("-"*20)
        print(f"caculator： {a} {operation} {b}")
        ans= int(input("ans= "))
        print("-"*20)
        if ans==correct_answer:
            print("correct!")
        else:
            exit()

        if i==100:
            print("*"*25)
            print("You are master of math.")
            print(FLAG)
            print("*"*25)
try:
    main()

except:
    print("failed...")
    exit()