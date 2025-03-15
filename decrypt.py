def decrypt_caesar(ciphertext, shift=3):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # Determine if character is uppercase or lowercase
            is_upper = char.isupper()
            # Convert to number (0-25)
            num = ord(char.upper()) - ord('A')
            # Apply decryption formula
            decrypted_num = (num - shift) % 26
            # Convert back to letter
            decrypted_char = chr(decrypted_num + ord('A'))
            # Preserve original case
            if not is_upper:
                decrypted_char = decrypted_char.lower()
            plaintext += decrypted_char
        else:
            # Keep non-alphabetic characters unchanged
            plaintext += char
    return plaintext