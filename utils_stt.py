from funasr import AutoModel
from funasr.utils.postprocess_utils import rich_transcription_postprocess
import keyboard
import wave
import pyaudio
import torch
device = "cuda" if torch.cuda.is_available() else "cpu"

audio = pyaudio.PyAudio()

# Configuration parameters
FORMAT = pyaudio.paInt16  # 16-bit resolution
CHANNELS = 1  # Mono channel
CHUNK = 1024  # Number of samples per chunk
OUTPUT_FILENAME = "output.wav"  # Output file name
supported_sample_rates = [8000, 16000, 32000, 44100, 48000]
supported_rate=44100

# Initialize the model
model = "iic/SenseVoiceSmall"
model = AutoModel(
    model=model,
    vad_model="./iic/speech_fsmn_vad_zh-cn-16k-common-pytorch",
    vad_kwargs={"max_single_segment_time": 30000},
    trust_remote_code=True,
    disable_log=True
)

def start_recording(input_device_index,supported_rate):
    global frames
    frames = []

    try:
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=supported_rate, input=True,
                            frames_per_buffer=CHUNK, input_device_index=input_device_index)
        print("Recording started... Press '2' to stop recording.")
    
        while True:
            if keyboard.is_pressed('2'):
                print("Recording stopped.")
                break
            data = stream.read(CHUNK)
            frames.append(data)

        stream.stop_stream()
        stream.close()

    except Exception as e:
        print(f"An error occurred during recording: {e}")


def save_recording():
    try:
        waveFile = wave.open(OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(supported_rate)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()
        print(f"Recording saved as {OUTPUT_FILENAME}")
    except Exception as e:
        print(f"An error occurred while saving the recording: {e}")

def stt_func():
        try:
            res = model.generate(
                input=f"./{OUTPUT_FILENAME}",
                cache={},
                language="auto",  # "zh", "en", "yue", "ja", "ko", "nospeech"
                use_itn=True,
                batch_size_s=60,
                merge_vad=True,
                merge_length_s=15,
            )
            text = rich_transcription_postprocess(res[0]["text"])
            print(f"Speech-to-Text Result:\n{text}")
            return text
        except Exception as e:
            print(f"An error occurred while saving the recording: {e}")

