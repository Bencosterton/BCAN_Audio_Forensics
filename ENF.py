import sys
import os
import librosa
import numpy as np
import pandas as pd
import csv

def sample_and_save_50Hz_data(audio_file_path, output_csv_file_path):
    # Load the file and work out what it is (sample rate and length etc.)
    y, sr = librosa.load(audio_file_path, sr=None)
    samples_per_second = int(sr / 50) 
    num_seconds = int(len(y) / sr)
    sampled_data = np.zeros(num_seconds)

    # Calculate the 50Hz variation for each second in the audio file starting at 0
    for i in range(num_seconds):
        start_sample = i * samples_per_second
        end_sample = (i + 1) * samples_per_second
        sampled_data[i] = np.mean(y[start_sample:end_sample])

    time_values = np.arange(0, num_seconds)
    absolute_values = np.full_like(sampled_data, 50.0) + sampled_data
    formatted_absolute_values = np.round(absolute_values, 3)  # Format the frequency values to 3 decimal places
    data_to_save = np.column_stack((time_values, formatted_absolute_values))

    # Put all the collected data in a CSV file
    with open(output_csv_file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['t', 'f'])
        csvwriter.writerows(data_to_save)

def add_difference_column(input_file_path, output_file_path):
    # Read the above csv file and make a 'd' column for difference data between 'f' data
    df = pd.read_csv(input_file_path, dtype={'f': float})
    df['d'] = df['f'].diff()
    df['d'] = df['d'].apply(lambda x: f"{'' if pd.isna(x) else '+' if x >= 0 else ''}{x:.3f}")
    df.to_csv(output_file_path, index=False)

if __name__ == "__main__":
    # find the audio file specified in the command argument
    if len(sys.argv) != 2:
        print("Usage: ENF.py <audio_file_path>")
        sys.exit(1)

    audio_file_path = sys.argv[1]

    # Go get the file! fetch!
    if not os.path.exists(audio_file_path):
        print(f"Error: The file '{audio_file_path}' does not exist.")
        sys.exit(1)

    # make the new csv file with the difference data
    output_diff_csv_file_path = os.path.splitext(audio_file_path)[0] + '.csv'
    intermediate_output_csv_file_path = os.path.splitext(audio_file_path)[0] + '_output.csv'
    sample_and_save_50Hz_data(audio_file_path, intermediate_output_csv_file_path)
    add_difference_column(intermediate_output_csv_file_path, output_diff_csv_file_path)

    # delete the output file without the diff 'd' data.
    os.remove(intermediate_output_csv_file_path)

    # Some info for you, after all is done.
    print(f"ENF data saved to '{output_diff_csv_file_path}'.")
