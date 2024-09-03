import tkinter as tk
from tkinter import filedialog, Text, messagebox
import csv

def load_csv_file():
    # Открыть диалог выбора файла CSV
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        print(f"Файл выбран: {file_path}")  # Отладочное сообщение
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')  # Используем запятую как разделитель
            content = []
            for row in reader:
                print(f"Чтение строки: {row}")  # Отладочное сообщение
                # Удаляем первую и третью колонки и добавляем префикс к оставшейся колонке
                if len(row) >= 3:
                    modified_value = '994' + row[1]  # Добавляем префикс 994 ко второй колонке
                    content.append([modified_value])  # Добавляем результат в контент
            text_widget.delete(1.0, tk.END)  # Очистить текстовое поле перед вставкой нового текста
            for line in content:
                text_widget.insert(tk.END, line[0] + '\n')  # Вставить обработанное содержимое файла

            if content:
                root.processed_data = content
                print(f"Обработанные данные сохранены: {root.processed_data}")  # Отладочное сообщение
            else:
                print("Обработанные данные пусты.")  # Отладочное сообщение

def save_csv_file():
    if hasattr(root, 'processed_data') and root.processed_data:
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file_path:
            with open(file_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=',')  # Используем запятую как разделитель
                writer.writerows(root.processed_data)  # Записать обработанные данные в новый CSV-файл
            messagebox.showinfo("Успех", "Файл успешно сохранен.")
            print(f"Файл сохранен по пути: {file_path}")  # Отладочное сообщение
    else:
        messagebox.showwarning("Нет данных", "Сначала загрузите и обработайте CSV-файл.")
        print("Сохранение невозможно: нет обработанных данных.")  # Отладочное сообщение

# Создаем главное окно
root = tk.Tk()
root.title("Загрузчик и обработчик CSV-файла")
root.geometry("600x400")

# Инициализируем атрибут для хранения данных
root.processed_data = []

# Создаем текстовый виджет
text_widget = Text(root, wrap='word', width=70, height=20)
text_widget.pack(pady=10)

# Создаем кнопки для загрузки и сохранения
load_button = tk.Button(root, text="Загрузить CSV", command=load_csv_file)
load_button.pack(side=tk.LEFT, padx=20)

save_button = tk.Button(root, text="Сохранить CSV", command=save_csv_file)
save_button.pack(side=tk.LEFT)

# Запускаем главный цикл приложения
root.mainloop()
