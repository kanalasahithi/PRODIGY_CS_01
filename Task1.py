def caesar_cipher(text, shift, encrypt=True):
    result = ""
    shift = shift % 26  # Ensure shift is within 0-25

    if not encrypt:
        shift = -shift

    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            new_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += new_char
        else:
            result += char

    return result

def main():
    print("Caesar Cipher Program")
    choice = input("Would you like to encrypt or decrypt a message? (enter 'encrypt' or 'decrypt'): ").strip().lower()
    message = input("Enter your message: ").strip()
    shift = int(input("Enter the shift value: ").strip())

    if choice == 'encrypt':
        encrypted_message = caesar_cipher(message, shift, encrypt=True)
        print(f"Encrypted Message: {encrypted_message}")
    elif choice == 'decrypt':
        decrypted_message = caesar_cipher(message, shift, encrypt=False)
        print(f"Decrypted Message: {decrypted_message}")
    else:
        print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
