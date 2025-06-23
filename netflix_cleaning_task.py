import pandas as pd

# Load the dataset
df = pd.read_csv("netflix_titles.csv")

# Remove duplicate rows
df = df.drop_duplicates()

# Handle missing values before datetime
df['director'] = df['director'].fillna('Unspecified')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna(df['country'].mode()[0])
df['rating'] = df['rating'].fillna('Not Rated')

# Standardize column names
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Clean 'show_id' and 'cast'
df['show_id'] = df['show_id'].str.replace("s", "", regex=False)
df['cast'] = df['cast'].str.split(',').str[0].str.strip()

# Convert to datetime
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# 🟨 Fill any NaT dates with a default (e.g., Jan 1, 2020)
df['date_added'] = df['date_added'].fillna(pd.Timestamp('2020-01-01'))

# Extract year and month
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month

# Check the All null values
print(df.isnull().sum())

# Check the All Dublicated values
print("Duplicatea value : ", df.duplicated().sum())

# Save the cleaned dataset
df.to_csv("netflix_titles_cleaned.csv", index=False)

print("Netflix dataset cleaned and saved as 'netflix_titles_cleaned.csv'")