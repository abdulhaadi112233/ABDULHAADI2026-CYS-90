sentence = input("Enter a sentence: ").lower()
vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for ch in sentence:
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print(f"Vowels = {vowel_count}")
print(f"Consonants = {consonant_count}")