# Function to encrypt a message using Caesar Cipher
def caesar_cipher_encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in a circular fashion
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters in a circular fashion
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Other characters (numbers, symbols) remain as they are
        else:
            result += char
    return result

# Function to decrypt a message using Caesar Cipher
def caesar_cipher_decrypt(ciphertext, shift):
    # Decrypting is just shifting in the opposite direction
    return caesar_cipher_encrypt(ciphertext, -shift)

# Function to get a valid shift value from the user
def get_shift_value():
    while True:
        try:
            shift = int(input("Enter the shift value (a number): "))
            return shift
        except ValueError:
            # Handling non-integer inputs for shift value
            print("Please enter a valid number.")

# Function to get the user's choice for encryption or decryption
def get_operation_choice():
    while True:
        choice = input("Do you want to encrypt or decrypt? Enter E for encrypt or D for decrypt: ").lower()
        if choice in ['e', 'd']:
            return choice
        else:
            # Handling invalid inputs for operation choice
            print("Please enter 'E' for encrypt or 'D' for decrypt.")

# Main function to run the program
def main():
    choice = get_operation_choice()
    text = input("Enter your message: ")
    shift = get_shift_value()

    # Perform encryption or decryption based on the user's choice
    if choice == 'e':
        result = caesar_cipher_encrypt(text, shift)
        operation = "Encrypted"
    else:
        result = caesar_cipher_decrypt(text, shift)
        operation = "Decrypted"

    # Display the result
    print(f"{operation} message: {result}")

# Check if the script is run directly (not imported) and then call main
if __name__ == "__main__":
    main()
