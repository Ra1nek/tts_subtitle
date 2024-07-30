# scripts/preprocess.py
import os
import librosa
import soundfile as sf
import pandas as pd

def preprocess_audio(data_dir, output_sr=22050):
    wav_dir = os.path.join(data_dir, 'wavs')
    metadata_path = os.path.join(data_dir, 'metadata.csv')
    metadata = []

    for filename in os.listdir(wav_dir):
        if filename.endswith('.wav'):
            filepath = os.path.join(wav_dir, filename)
            y, sr = librosa.load(filepath, sr=output_sr)
            output_path = filepath.replace('.wav', '_resampled.wav')
            sf.write(output_path, y, output_sr)
            os.remove(filepath)
            os.rename(output_path, filepath)
            text = input(f'Enter text for {filename}: ')
            metadata.append([filename, text])

    df = pd.DataFrame(metadata, columns=['filename', 'text'])
    df.to_csv(metadata_path, index=False)

if __name__ == "__main__":
    data_dir = input("Enter path to data directory: ")
    preprocess_audio(data_dir)