import os


def merge_files(input_folder, output_file):
    files_info = []

    # Считываем информацию о файлах
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            file_path = os.path.join(input_folder, filename)
            print(f"Чтение файла: {file_path}")  # Отладочное сообщение
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                line_count = len(lines)
                files_info.append((filename, line_count, lines))
                print(f"Добавлен файл: {filename}, строк: {line_count}")  # Отладочное сообщение

    # Сортируем файлы по количеству строк
    files_info.sort(key=lambda x: x[1])

    # Записываем в результирующий файл
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for filename, line_count, lines in files_info:
            out_file.write(f"{filename}\n{line_count}\n")  # Записываем служебную информацию
            out_file.writelines(lines)  # Записываем содержимое файла


# Укажите путь к папке с файлами и имя выходного файла
input_folder = r'C:\Users\hp\Desktop\3'  # Используем сырую строку
output_file = r'C:\Users\hp\Desktop\3\merged_output.txt'  # Путь к выходному файлу

merge_files(input_folder, output_file)

