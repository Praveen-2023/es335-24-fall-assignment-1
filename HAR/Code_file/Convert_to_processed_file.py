import pandas as pd
import os

# Define paths
combined_path = "./Combined"  # Assuming data is combined here
output_path = "./Processed"  # Path to save processed data

# Dictionary of activities
ACTIVITIES = {
    1: 'WALKING',
    2: 'WALKING_UPSTAIRS',
    3: 'WALKING_DOWNSTAIRS',
    4: 'SITTING',
    5: 'STANDING',
    6: 'LAYING',
}

# Ensure output directory exists
if not os.path.exists(output_path):
    os.makedirs(output_path)

def calculate_statistics(df):
    """
    Calculate the mean, standard deviation, min, and max for X, Y, Z axes.
    """
    stats = {
        'Mean_X': df['accx'].mean(),
        'StdDev_X': df['accx'].std(),
        'Min_X': df['accx'].min(),
        'Max_X': df['accx'].max(),
        'Mean_Y': df['accy'].mean(),
        'StdDev_Y': df['accy'].std(),
        'Min_Y': df['accy'].min(),
        'Max_Y': df['accy'].max(),
        'Mean_Z': df['accz'].mean(),
        'StdDev_Z': df['accz'].std(),
        'Min_Z': df['accz'].min(),
        'Max_Z': df['accz'].max()
    }
    return stats

def process_data(activity_folder, activity_name):
    """
    Process CSV files in a given activity folder and save the statistics, including subject info.
    """
    data_frames = []
    
    # Loop through all subjects in the activity folder
    for subject_file in os.listdir(activity_folder):
        if subject_file.endswith(".csv"):
            file_path = os.path.join(activity_folder, subject_file)
            df = pd.read_csv(file_path)
            subject_id = os.path.splitext(subject_file)[0].split('_')[-1]  # Extract subject ID from filename
            stats = calculate_statistics(df)
            stats['Activity'] = activity_name
            stats['Subject'] = subject_id
            data_frames.append(stats)
    
    # Convert list of dicts to DataFrame and return
    result_df = pd.DataFrame(data_frames)
    return result_df

def main():
    # Initialize lists to collect data frames for train and test data
    train_data_frames = []
    test_data_frames = []

    # Process training data
    for activity in ACTIVITIES.values():
        activity_folder = os.path.join(combined_path, "Train", activity)
        train_df = process_data(activity_folder, activity)
        train_data_frames.append(train_df)
    
    # Process testing data
    for activity in ACTIVITIES.values():
        activity_folder = os.path.join(combined_path, "Test", activity)
        test_df = process_data(activity_folder, activity)
        test_data_frames.append(test_df)

    # Concatenate all data frames and save to CSV files
    train_result_df = pd.concat(train_data_frames, ignore_index=True)
    test_result_df = pd.concat(test_data_frames, ignore_index=True)

    train_result_df.to_csv(os.path.join(output_path, "processedata_train.csv"), index=False)
    test_result_df.to_csv(os.path.join(output_path, "processedata_test.csv"), index=False)

if __name__ == "__main__":
    main()
