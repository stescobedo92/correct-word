from autocorrect import Speller

corrector = Speller(lang='en')


def check_word(word):
    if not corrector(word) == word:
        return corrector(word)
    else:
        return word


print(check_word("I likke the excersise"))
