import sys
from voice_embedding import load_embedding

def synthesize_speech(srt_path, embedding_path):
    # Загрузите векторное представление
    embedding = load_embedding(embedding_path)
    # Реализуйте процесс синтеза речи, используя embedding
    print(f"Synthesizing speech using embedding from {embedding_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python synthesize.py <srt_path> <embedding_path>")
        sys.exit(1)
    srt_path = sys.argv[1]
    embedding_path = sys.argv[2]
    synthesize_speech(srt_path, embedding_path)
