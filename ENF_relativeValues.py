import librosa
import numpy as np
import soundfile as sf

def extract_50Hz_signal(audio_file_path, output_file_path):
    y, sr = librosa.load(audio_file_path, sr=None)

    fifty_hz_signal = y

    sf.write(output_file_path, fifty_hz_signal, sr)

def sample_and_save_50Hz_data(audio_file_path, output_file_path):
    y, sr = librosa.load(audio_file_path, sr=None)

    samples_per_second = int(sr / 50)
    sampled_data = y[::samples_per_second]

    np.savetxt(output_file_path, np.hstack((['50.'], sampled_data)), fmt='%s')

audio_file_path = 'C:\\Users\\benco\\Documents\\pyScripts\\ENFAnalaysis\\231010_1037.wav'
extracted_50Hz_file_path = 'C:\\Users\\benco\\Documents\\pyScripts\\ENFAnalaysis\\extracted_50Hz_signal.wav'
sampled_50Hz_data_file_path = 'C:\\Users\\benco\\Documents\\pyScripts\\ENFAnalaysis\\sampled_50Hz_data.txt'

extract_50Hz_signal(audio_file_path, extracted_50Hz_file_path)

sample_and_save_50Hz_data(extracted_50Hz_file_path, sampled_50Hz_data_file_path)
