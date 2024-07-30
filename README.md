tts_subtitle/
│
├── gui/
│   ├── main.py                # Основной GUI-скрипт
│   ├── utils.py               # Вспомогательные функции для GUI (пока пустой)
│   └── assets/
│       └── logo.png           # Логотип или другие ресурсы для GUI (если есть)
│
├── src/
│   ├── generate.py            # Скрипт для генерации векторного представления голоса
│   ├── preprocess.py          # Скрипт для предварительной обработки данных
│   ├── synthesize.py          # Скрипт для синтеза речи
│   ├── train.py               # Скрипт для обучения модели
│   ├── utils.py               # Вспомогательные функции (пока пустой)
│   └── voice_embedding.py     # Работа с векторными представлениями голоса (пока пустой)
│
├── config/
│   └── config.json            # Конфигурационный файл модели
│
├── data/
│   ├── metadata.csv           # Метаданные для аудиофайлов
│   └── audio/                 # Папка с аудиофайлами
│
├── models/
│   ├── speaker_encoder.pth    # Модель для генерации embedding
│   └── speaker_embedding.pkl  # Сохранённые векторные представления
│
├── requirements.txt           # Зависимости проекта
├── README.md                  # Документация проекта
└── .gitignore                  # Игнорируемые файлы для git
