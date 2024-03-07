import numpy as np
house_data = np.array([[3, 1500, 200000], [4, 1800, 250000], [5, 2000, 300000], [6, 2200, 350000], [4, 1900, 270000], [5, 2100, 320000]])
filtered_data = house_data[house_data[:, 0] > 4]

average_sale_price = np.mean(filtered_data[:, 2])

print(f"The average sale price of houses with more than four bedrooms is: {average_sale_price:.2f}")
