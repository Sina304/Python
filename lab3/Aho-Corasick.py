class TrieNode:
    def __init__(self):
        self.children = {}      #dzieci czyli kolejne litery
        self.failure = None     #wskaźnik na skrót
        self.output = []        #lista słów ???
        self.is_end = False     #czy to jest koniec slowa

class AhoCorasick:              #Główna klasa
    def __init__(self):         
        self.root = TrieNode()  #Korzeń drzewa (punkt startowy)
        self.patterns = []      #Lista wszystkich słów, które dodaliśmy

    def add_pattern(self, pattern): 
        #Dodawanie słowa do drzewa
        node = self.root                #Korzeń
        self.patterns.append(pattern)   #Zapisanie drzewa  
        
        for char in pattern:            #przechodzenie przez kazda litere
            if char not in node.children:   #jezeli nie ma jeszcze takiej litery,
                node.children[char] = TrieNode()    #to ja tworzymy
            node = node.children[char]
        
        node.is_end = True                  #ostatnia litera to koniec słowa
        node.output.append(pattern)         #no i dodajemy słowo
    
    def build_failure_links(self):
        from collections import deque
        queue = deque()                 #Kolejka typu FIFO
        
        for child in self.root.children.values():
            child.failure = self.root
            queue.append(child)
        
        while queue:
            #Wyciąga do current_node pierwszy item i wrzuca na koniec kolejki jego dzieci
            current_node = queue.popleft()  
            
            for char, child_node in current_node.children.items():
                queue.append(child_node)
                failure_node = current_node.failure
                
                while failure_node is not None and char not in failure_node.children:
                    failure_node = failure_node.failure
                
                if failure_node is None:
                    child_node.failure = self.root
                else:
                    child_node.failure = failure_node.children[char]
                
                child_node.output.extend(child_node.failure.output)
    
    def search(self, text):
        result = {}
        current_node = self.root
        
        for i, char in enumerate(text):
            while current_node != self.root and char not in current_node.children:
                current_node = current_node.failure
            
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                current_node = self.root
            
            for pattern in current_node.output:
                start_index = i - len(pattern) + 1
                if pattern not in result:
                    result[pattern] = []
                result[pattern].append(start_index)
        
        return result

# PRZYKŁAD UŻYCIA - krok po kroku
print("=== PRZYKŁAD ===")

# 1. Tworzymy wyszukiwarkę
print("1. Tworzymy wyszukiwarkę Aho-Corasick")
ac = AhoCorasick()

# 2. Dodajemy słowa do wyszukania
print("2. Dodajemy słowa:")
words = ["ów"]
for word in words:
    ac.add_pattern(word)

# 3. Budujemy skróty
print("3. Budujemy skróty między słowami")
ac.build_failure_links()

# 4. Szukamy w tekście
print("4. Szukamy w tekście: 'ushers'")
text = "ów stado krów"
results = ac.search(text)

# 5. Pokazujemy wyniki
print("5. WYNIKI:")
for word, positions in results.items():
    for pos in positions:
        found = text[pos:pos+len(word)]
        print(f"   Znaleziono '{word}' na pozycji {pos}: '{found}'")

