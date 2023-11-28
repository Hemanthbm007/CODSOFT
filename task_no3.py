import random
import string

def generate_password(length, complexity):
    if complexity == 'low':
        characters = string.ascii_letters + string.digits
    elif complexity == 'medium':
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == 'high':
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase
    else:
        return "Invalid complexity level. Please choose low, medium, or high."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the length of the password: "))
    complexity = input("Enter complexity level (low/medium/high): ").lower()

    password = generate_password(length, complexity)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
