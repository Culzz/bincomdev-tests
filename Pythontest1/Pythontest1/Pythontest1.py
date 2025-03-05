import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("student_performance.csv")

# Display basic information
print("First 5 rows of dataset:")
print(df.head())
print("\nDataset Information:")
print(df.info())
print("\nStatistical Summary:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handling missing values
df.fillna(df.mean(), inplace=True)  # Fill numerical missing values with mean
df.dropna(inplace=True)  # Drop rows with missing categorical values

# Check for duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())
df.drop_duplicates(inplace=True)

# Statistical Analysis
print("\nMean Scores:")
print(df[['Math_Score', 'Reading_Score', 'Writing_Score']].mean())

print("\nMedian Scores:")
print(df[['Math_Score', 'Reading_Score', 'Writing_Score']].median())

print("\nStandard Deviation:")
print(df[['Math_Score', 'Reading_Score', 'Writing_Score']].std())

# Correlation Heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(df[['Math_Score', 'Reading_Score', 'Writing_Score']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Between Scores")
plt.show()

# Distribution of Scores
plt.figure(figsize=(12, 6))
sns.histplot(df['Math_Score'], kde=True, color='blue', label="Math Score")
sns.histplot(df['Reading_Score'], kde=True, color='green', label="Reading Score")
sns.histplot(df['Writing_Score'], kde=True, color='red', label="Writing Score")
plt.legend()
plt.title("Distribution of Scores")
plt.show()

# Gender-Based Performance
plt.figure(figsize=(10, 5))
sns.boxplot(x='Gender', y='Math_Score', data=df, palette="Set2")
plt.title("Math Score Distribution by Gender")
plt.show()

# Impact of Parental Education on Performance
plt.figure(figsize=(12, 6))
sns.boxplot(x='Parental_Education', y='Math_Score', data=df, palette="muted")
plt.xticks(rotation=45)
plt.title("Impact of Parental Education on Math Score")
plt.show()

# Effect of Test Preparation Course
plt.figure(figsize=(8, 4))
sns.barplot(x='Test_Preparation_Course', y=df[['Math_Score', 'Reading_Score', 'Writing_Score']].mean(axis=1), data=df, palette="coolwarm")
plt.title("Test Preparation Course Impact on Average Score")
plt.show()

# Save cleaned dataset
df.to_csv("cleaned_student_performance.csv", index=False)
print("\nCleaned dataset saved as 'cleaned_student_performance.csv'")

