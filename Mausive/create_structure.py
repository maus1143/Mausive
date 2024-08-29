import os

def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█'):
    percent = f"{100 * (iteration / float(total)):.{decimals}f}"
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total:
        print()

def create_folders(base_path, themes, categories, sections, directories):
    total_iterations = themes * categories * sections * directories
    iteration = 0

    for theme in range(1, themes + 1):
        theme_path = os.path.join(base_path, f"Theme-{theme}")
        os.makedirs(theme_path, exist_ok=True)

        for category in range(1, categories + 1):
            category_path = os.path.join(theme_path, f"Category-{category}")
            os.makedirs(category_path, exist_ok=True)

            for section in range(1, sections + 1):
                section_path = os.path.join(category_path, f"Section-{section}")
                os.makedirs(section_path, exist_ok=True)

                for directory in range(1, directories + 1):
                    dir_path = os.path.join(section_path, f"Dir-{directory}")
                    os.makedirs(dir_path, exist_ok=True)
                    with open(os.path.join(dir_path, f"file-{directory}.txt"), 'w') as file:
                        file.write(f"Diese Datei befindet sich in: {dir_path}")

                    iteration += 1
                    print_progress_bar(iteration, total_iterations, prefix='Progress', suffix='Mausive wird erstellt', length=50)

base_path = "Mausive-The_Libary"
themes = 10
categories = 10
sections = 10
directories = 20

create_folders(base_path, themes, categories, sections, directories)