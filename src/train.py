import sys
from TTS.bin.train import main as tts_train

def train_model(config_path):
    tts_train(config_path=config_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python train.py <config_path>")
        sys.exit(1)
    config_path = sys.argv[1]
    train_model(config_path)
