# scripts/synthesize.py
import srt
from pydub import AudioSegment
from TTS.utils.synthesizer import Synthesizer

def synthesize_speech(srt_path, model_path, config_path, embedding_path, output_path):
    synthesizer = Synthesizer(model_path, config_path)
    
    with open(embedding_path, 'rb') as f:
        embedding = f.read()
    
    with open(srt_path, 'r', encoding='utf-8') as f:
        subtitles = list(srt.parse(f.read()))

    audio_segments = []

    for subtitle in subtitles:
        wav = synthesizer.tts(subtitle.content, speaker_embedding=embedding)
        audio_segment = AudioSegment(wav.tobytes(), frame_rate=22050, sample_width=2, channels=1)
        
        pause_duration = (subtitle.end - subtitle.start).total_seconds() * 1000
        audio_segment += AudioSegment.silent(duration=pause_duration)
        
        audio_segments.append(audio_segment)

    combined_audio = sum(audio_segments)
    combined_audio.export(output_path, format="mp3")

if __name__ == "__main__":
    srt_path = "path/to/your_subtitle_file.srt"
    model_path = "models/best_model.pth.tar"
    config_path = "config/config.json"
    embedding_path = "models/speaker_embedding.pkl"
    output_path = "output/final_output.mp3"
    synthesize_speech(srt_path, model_path, config_path, embedding_path, output_path)
