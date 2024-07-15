# import csv
import pandas

# CSV - Comma Separated Values
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

data = pandas.read_csv("weather_data.csv")
# print(data)  # type = DataFrame (all the data)
# print(data["temp"])  # type = Series (a single column)

# converting the data to a dictionary
# data_dict = data.to_dict()
# print(data_dict)

# converting data to a list
# temp_list = data["temp"].to_list()
# print(temp_list)

# average
# average = sum(temp_list) / len(temp_list)
# print(average)

# average
# print(data["temp"].mean())

# max value
# print(data["temp"].max())

# min value
# print(data["temp"].min())

# print(data.temp)  # as an object
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# temperature in Fahrenheit
# monday = data[data.day == "Monday"]
# temperature = monday.temp[0] * (9/5) + 32
# print(temperature)

# create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Rubia"],
    "scores": [76, 56, 65]
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("new_data.csv")
