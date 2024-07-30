# scripts/train.py
import os
from TTS.bin.train import main as tts_train

def train_model(config_path):
    tts_train(config_path=config_path)

if __name__ == "__main__":
    config_path = "config/config.json"
    train_model(config_path)
