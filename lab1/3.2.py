import re

def remove_words_re(text, words_to_remove):
    pattern = r'\b(' + '|'.join(words_to_remove) + r')\b'
    text = re.sub(pattern, '', text)
    return text

text = "Jade bardzo daleko i nie wiem co to bedzie oj oj oj"
words_to_remove = ['i', 'co', 'oj'] 

print("Wynik:", remove_words_re(text, words_to_remove))