import os

file_path = 'file_to_delete.txt'

try:
    os.remove(file_path)
    print(f"Файл '{file_path}' успешно удален.")
except FileNotFoundError:
    print(f"Файл '{file_path}' не найден.")
except PermissionError:
    print(f"Недостаточно прав для удаления файла '{file_path}'.")
except Exception as e:
    print(f"Произошла ошибка при удалении файла: {e}")