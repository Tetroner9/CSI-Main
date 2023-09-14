import pyaudio
import wave

# Initialize PyAudio
p = pyaudio.PyAudio()

# Check available audio devices
for i in range(p.get_device_count()):
    print(p.get_device_info_by_index(i))

# Set the output device to your Bluetooth device (replace with the index of your Bluetooth device)
output_device_index = 3  # Replace with the index of your Bluetooth device
stream = p.open(output_device_index=output_device_index, format=pyaudio.paInt16, channels=2, rate=44100, output=True)

# Read audio data from a WAV file (replace 'audio.wav' with your file)
file_path = 'stathicc.wav'  # Replace with the path to your audio file

try:
    with wave.open(file_path, 'rb') as audio_file:
        audio_data = audio_file.readframes(audio_file.getnframes())

    # Play audio
    stream.write(audio_data)

    # Close the stream and PyAudio when done
    stream.stop_stream()
    stream.close()
    p.terminate()

except Exception as e:
    print(f"An error occurred: {str(e)}")
