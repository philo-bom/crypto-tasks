import re

def generate_matrix(keyword):
    key = keyword.upper().replace("J", "I") + "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    used = set()
    matrix = []
    
    for char in key:
        if char not in used and char.isalpha():
            used.add(char)
            if len(matrix) % 5 == 0:
                matrix.append([])
            matrix[-1].append(char)
    
    return matrix

def display_matrix(matrix):
    print("Playfair Cipher Matrix:")
    for row in matrix:
        print(" ".join(row))

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None

def prepare_text(text):
    text = text.upper().replace("J", "I")
    prepared = []
    
    for i in range(len(text)):
        if i > 0 and text[i] == text[i - 1]:
            prepared.append('X')
        prepared.append(text[i])
    
    if len(prepared) % 2 != 0:
        prepared.append('X')
    
    return "".join(prepared)

def process_text(text, matrix, encrypt=True):
    text = prepare_text(re.sub("[^A-Z]", "", text))
    result = []
    
    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        posA, posB = find_position(matrix, a), find_position(matrix, b)
        
        if posA[0] == posB[0]:
            result.append(matrix[posA[0]][(posA[1] + (1 if encrypt else -1)) % 5])
            result.append(matrix[posB[0]][(posB[1] + (1 if encrypt else -1)) % 5])
        elif posA[1] == posB[1]:
            result.append(matrix[(posA[0] + (1 if encrypt else -1)) % 5][posA[1]])
            result.append(matrix[(posB[0] + (1 if encrypt else -1)) % 5][posB[1]])
        else:
            result.append(matrix[posA[0]][posB[1]])
            result.append(matrix[posB[0]][posA[1]])
    
    return "".join(result)

def main():
    keyword = input("Enter keyword: ").upper()
    matrix = generate_matrix(re.sub("[^A-Z]", "", keyword))
    display_matrix(matrix)
    
    text = input("Enter text (encrypt/decrypt): ")
    mode = input("Encrypt or Decrypt? (E/D): ").strip().upper()
    
    if mode == 'E':
        print("Encrypted Text:", process_text(text, matrix, True))
    elif mode == 'D':
        print("Decrypted Text:", process_text(text, matrix, False))
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()
