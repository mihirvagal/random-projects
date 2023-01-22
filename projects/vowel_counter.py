def detect_vowel():
    """
    Takes variable `sentence` and return the number of vowels.
    """
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for i in sentence:
        if i.lower() in vowels:
            count += 1
    print(count)


sentence = str(input("Enter a sentence: "))
detect_vowel()
