import pandas as pd
import matplotlib.pyplot as plt

# Read the daily weather data from a CSV file
weather_data = pd.read_csv('daily_weather_data.csv')

# Display the first few rows of the dataset
print(weather_data.head())

# Calculate summary statistics
summary_stats = weather_data.describe()
print(summary_stats)

# Visualize temperature over time
plt.figure(figsize=(10, 6))
plt.plot(weather_data['Date'], weather_data['Temperature'], marker='o', linestyle='-')
plt.xlabel('Date')
plt.ylabel('Temperature (Celsius)')
plt.title('Daily Temperature Variation')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Visualize precipitation over time
plt.figure(figsize=(10, 6))
plt.plot(weather_data['Date'], weather_data['Precipitation'], marker='o', linestyle='-')
plt.xlabel('Date')
plt.ylabel('Precipitation (mm)')
plt.title('Daily Precipitation Variation')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
