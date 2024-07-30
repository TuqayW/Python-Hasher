# Custom Alphabet Hashing
Overview
The Custom Alphabet Hashing project provides a unique hashing algorithm that uses a dynamically generated alphabet based on an input word and a key to mix this alphabet. This method creates a custom hash of another word. While it's a fascinating exercise in algorithm design, please note that this hashing technique is not suitable for cryptographic applications. For secure hashing, consider using established cryptographic algorithms like SHA-256.

Features
Dynamic Alphabet Creation: Generates a custom alphabet from an input word.
Custom Hashing Mechanism: Uses a key to rotate and mix the alphabet for hashing an input word.
How It Works
Create Alphabet:

Function: create_alphabet(word)
Description: This function generates a custom alphabet list based on the characters in the input word. It starts with the letters from the input word and adds any missing letters of the alphabet to complete the custom set.
Clean Word:

### Function: clean_word(word)
Description: This function preprocesses the input by removing spaces and converting numeric characters to corresponding alphabet letters. This step ensures that the input is in the correct format for hashing.
Letter Positions:

### Function: letter_positions(word)
Description: Converts each letter of the input word to its position in the alphabet (e.g., 'a' = 1, 'b' = 2). This helps in mapping letters to their positions for hashing.
Mix Alphabet:

### Function: mix_alphabet(key, word, alphabet)
Description: Uses the provided key to determine the rotation and mixing of the custom alphabet. The key's letter positions influence how the alphabet is rotated to produce the final hash of the input word.

### How to Use
Create Alphabet: Enter an initial word to generate a custom alphabet.
Enter Key: Provide a key that will influence how the alphabet is mixed and rotated.
Hash Input: Input the word you want to hash. The algorithm will use the custom alphabet and key to produce a hashed result.
View Result: The hashed word will be displayed as output.
Example Workflow
Generating Alphabet: Input a word to initialize the custom alphabet.
Provide Key: Enter a key for hashing.
Input Word: Enter the word you wish to hash.
Get Hashed Output: The system will display the hashed result based on the custom alphabet and key.
### Installation
  To use this hashing algorithm, clone the repository and execute the script. Ensure you have Python installed.


`git clone https://github.com/yourusername/custom-alphabet-hashing.git`

`cd custom-alphabet-hashing`

`python hashing_script.py`

### Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to enhance the hashing algorithm or add new features.

### License
This project is licensed under the MIT License. For more details, see the LICENSE file.
