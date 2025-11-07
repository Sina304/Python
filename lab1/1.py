import os     #operative_system

def count_files(directory="."):   
    """Zlicza ilość plików w podanym katalogu (domyślnie bieżący)."""
    try:
        # Pobierz wszystkie elementy w katalogu
        items = os.listdir(directory)
        
        # Policz tylko pliki
        file_count = 0
        for item in items:
            if os.path.isfile(os.path.join(directory, item)):    #czy plik ->  funkcja tworzenia sciezki (sciezka,plik)
                file_count += 1
                
        return file_count
        
    except FileNotFoundError:
        return "Błąd: Katalog nie istnieje"
    except PermissionError:
        return "Błąd: Brak uprawnień"

# Użycie - najprościej:
print("Plików w bieżącym katalogu:", count_files())

# Albo sprawdź inny katalog:
print("Plików w C:\\Windows:", count_files("C:\\Windows"))