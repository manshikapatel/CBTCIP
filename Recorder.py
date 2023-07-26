import pyaudio
import wave

def record_audio(file_name,duration,sample_rate=44100,chunk_size=1024,channels=2):
    audio_format = pyaudio.paInt16
    audio_frames =[]

    audio = pyaudio.PyAudio()

    stream = audio.open(format=audio_format, channels=channels, rate=sample_rate,input=True,frames_per_buffer=chunk_size)

    print("Recording...")

    for _ in range(int(sample_rate / chunk_size *duration)):
        data = stream.read(chunk_size)
        audio_frames.append(data)

    print("Recording finished.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    save_audio(file_name,audio_frames,sample_rate)

def save_audio(file_name,audio_frames,sample_rate):
    wave_file = wave.open(file_name,'wb')
    wave_file.setnchannels(2)
    wave_file.setsampwidth(2)
    wave_file.setframerate(sample_rate)
    wave_file.writeframes(b''.join(audio_frames))
    wave_file.close()

if __name__ =="__main__":
    file_name = "recorded_audio.wav"
    duration= 5

    record_audio(file_name,duration)