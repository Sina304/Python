def remove_words(text, words_to_remove):
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in words_to_remove]
    

    return ' '.join(filtered_words)

# Przykład użycia
text = "Jade bardzo daleko i nie wiem co to bedzie oj oj oj"
words_to_remove = ['i', 'co', 'oj']
print(remove_words(text, words_to_remove))