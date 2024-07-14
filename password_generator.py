import string
import random
import argparse

def generate_password(length, use_letters, use_numbers, use_symbols):
    character_set = ''
    
    if use_letters:
        character_set += string.ascii_letters
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation
    
    if not character_set:
        raise ValueError("At least one character set must be selected")
    
    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description="Generate a random password based on user-defined criteria")
    parser.add_argument('-l', '--length', type=int, required=True, help='Length of the password')
    parser.add_argument('--letters', action='store_true', help='Include letters in the password')
    parser.add_argument('--numbers', action='store_true', help='Include numbers in the password')
    parser.add_argument('--symbols', action='store_true', help='Include symbols in the password')

    args = parser.parse_args()

    try:
        password = generate_password(args.length, args.letters, args.numbers, args.symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
