import pandas as pd
from scipy import stats

file_path = "C:\\Users\\ALAM MAHESH\\Downloads\\online.csv"  
data = pd.read_csv(file_path)

ratings = data['reviews rating ']


confidence_level = 0.95  
confidence_interval = stats.norm.interval(confidence_level, loc=ratings.mean())


print(f"Average Rating: {ratings.mean():.2f}")
print(f"Confidence Interval ({confidence_level * 100:.0f}%): ({confidence_interval[0]:.2f}, {confidence_interval[1]:.2f})")
