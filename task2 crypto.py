import collections
NALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ENGLISH_LETTER_FREQUENCY = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
DICTIONARY = {"HELLO", "WORLD", "JAVA", "ENCRYPT", "DECRYPT", "ATTACK", "CIPHER", "SECURE", "MESSAGE", "CODE"}

def get_frequency_map(text):
    frequency_map = collections.Counter(c for c in text if c.isalpha())
    return frequency_map

def sort_by_frequency(frequency_map):
    return sorted(frequency_map, key=frequency_map.get, reverse=True)

def apply_substitution(text, substitution_map):
    return "".join(substitution_map.get(c, c) for c in text)

def frequency_analysis_decrypt(text):
    frequency_map = get_frequency_map(text)
    sorted_letters = sort_by_frequency(frequency_map)
    
    substitution_map = {sorted_letters[i]: ENGLISH_LETTER_FREQUENCY[i] for i in range(min(len(sorted_letters), len(ENGLISH_LETTER_FREQUENCY)))}
    return apply_substitution(text, substitution_map)

def manual_adjustment(text):
    custom_map = {}
    print("Enter manual letter mappings (e.g., A->T). Type 'done' when finished:")
    while True:
        mapping = input("Mapping: ").strip().upper()
        if mapping == "DONE":
            break
        if len(mapping) == 3 and mapping[1] == '->':
            custom_map[mapping[0]] = mapping[2]
        else:
            print("Invalid format. Use A->T")
    return apply_substitution(text, custom_map)

def main():
    encrypted_text = input("Enter the encrypted text: ").upper()
    decrypted_text = frequency_analysis_decrypt(encrypted_text)
    print("Most likely decryption:", decrypted_text)
    
    response = input("Do you want to manually adjust mappings? (yes/no): ").strip().lower()
    if response == "yes":
        decrypted_text = manual_adjustment(encrypted_text)
        print("Final adjusted decryption:", decrypted_text)

if __name__ == "__main__":
    main()