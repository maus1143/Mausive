import os
import re
import sys

def print_progress_bar(iteration, total, length=50):
    progress = (iteration / total) * 100
    bar = '█' * int((progress / 100) * length) + '-' * (length - int((progress / 100) * length))
    sys.stdout.write(f"\r[{bar}] {progress:.2f}%")
    sys.stdout.flush()

def search_archive(base_path, search_terms):
    results = {term: [] for term in search_terms}

    all_files = []
    total_files = 0

    for root, dirs, files in os.walk(base_path):
        all_files.extend([os.path.join(root, file) for file in files])
        total_files += len(files)

    for i, file_path in enumerate(all_files):
        print_progress_bar(i + 1, total_files)

        for term in search_terms:
            search_pattern = re.compile(r'\b' + re.escape(term) + r'\b', re.IGNORECASE)

            if search_pattern.search(os.path.basename(file_path)):
                results[term].append((file_path, 'Dateiname'))

            if file_path.endswith('.txt'):
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        lines = file.readlines()
                        if len(lines) > 1 and search_pattern.search(lines[1]):
                            results[term].append((file_path, 'Überschrift'))
                except Exception as e:
                    print(f"\nFehler beim Lesen der Datei {file_path}: {e}")

    return results

search_term_input = input("Gib einen Suchbegriff ein (Ordnername, Dateiname oder Überschrift), getrennt durch Kommas: ")

search_terms = [term.strip() for term in search_term_input.split(',')]

base_path = "Mausive-The_Libary"

matches = search_archive(base_path, search_terms)

print("\nFertig. Ergebnisse:\n")

for term in search_terms:
    print(f"Ergebnisse für '{term}':")
    if matches[term]:
        for match in matches[term]:
            file_path, match_type = match
            print(f"{file_path} - {match_type}")
    else:
        print("Keine Treffer gefunden.")
    print()  