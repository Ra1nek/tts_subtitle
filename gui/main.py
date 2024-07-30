import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess
import sys

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
        self.data_dir_entry.delete(0, tk.END)
        self.data_dir_entry.insert(0, data_dir)

    def preprocess_data(self):
        data_dir = self.data_dir_entry.get()
        if data_dir:
            script_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'preprocess.py')
            result = subprocess.run([sys.executable, script_path, data_dir], capture_output=True, text=True)
            if result.returncode == 0:
                messagebox.showinfo("Информация", "Предварительная обработка данных завершена")
            else:
                messagebox.showerror("Ошибка", f"Ошибка при предварительной обработке данных:\n{result.stderr}")
        else:
            messagebox.showwarning("Предупреждение", "Пожалуйста, выберите директорию с данными")

    def train_model(self):
        script_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'train.py')
        result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
        if result.returncode == 0:
            messagebox.showinfo("Информация", "Обучение модели завершено")
        else:
            messagebox.showerror("Ошибка", f"Ошибка при обучении модели:\n{result.stderr}")

    def generate_embedding(self):
        audio_path = filedialog.askopenfilename(title="Выберите образец голоса", filetypes=[("WAV файлы", "*.wav")])
        if audio_path:
            script_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'generate.py')
            result = subprocess.run([sys.executable, script_path, audio_path], capture_output=True, text=True)
            if result.returncode == 0:
                messagebox.showinfo("Информация", "Векторное представление голоса сгенерировано")
            else:
                messagebox.showerror("Ошибка", f"Ошибка при генерации векторного представления:\n{result.stderr}")
        else:
            messagebox.showwarning("Предупреждение", "Пожалуйста, выберите аудиофайл")

    def synthesize_speech(self):
        srt_path = filedialog.askopenfilename(title="Выберите файл субтитров", filetypes=[("SRT файлы", "*.srt")])
        if srt_path:
            script_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'synthesize.py')
            result = subprocess.run([sys.executable, script_path, srt_path], capture_output=True, text=True)
            if result.returncode == 0:
                messagebox.showinfo("Информация", "Синтез речи завершен")
            else:
                messagebox.showerror("Ошибка", f"Ошибка при синтезе речи:\n{result.stderr}")
        else:
            messagebox.showwarning("Предупреждение", "Пожалуйста, выберите файл субтитров")

if __name__ == "__main__":
    root = tk.Tk()
    app = TTSApp(root)
    root.mainloop()
