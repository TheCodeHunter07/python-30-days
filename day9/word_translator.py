

# Stretch: word_translator.py — a small English-to-Hindi or Marathi dictionary that translates word by word.


translations = {
    "hello": "नमस्कार",
    "water": "पाणी",
    "food": "जेवण",
    "friend": "मित्र",
    "book": "पुस्तक"
}

word = input("Enter an English word: ")

word = word.lower()

if word in translations:
    print(f"Marathi translation: {translations[word]}")
else:
    print("Translation not available")