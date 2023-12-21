import pandas as pd
from sklearn.cluster import KMeans
from sklearn.impute import SimpleImputer
from sklearn.metrics import pairwise_distances_argmin_min

# Create a DataFrame from the CSV data
df = pd.read_csv(r"C:\\Users\\Rajender\\Documents\\GitHub\\StudyPlanner\\final_data.csv")

# Assume user provides input in a dictionary format
user_input = {
    'Academic': 2,
    'Attendance': 3, 
    '6': 2.0,
    '7': 3,
    '8': 3.0,
    '9': 3.0,
    '10': 2.0,
    '11': 2.0,
    '12': 2,
    '13': 3.0,
    '14': 4,
    '15': 3.0,
    '16': 4.0,
    '17': 4.0,
    'Course': 'Science and engineering'
}

# Extract the relevant columns for clustering
columns_for_clustering = ['Academic', 'Attendance', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17']

# Subset the DataFrame with the selected columns
X = df[columns_for_clustering]

# Impute missing values
imputer = SimpleImputer(strategy='mean')  # You can choose a different strategy if needed
X_imputed = pd.DataFrame(imputer.fit_transform(X), columns=columns_for_clustering)

# Perform k-means clustering
kmeans = KMeans(n_clusters=5, random_state=42)  # Adjust the number of clusters as needed
df['Cluster'] = kmeans.fit_predict(X_imputed)

# Find the cluster of the user input
user_input_values = [user_input[col] for col in columns_for_clustering]
user_cluster = kmeans.predict([user_input_values])[0]

# Find the most similar data point in the user's cluster
cluster_data = df[df['Cluster'] == user_cluster]
closest_point_idx = pairwise_distances_argmin_min([user_input_values], X_imputed.iloc[cluster_data.index])[0][0]
closest_point = df.iloc[closest_point_idx]

# Extract the relevant information for the closest point
hours_week = closest_point['hours_week']
days_studied_week = closest_point['days_studied_week']
hours_at_time = closest_point['hours_at_time']
time_day_studied = closest_point['time_day_studied']


# Mapping for 'hours_week'
hours_week_mapping = {1: '<5', 2: '5-10', 3: '10-15', 4: '15-20', 5: '>20'}
df['hours_week'] = df['hours_week'].map(hours_week_mapping)

# Mapping for 'days_studied_week'
days_studied_week_mapping = {1: '<2', 2: '3', 3: '4', 4: '5', 5: '>5'}
df['days_studied_week'] = df['days_studied_week'].map(days_studied_week_mapping)

# Mapping for 'hours_at_time'
hours_at_time_mapping= {1: '<1', 2: '2', 3: '3', 4: '>4'}
df['hours_at_time'] = df['hours_at_time'].map(hours_at_time_mapping)

# Mapping for 'time_day_studied'
time_day_studied_mapping = {1: 'morning', 2: 'afternoon', 3: 'evening', 4: 'midnight'}
df['time_day_studied'] = df['time_day_studied'].map(time_day_studied_mapping)

# Print the results
print(f"Most similar data point to user input:\n{closest_point}")
print(f"\nRecommended study pattern:\n"
      f"Hours per week: {hours_week}\n"
      f"Days studied per week: {days_studied_week}\n"
      f"Hours at a time: {hours_at_time}\n"
      f"Time of day studied: {time_day_studied}")


print(f"Most similar data point to user input:\n{closest_point}")
print(f"\n**Mapped values**\nRecommended study pattern:\n"
      f"Hours per week: {hours_week_mapping}\n"
      f"Days studied per week: {days_studied_week_mapping}\n"
      f"Hours at a time: {hours_at_time_mapping}\n"
      f"Time of day studied: {time_day_studied_mapping}")



