import pandas as pd

def find_sequential_matching_dates(new_data_file, known_database_file, tolerance=0.005):
    sampled_data = pd.read_csv(new_data_file, header=None, names=['ENF'], dtype={'ENF': float})
    
    try:
        known_database = pd.read_csv(known_database_file, skiprows=1, names=['Timestamp', 'ENF'], dtype={'ENF': float})
    except ValueError:
        print("Error: Non-numeric values found in 'ENF' column of the known database.")
        return []

    matching_dates = []
    
    for i in range(len(known_database) - len(sampled_data) + 1):
        current_match = [] 

        for j in range(len(sampled_data)):
            new_data_value = sampled_data.loc[j, 'ENF']
            known_data_value = known_database.loc[i + j, 'ENF']

            if abs(new_data_value - known_data_value) <= tolerance:
                current_match.append(known_database.loc[i + j, 'Timestamp'])
            else:
                current_match = []  
                break 

        if len(current_match) == len(sampled_data):
            matching_dates.extend(current_match)
            break 

    return matching_dates

new_data_file = 'C:\\Users\\benco\\Documents\\pyScripts\\ENFAnalaysis\\_sampled_50Hz_data.txt'
known_database_file = 'C:\\Users\\benco\\Documents\\pyScripts\\ENFAnalaysis\\knowndata.csv'
matching_dates = find_sequential_matching_dates(new_data_file, known_database_file)

print("Matching Dates:")
for date in matching_dates:
    print(date)
