# import pandas as pd

# # Step 1: Load the raw data
# file_path = r"C:\Users\prave\OneDrive\Desktop\HAR\My_data\combined_data.csv"  
# data = pd.read_csv(file_path, delim_whitespace=True)  # Assuming the file uses whitespace as delimiter

# # Step 2: Calculate statistical features grouped by 'activity' and 'subject'
# agg_data = data.groupby(['activity', 'subject']).agg(
#     Mean_X=('ax (m/s^2)', 'mean'),
#     StdDev_X=('ax (m/s^2)', 'std'),
#     Min_X=('ax (m/s^2)', 'min'),
#     Max_X=('ax (m/s^2)', 'max'),
#     Mean_Y=('ay (m/s^2)', 'mean'),
#     StdDev_Y=('ay (m/s^2)', 'std'),
#     Min_Y=('ay (m/s^2)', 'min'),
#     Max_Y=('ay (m/s^2)', 'max'),
#     Mean_Z=('az (m/s^2)', 'mean'),
#     StdDev_Z=('az (m/s^2)', 'std'),
#     Min_Z=('az (m/s^2)', 'min'),
#     Max_Z=('az (m/s^2)', 'max')
# ).reset_index()

# # Step 3: Save the aggregated data to a new CSV file
# output_file_path = "C:\Users\prave\OneDrive\Desktop\HAR\My_data\my_processed_data.csv"  # Replace with your desired output file path
# agg_data.to_csv(output_file_path, index=False)

# print(f"Aggregated data saved to {output_file_path}")


import pandas as pd
import os
from sklearn.model_selection import train_test_split

# Load the original dataset
file_path = r"C:\Users\prave\OneDrive\Desktop\HAR\My_data\my_processed_data.csv"  # Replace with the correct path to your CSV file
data = pd.read_csv(file_path)

# Perform stratified split to maintain the distribution of activities
train_data, test_data = train_test_split(
    data, 
    test_size=0.3, 
    stratify=data['Activity'],  # Use 'Activity' column for stratification
    random_state=42  # For reproducibility
)

# Define output directory
output_dir = "./My_data"  # Directory where you want to save the files
os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Define file paths for saving the split data
train_file_path = os.path.join(output_dir, "my_processed_data_train.csv")
test_file_path = os.path.join(output_dir, "my_processed_data_test.csv")

# Save the split data into separate CSV files
train_data.to_csv(train_file_path, index=False)
test_data.to_csv(test_file_path, index=False)

print(f"Training data saved to: {train_file_path}")
print(f"Testing data saved to: {test_file_path}")
