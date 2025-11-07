import re

def replace_words_re(text, replacements):
    pattern = r'\b(' + '|'.join(replacements.keys()) + r')\b'
    return re.sub(pattern,lambda match: replacements[match.group()],text)
    

# PRZYKŁAD UŻYCIA
text = "jade jade bardzo daleko moim samochodem"
replacements = {'jade': 'pedze', 'samochodem': 'supercarem'}

print("Wynik:", replace_words_re(text, replacements))