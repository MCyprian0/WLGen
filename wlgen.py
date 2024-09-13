'''
WLGEN v 1.0
Author: ZeroCypher

!!!DISCLAIMER!!!
This script makes a personalized wordlist, intended to make brute force attacks.
Unauthorized attacks are illegal and NOT supported by this author.

How to use:
Insert one or more words, preferably already known through the information gathering.
The script will generate a file (wl_gen.txt) with all possible combinations.
'''

import itertools

# function to generate all possible combinations.
def change_word(word):
    changes = [word]
    changes.append(word.capitalize())
    changes.append(word.upper())
    for i in range(10):
        changes.append(word + str(i))
    special_caracters = [
        "`", "˜", "!", "@", "#", "$", "%", "ˆ", "&", "*", "(", ")", "-", "_", "+", "=",
        "?", "<", ">", "/", "|", "\\", "]", "[", "}", "{", ";", ":", "'", '"'
    ]
    for char in special_caracters:
        changes.append(word + char)

    return changes

# function to create the wordlist
def wordlist(words):
    comb = []
    for word in words:
        comb.extend(change_word(word))

    # generate combinations with the provided words
    for r in range(2, len(words) + 1):
        for c in itertools.permutations(words, r):
            comb.append(''.join(c))

    # remove duplicates
    comb = list(set(comb))

    # create the wl_gen.txt file
    with open("wl_gen.txt", "w") as file:
        for item in comb:
            file.write(f"{item}\n")

    print(f"Wordlist created with {len(comb)} combinations and saved as wl_gen.txt")
    return comb

def main():
    words = []

    while True:
        word = input("Insert a word (or 'exit' to generate the wordlist): ")
        if word.lower() == 'exit':
            print("Generating wordlist, this may take a while...\n")
            break
        words.append(word)

    wordlist(words)

if __name__ == "__main__":
    print("WLGen v1.0")
    print("Author: ZeroCypher")
    print("Use it only with previous authorization."
          "\nMisuse of this tool is entirely your responsibility.\n"
          )
    main()