import getpass


def analyze_message(message):
    """
    Analyze the provided message and print details about its composition.
    """
    num_letters = sum(c.isalpha() for c in message)
    num_digits = sum(c.isdigit() for c in message)
    num_special = len(message) - num_letters - num_digits

    print(f"Please check whether the message you provided was correct or not using the following hints:")
    print(f"\nFirst and last characters of the message: {message[:1]}***{message[-1]}")
    print(f"Total number of characters entered: {len(message)}")
    print(f"Number of alphabetical letters: {num_letters}")
    print(f"Number of digits: {num_digits}")
    
    if num_special > 0:
        print(f"Number of special characters: {num_special}")
        print("Special characters are present in the message.")
    else:
        print("No special characters in the message.")

def caesar_cipher(text, shift, action):
    """
    Perform Caesar Cipher encryption or decryption on the provided text.
    
    Args:
        text (str): The input text to encrypt or decrypt.
        shift (int): The number of positions to shift each letter.
        action (str): 'e' for encryption, 'd' for decryption.
    
    Returns:
        str: The resulting encrypted or decrypted text.
    """
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            if action == 'e':
                result_char = chr((ord(char) - start + shift) % 26 + start)
            elif action == 'd':
                result_char = chr((ord(char) - start - shift) % 26 + start)
            else:
                raise ValueError("Invalid action. Use 'e' to encrypt or 'd' to decrypt")
            result += result_char
        else:
            result += char
    return result

def main():
    """
    Main function to run the Caesar Cipher tool. It handles user input and calls other functions as needed.
    """
    while True:
        action = input("Do you want to encrypt or decrypt a message? Input 'e' for encryption, 'd' for decryption, or 'q' to quit: ").lower()
        if action == 'q':
            print("Exiting the program. Goodbye!")
            return
        elif action in ['e', 'd']:
            break
        else:
            print("Invalid action. Please choose 'e', 'd', or 'q' to quit.")

    # Use of getpass to make the message input invisible
    message = getpass.getpass(prompt="Enter the message (invisible, type carefully): ")

    analyze_message(message)

    while True:
        try:
            shift = int(getpass.getpass(prompt="Enter the shift value (invisible, type carefully): "))
            break
        except ValueError:
            print("Invalid shift value. Please enter a valid integer.")

    if action == 'e':
        result = caesar_cipher(message, shift, 'e')
        print("\nEncrypted Message:", result)
    elif action == 'd':
        result = caesar_cipher(message, shift, 'd')
        print("\nDecrypted Message:", result)

    main()  # Return to the main menu after completing the task

if __name__ == "__main__":
    main()
