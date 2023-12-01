import pandas as pd
import numpy as np

def find_sequential_matching_dates(new_data_file, known_database_file, correlation_threshold=0.1, tolerance=0.003):
    sampled_data = pd.read_csv(new_data_file, header=0, dtype={'f': float, 'd': float})
    sampled_data['d'] = sampled_data['d'].replace(np.nan, 0.0)
    
    try:
        known_database = pd.read_csv(known_database_file, dtype={'f': float, 'd': float})
        known_database['d'] = known_database['d'].replace(np.nan, 0.0)
    except ValueError:
        print("Error: Non-numeric values found in 'ENF' column of the known database.")
        return []

    matching_dates = []
    
    for i in range(len(known_database) - len(sampled_data) + 1):
        current_match = [] 

        for j in range(len(sampled_data)):
            new_data_value = sampled_data.loc[j, 'd']
            known_data_value = known_database.loc[i + j, 'd']

            if abs(new_data_value - known_data_value) <= tolerance:
                current_match.append(known_database.loc[i + j, 'dtm'])
            else:
                current_match = []  
                break 

        if len(current_match) / len(sampled_data) >= correlation_threshold:
            matching_dates.extend(current_match)
            break 

    return matching_dates

new_data_file = 'C:\\Users\\benco\\Documents\\pyScripts\\ENFAnalaysis\\sample_database.csv'
known_database_file = 'C:\\Users\\benco\\Documents\\pyScripts\\ENFAnalaysis\\known_database.csv'
matching_dates = find_sequential_matching_dates(new_data_file, known_database_file)

if matching_dates:
    first_result = matching_dates[0]
    last_result = matching_dates[-1]
    print(f"Recording began at {first_result} and ended {last_result}")
else:
    print("No matching dates found.")
