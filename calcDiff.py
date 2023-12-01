import pandas as pd

def add_difference_column(input_file_path, output_file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file_path, dtype={'f': float})

    # Calculate the difference and add it as a new column
    df['d'] = df['f'].diff()

    # Format the 'd' column to include a sign and fill NaN with 0
    df['d'] = df['d'].apply(lambda x: f"{'' if pd.isna(x) else '+' if x >= 0 else ''}{x:.3f}")

    # Save the updated DataFrame to a new CSV file
    df.to_csv(output_file_path, index=False)

# Example usage:
input_file_path = '231010_1022.csv'
output_file_path = '231010_1022_diff.csv'
add_difference_column(input_file_path, output_file_path)
