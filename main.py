from spellchecker import SpellChecker
corrector = SpellChecker()

word = str(input("Enter a Word : "))
if word in corrector:
    print("Correct")
else:
    correct_word = corrector.correction(word)
    print("Correct Spelling is ", correct_word)
