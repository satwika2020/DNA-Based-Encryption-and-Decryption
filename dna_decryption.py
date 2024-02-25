import json
import hashlib
import base64

def load_dna_mapping(file_path):
    with open(file_path, "r") as dna_file:
        return json.load(dna_file)

def decrypt_input(cipher_text, dna_mapping):
    cipher_text = cipher_text.replace(" ", "")
    decoded_result = []

    for i in range(0, len(cipher_text), 3):
        triplet = cipher_text[i:i + 3]
        decoded_result.append(dna_mapping.get(triplet, ''))

    return ''.join(str(symbol) for symbol in decoded_result)

def encode_base64(input_str):
    return base64.b64encode(input_str.encode()).decode()

def main():
    dna_file_path = "C:/Users/chamarthiramesh/DNA_Cryptography/dna.json"
    dna_mapping = load_dna_mapping(dna_file_path)

    user_cipher_text = input("Enter the cipher text for decryption: ")
    decrypted_output = decrypt_input(user_cipher_text, dna_mapping)

    print(f"Decryption Result: {decrypted_output}")

    # Adding a call to encode input in base64
    encoded_input = encode_base64(user_cipher_text)
    print(f"Encoded Base64 Input: {encoded_input}")

if __name__ == "__main__":
    main()
