import pandas as pd

def find_sequential_matching_dates(new_data_file, known_database_file, tolerance=0.005):
    # Load the data from your newly created file
    sampled_data = pd.read_csv(new_data_file, header=None, names=['ENF'], dtype={'ENF': float})
    
    # Load the data from the known database, skipping rows with non-numeric values in 'ENF'
    try:
        known_database = pd.read_csv(known_database_file, skiprows=1, names=['Timestamp', 'ENF'], dtype={'ENF': float})
    except ValueError:
        print("Error: Non-numeric values found in 'ENF' column of the known database.")
        return []

    matching_dates = []

    # Iterate through each entry in your dataset
    for i in range(len(known_database) - len(sampled_data) + 1):
        current_match = []  # Store the current sequence of matching dates

        # Compare it with each entry in the known database
        for j in range(len(sampled_data)):
            new_data_value = sampled_data.loc[j, 'ENF']
            known_data_value = known_database.loc[i + j, 'ENF']

            # Check if the values match within the specified tolerance
            if abs(new_data_value - known_data_value) <= tolerance:
                current_match.append(known_database.loc[i + j, 'Timestamp'])
            else:
                current_match = []  # Reset the current match if a mismatch is found
                break  # Break out of the inner loop once a match is not found

        # Check if the current match is a complete sequence
        if len(current_match) == len(sampled_data):
            matching_dates.extend(current_match)
            break  # Break out of the outer loop once a match is found

    return matching_dates

# Example usage
new_data_file = 'C:\\Users\\benco\\Documents\\pyScripts\\ENFAnalaysis\\_sampled_50Hz_data.txt'
known_database_file = 'C:\\Users\\benco\\Documents\\pyScripts\\ENFAnalaysis\\knowndata.csv'
matching_dates = find_sequential_matching_dates(new_data_file, known_database_file)

# Display the matching dates
print("Matching Dates:")
for date in matching_dates:
    print(date)
