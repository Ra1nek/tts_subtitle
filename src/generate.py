# scripts/generate.py
from TTS.utils.speaker import SpeakerManager

def generate_embedding(audio_path, model_path, output_path):
    speaker_manager = SpeakerManager(encoder_model_path=model_path)
    embedding = speaker_manager.compute_embedding_from_file(audio_path)
    with open(output_path, 'wb') as f:
        f.write(embedding)

if __name__ == "__main__":
    audio_path = "path/to/speaker_sample.wav"
    model_path = "models/speaker_encoder.pth"
    output_path = "models/speaker_embedding.pkl"
    generate_embedding(audio_path, model_path, output_path)
