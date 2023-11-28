import librosa
import numpy as np
import soundfile as sf

def extract_50Hz_signal(audio_file_path, output_file_path):
    # Load the audio file
    y, sr = librosa.load(audio_file_path, sr=None)

    # Extract the 50Hz signal
    fifty_hz_signal = y

    # Save the extracted 50Hz signal using soundfile
    sf.write(output_file_path, fifty_hz_signal, sr)

def sample_and_save_50Hz_data(audio_file_path, output_file_path):
    # Load the audio file
    y, sr = librosa.load(audio_file_path, sr=None)

    # Sample the 50Hz signal every second
    samples_per_second = int(sr / 50)  # Number of samples in 1 second at 50Hz
    sampled_data = y[::samples_per_second]

    # Convert sampled_data to float array
    sampled_data = np.asarray(sampled_data, dtype=np.float32)

    # Add the base value to the variations in the 50Hz signal
    sampled_data_absolute = np.full_like(sampled_data, 50.0) + sampled_data

    # Save only the absolute values in the 50Hz signal with "50." prefix to a text file
    np.savetxt(output_file_path, sampled_data_absolute, fmt='%.3f')

# Example usage
audio_file_path = 'C:\\Users\\benco\\Documents\\pyScripts\\ENFAnalaysis\\231010_1037.wav'
extracted_50Hz_file_path = 'C:\\Users\\benco\\Documents\\pyScripts\\ENFAnalaysis\\extracted_50Hz_signal.wav'
sampled_50Hz_data_file_path = 'C:\\Users\\benco\\Documents\\pyScripts\\ENFAnalaysis\\sampled_50Hz_data.txt'

# Step 1: Extract 50Hz signal
extract_50Hz_signal(audio_file_path, extracted_50Hz_file_path)

# Step 2: Sample and save 50Hz data without timestamps
sample_and_save_50Hz_data(extracted_50Hz_file_path, sampled_50Hz_data_file_path)

