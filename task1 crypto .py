import itertools

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DICTIONARY = {"HELLO", "WORLD", "JAVA", "ENCRYPT", "DECRYPT", "ATTACK", "CIPHER", "SECURE", "MESSAGE", "CODE"}

def generate_limited_permutations(alphabet, limit):
    return list(itertools.islice(itertools.permutations(alphabet), limit))

def decrypt(text, key):
    key_map = {k: v for k, v in zip(key, ALPHABET)}
    return "".join(key_map.get(c, c) for c in text)

def is_valid_english(text):
    words = text.split()
    return any(word in DICTIONARY for word in words)

def main():
    encrypted_text = input("Enter the encrypted text: ").upper()
    permutations = generate_limited_permutations(ALPHABET, 10000)
    
    for key_tuple in permutations:
        key = "".join(key_tuple)
        decrypted_text = decrypt(encrypted_text, key)
        if is_valid_english(decrypted_text):
            print("Possible decryption:", decrypted_text)
            
if __name__ == "__main__":
    main()
