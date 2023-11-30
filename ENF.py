import librosa
import numpy as np
import csv

def sample_and_save_50Hz_data(audio_file_path, output_csv_file_path):
    # load the file and work out what it is (sample rate and length etc.)
    y, sr = librosa.load(audio_file_path, sr=None)
    samples_per_second = int(sr / 50) 
    num_seconds = int(len(y) / sr)
    sampled_data = np.zeros(num_seconds)

    # Calclate the 50Hz variation for each second in the audio file starting at 0
    for i in range(num_seconds):
        start_sample = i * samples_per_second
        end_sample = (i + 1) * samples_per_second
        sampled_data[i] = np.mean(y[start_sample:end_sample])

    time_values = np.arange(0, num_seconds)
    absolute_values = np.full_like(sampled_data, 50.0) + sampled_data
    formatted_absolute_values = np.round(absolute_values, 3) # format the fruency values to 3 decimal placs
    data_to_save = np.column_stack((time_values, formatted_absolute_values))

    # Put all the collected data in a csv file
    with open(output_csv_file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['t', 'f'])
        csvwriter.writerows(data_to_save)

audio_file_path = 'C:\\Users\\benco\\Documents\\pyScripts\\ENFAnalaysis\\input_file.wav'
sampled_50Hz_data_csv_file_path = 'C:\\Users\\benco\\Documents\\pyScripts\\ENFAnalaysis\\output_file.csv'

sample_and_save_50Hz_data(audio_file_path, sampled_50Hz_data_csv_file_path)
