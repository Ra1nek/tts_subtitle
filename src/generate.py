import sys
from TTS.utils.speaker import SpeakerManager
from voice_embedding import save_embedding

def generate_embedding(audio_path, model_path, output_path):
    speaker_manager = SpeakerManager(encoder_model_path=model_path)
    embedding = speaker_manager.compute_embedding_from_file(audio_path)
    save_embedding(embedding, output_path)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python generate.py <audio_path> <model_path> <output_path>")
        sys.exit(1)
    audio_path = sys.argv[1]
    model_path = sys.argv[2]
    output_path = sys.argv[3]
    generate_embedding(audio_path, model_path, output_path)
