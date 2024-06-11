# Part 1
# - Expanding the list columns in the dataset
# - Saving the expanded datasets to CSV files
# - Creating a main dataset without the expanded columns

import pandas as pd 

# Load the datasets
ratings_df = pd.read_csv('C:/Users/sytse/Documents/Maastricht University/Master BISS/4225 Data Visualisation/Infographic/Wine Data/XWines_Slim_150K_ratings.csv')
                        
wines_df = pd.read_csv('C:/Users/sytse/Documents/Maastricht University/Master BISS/4225 Data Visualisation/Infographic/Wine Data/XWines_Slim_1K_wines.csv')

# Create the main dataset without expanding list columns
main_df = wines_df.copy()

# Function to create an expanded dataset with only WineID and the specified column
def create_expanded_dataset(df, column_name):
    expanded_rows = []
    for _, row in df.iterrows():
        items = eval(row[column_name])
        for item in items:
            expanded_rows.append({'WineID': row['WineID'], column_name: item})
    expanded_df = pd.DataFrame(expanded_rows)
    return expanded_df

# Create the expanded datasets
grapes_expanded_df = create_expanded_dataset(wines_df, 'Grapes')
vintages_expanded_df = create_expanded_dataset(wines_df, 'Vintages')
harmonize_expanded_df = create_expanded_dataset(wines_df, 'Harmonize')

main_df = main_df.drop(columns=['Grapes', 'Vintages', 'Harmonize'])

# Save the main and expanded dataframes to CSV files
main_df.to_csv('C:/Users/sytse/Documents/Maastricht University/Master BISS/4225 Data Visualisation/Infographic/Wine Data/100Kmain_dataset.csv', index=False)
grapes_expanded_df.to_csv('C:/Users/sytse/Documents/Maastricht University/Master BISS/4225 Data Visualisation/Infographic/Wine Data/100Kexpanded_grapes_only.csv', index=False)
vintages_expanded_df.to_csv('C:/Users/sytse/Documents/Maastricht University/Master BISS/4225 Data Visualisation/Infographic/Wine Data/100Kexpanded_vintages_only.csv', index=False)
harmonize_expanded_df.to_csv('C:/Users/sytse/Documents/Maastricht University/Master BISS/4225 Data Visualisation/Infographic/Wine Data/100Kexpanded_harmonize_only.csv', index=False)

# Display the first few rows of each dataset
main_df.head()


# Part 2
# - For the Leaderboard Acidity and Body Tooltip, CNTD is used to count the number of unique values in the dataset. 
# - In this way, values are stacked and counted for each wine.

# - Expanding the 'Body' column in the dataset with a sequence of letters (A, B, C, D, E) corresponding to Ordinal Body values (1-5)
# - Expanding the 'Acidity' column in the dataset with a sequence of letters (A, B, C) corresponding to Ordinal Acidity values (1-3)
# - Saving the expanded datasets to CSV files: 'Body_data.csv' and 'Acidity_data.csv'
# - unused letters are saved in a separate dataset to be used in the infographic: 'Unused_Body_data.csv' and 'Unused_Acidity_data.csv'

# Load the datasets
wines_df = main_df

# Create the main dataset without expanding list columns
body_df = wines_df.copy()

# Create a mapping for BodyOrdinal
body_mapping = {
    "Very full-bodied": 5,
    "Full-bodied": 4,
    "Medium-bodied": 3,
    "Light-bodied": 2,
    "Very light-bodied": 1
}

# Apply the mapping to create a new column 'BodyOrdinal'
body_df['BodyOrdinal'] = body_df['Body'].map(body_mapping).fillna(1).astype(int)

# Create a new DataFrame to hold the expanded rows
expanded_rows = []

# Define the sequence of letters to use
letters = ['A', 'B', 'C', 'D', 'E']

# Create a list to hold the unused letters rows
unused_letter_rows = []

# Iterate through each row and expand it according to 'BodyOrdinal'
for index, row in body_df.iterrows():
    used_letters = letters[:row['BodyOrdinal']]
    unused_letters = letters[row['BodyOrdinal']:]
    for i in range(row['BodyOrdinal']):
        expanded_row = row.copy()
        expanded_row['BodyOrdinal'] = used_letters[i]
        expanded_rows.append(expanded_row)
    for letter in unused_letters:
        unused_row = row.copy()
        unused_row['UnusedLetter'] = letter
        unused_letter_rows.append(unused_row)

# Create a new DataFrame from the expanded rows
expanded_df = pd.DataFrame(expanded_rows)

# Create the DataFrame for unused letters
unused_letters_df = pd.DataFrame(unused_letter_rows)

# Select only the 'WineID' and 'BodyOrdinal' columns for the new CSV
result_df = expanded_df[['WineID', 'BodyOrdinal']]

# Save the main and expanded dataframes to CSV files
result_df.to_csv('C:/Users/sytse/Documents/Maastricht University/Master BISS/4225 Data Visualisation/Infographic/Wine Data/Final Data/Body_data.csv', index=False)

# Display the first few rows of each dataset
result_df.head(10)

# Select only the 'WineID' and 'UnusedLetter' columns for the new CSV
unused_result_df = unused_letters_df[['WineID', 'UnusedLetter']]

unused_result_df.to_csv('C:/Users/sytse/Documents/Maastricht University/Master BISS/4225 Data Visualisation/Infographic/Wine Data/Final Data/Unused_Body_data.csv', index=False)

unused_result_df.head(10)

acidity_df = wines_df.copy()

# Create a mapping for AcidityOrdinal   
acidity_mapping = {
    "Low": 1,
    "Medium": 2,
    "High": 3
}

# Apply the mapping to create a new column 'AcidityOrdinal'
acidity_df['AcidityOrdinal'] = acidity_df['Acidity'].map(acidity_mapping).fillna(1).astype(int)

# Create a new DataFrame to hold the expanded rows
expanded_rows = []

# Define the sequence of letters to use
ac_letters = ['A', 'B', 'C']

# Create a list to hold the unused letters rows
unused_letter_rows = []


# Iterate through each row and expand it according to 'AcidityOrdinal'
for index, row in acidity_df.iterrows():
    used_letters = ac_letters[:row['AcidityOrdinal']]
    unused_letters = ac_letters[row['AcidityOrdinal']:]
    for i in range(row['AcidityOrdinal']):
        expanded_row = row.copy()
        expanded_row['AcidityOrdinal'] = used_letters[i]
        expanded_rows.append(expanded_row)
    for letter in unused_letters:
        unused_row = row.copy()
        unused_row['Ac_UnusedLetter'] = letter
        unused_letter_rows.append(unused_row)

# Create a new DataFrame from the expanded rows
expanded_df = pd.DataFrame(expanded_rows)

# Create the DataFrame for unused letters
unused_ac_letters_df = pd.DataFrame(unused_letter_rows)

# Select only the 'WineID' and 'AcidityOrdinal' columns for the new CSV
ac_result_df = expanded_df[['WineID', 'AcidityOrdinal']]
ac_result_df.to_csv('C:/Users/sytse/Documents/Maastricht University/Master BISS/4225 Data Visualisation/Infographic/Wine Data/Final Data/Acidity_data.csv', index=False)

# Select only the 'WineID' and 'Ac_UnusedLetter' columns for the new CSV
unused_ac_result_df = unused_ac_letters_df[['WineID', 'Ac_UnusedLetter']]
unused_ac_result_df.to_csv('C:/Users/sytse/Documents/Maastricht University/Master BISS/4225 Data Visualisation/Infographic/Wine Data/Final Data/Unused_Acidity_data.csv', index=False)

# Display the first few rows of each dataset
ac_result_df.head(10), unused_ac_result_df.head(10)