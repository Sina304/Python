def replace_words(text, replacement_dict):
    words = text.split()
    replaced_words = [replacement_dict.get(word, "nie ma") for word in words]
    return ' '.join(replaced_words)

# Przykład
text = "jade jade bardzo daleko moim samochodem"
replacements = {'jade': 'pedze', 'samochodem': 'supercarem'}
print(replace_words(text, replacements))