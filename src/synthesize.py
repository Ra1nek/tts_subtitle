import sys

def synthesize_speech(srt_path):
    # Реализуйте синтез речи на основе файла субтитров
    pass

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python synthesize.py <srt_path>")
        sys.exit(1)
    srt_path = sys.argv[1]
    synthesize_speech(srt_path)
