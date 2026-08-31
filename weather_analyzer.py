import pandas as pd
#Read the weather data
data=pd.read_csv("weather_data.csv")

#Calculate average temperature
average_temperature=data["Temperature"].mean()

#Find highest and lowest temperature
highest_temperature=data["Temperature"].max()
lowest_temperature = data["Temperature"].min()

#Calculate average humidity
average_humidity=data["Temperature"].min()

#calculate total rainfall
total_rainfall=data["Rainfall"].sum()

#Find hosttest and coldest days
hottest_day=data.loc[data["Temperature"].idxmax()]
coldest_day=data.loc[data["Temperature"].idxmin()]

#Display reults
print("WEATHER DATA ANALYSIS")
Print("---------------------")

print("Average Temperature:",round(average_temperature,2),"C")

print("Highest Temperature:",highest_temperature,"C")

print("lowest Temperature:",lowest_temperature,"C")

print("Total Rainfall:",total_rainfall,"mm")

print("\nHottestDay:")
print(hottest_day["Date"],"-",coldest_day["Temperature"],"c")
