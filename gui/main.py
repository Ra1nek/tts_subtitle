# gui/main.py
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess

class TTSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Приложение TTS")

        self.create_widgets()

    def create_widgets(self):
        # Путь к директории с данными
        self.data_dir_label = tk.Label(self.root, text="Директория с данными:")
        self.data_dir_label.grid(row=0, column=0, padx=10, pady=10)
        self.data_dir_entry = tk.Entry(self.root, width=50)
        self.data_dir_entry.grid(row=0, column=1, padx=10, pady=10)
        self.data_dir_button = tk.Button(self.root, text="Обзор", command=self.browse_data_dir)
        self.data_dir_button.grid(row=0, column=2, padx=10, pady=10)

        # Кнопка для предварительной обработки данных
        self.preprocess_button = tk.Button(self.root, text="Предварительная обработка данных", command=self.preprocess_data)
        self.preprocess_button.grid(row=1, column=1, padx=10, pady=10)

        # Кнопка для обучения модели
        self.train_button = tk.Button(self.root, text="Обучение модели", command=self.train_model)
        self.train_button.grid(row=2, column=1, padx=10, pady=10)

        # Кнопка для генерации embedding
        self.generate_button = tk.Button(self.root, text="Генерация векторного представления", command=self.generate_embedding)
        self.generate_button.grid(row=3, column=1, padx=10, pady=10)

        # Кнопка для синтеза речи
        self.synthesize_button = tk.Button(self.root, text="Синтез речи", command=self.synthesize_speech)
        self.synthesize_button.grid(row=4, column=1, padx=10, pady=10)

    def browse_data_dir(self):
        data_dir = filedialog.askdirectory()
        self.data_dir_entry.insert(0, data_dir)

    def preprocess_data(self):
        data_dir = self.data_dir_entry.get()
        if data_dir:
            subprocess.run(["python", "scripts/preprocess.py", data_dir])
            messagebox.showinfo("Информация", "Предварительная обработка данных завершена")
        else:
            messagebox.showwarning("Предупреждение", "Пожалуйста, выберите директорию с данными")

    def train_model(self):
        subprocess.run(["python", "scripts/train.py"])
        messagebox.showinfo("Информация", "Обучение модели завершено")

    def generate_embedding(self):
        audio_path = filedialog.askopenfilename(title="Выберите образец голоса", filetypes=[("WAV файлы", "*.wav")])
        if audio_path:
            subprocess.run(["python", "scripts/generate.py", audio_path])
            messagebox.showinfo("Информация", "Векторное представление голоса сгенерировано")
        else:
            messagebox.showwarning("Предупреждение", "Пожалуйста, выберите аудиофайл")

    def synthesize_speech(self):
        srt_path = filedialog.askopenfilename(title="Выберите файл субтитров", filetypes=[("SRT файлы", "*.srt")])
        if srt_path:
            subprocess.run(["python", "scripts/synthesize.py", srt_path])
            messagebox.showinfo("Информация", "Синтез речи завершен")
        else:
            messagebox.showwarning("Предупреждение", "Пожалуйста, выберите файл субтитров")

if __name__ == "__main__":
    root = tk.Tk()
    app = TTSApp(root)
    root.mainloop()
