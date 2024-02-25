import json

def read_dna_mapping(file_path):
    with open(file_path, "r") as dna_file:
        return json.load(dna_file)

def encrypt_text(input_text, dna_mapping):
    keys, values = list(dna_mapping.keys()), list(dna_mapping.values())
    encrypted_result = []

    for char in input_text:
        if char in values:
            encrypted_result.append(keys[values.index(char)])
        else:
            encrypted_result.append(char)

    return ''.join(str(s) for s in encrypted_result)

def main():
    dna_file_path = "C:/Users/chamarthiramesh/DNA_Cryptography/dna.json"
    dna_map = read_dna_mapping(dna_file_path)

    user_input = str(input("Enter text for encryption: "))
    encrypted_output = encrypt_text(user_input, dna_map)

    print(f"Encrypted Result: {encrypted_output}")

if __name__ == "__main__":
    main()
