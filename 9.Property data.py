import numpy as np
num_houses = int(input("Enter the number of houses: "))
house_data_list = []
for i in range(num_houses):
    print(f"\nEnter details for House {i + 1}:")
    bedrooms = int(input("Number of bedrooms: "))
    square_footage = float(input("Square footage: "))
    sale_price = float(input("Sale price: "))
    house_data_list.append([bedrooms, square_footage, sale_price])
house_data = np.array(house_data_list)
houses_more_than_4_bedrooms = house_data[house_data[:, 0] > 4]  
sale_prices = houses_more_than_4_bedrooms[:, -1]  
average_sale_price = np.mean(sale_prices)

print("\nAverage sale price of houses with more than four bedrooms:", average_sale_price)
