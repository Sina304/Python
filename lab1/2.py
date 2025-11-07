import os

def list_files_recursive(start_path, level=0):
    """Rekurencyjnie wypisuje wszystkie pliki od katalogu start_path."""
    
    try:
        for item in os.listdir(start_path):
            item_path = os.path.join(start_path, item)
            
            if os.path.isfile(item_path):
                # Jeśli to plik - wypisz
                print("    " * level + item)  # POPRAWIONE: usunięte { } i f
            elif os.path.isdir(item_path):
                # Jeśli to katalog - rekurencyjne zejście głębiej
                print("    " * level + item)  # DODANE: wcięcie też dla katalogów
                list_files_recursive(item_path, level+1)
    
    except FileNotFoundError:
        return "Błąd: Katalog nie istnieje"
    except PermissionError:
        return "Błąd: Brak uprawnień"

list_files_recursive('.')  # Przykład dla bieżącego katalogu