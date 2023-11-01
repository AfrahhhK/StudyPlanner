
import pandas as pd

df = pd.read_csv('E:\\Geetika\\Programs\\Pandas\\finalYear_Project\\International_students_Time_management_data.csv')
print(df)

print("\n\ndf.head():")
print(df.head())

print("\n\ndf.info():")
print(df.info())

print("\n\ndf.describe():")
print(df.describe())

# Remove rows with missing values
df = df.dropna()

# Fill missing values with a specific value
df = df.fillna(0)

# removing duplicates
df = df.drop_duplicates()

df.to_csv('preprocessed_data.csv', index=False)



# with open('E:\\Geetika\\Programs\\Pandas\\finalYear_Project\\International_students_Time_management_data.csv') as f:

#     data = f.read()
#     data = data.split("\n")

# print(data) 

# newData = []
# for line in data:
#     # print(line)
#     newData.append(line.split(","))