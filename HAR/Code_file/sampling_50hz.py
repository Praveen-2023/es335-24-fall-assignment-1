import pandas as pd

# Load the dataset
input_file = "C:\\Users\\prave\\Downloads\\sitting_praveen_sample_1.csv"  # Use double backslashes to avoid escape characters
data = pd.read_csv(input_file)

# Downsample by keeping every 4th sample
downsampled_data = data.iloc[::4, :].reset_index(drop=True)

# Save the downsampled data to a new CSV file
output_file = 'downsampled_dataset.csv'  # Replace with your desired output file name
downsampled_data.to_csv(output_file, index=False)

print("Downsampling complete. Downsampled data saved to", output_file)
