import pandas
# data = pandas.read_csv("weather_data - Sheet1.csv")
# average = data["temp"].mean()
# maximum = data["temp"].max()
# #Get data from a row
# monday = data[data.day == "Monday"]
# monday_temp_fahr = (monday.temp * 9/5) + 32
# print(monday_temp_fahr)
#Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy","James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_fur_count = len(data[data["Primary Fur Color"]=="Gray"])
red_fur_count = len(data[data["Primary Fur Color"]=="Cinnamon"])
black_fur_count = len(data[data["Primary Fur Color"]=="Black"])

squirrel_count = {
    "Fur Color": ["Black", "Red", "Gray"],
    "Count": [black_fur_count, red_fur_count, gray_fur_count]
}

data_seq = pandas.DataFrame(squirrel_count)
data_seq.to_csv("squirrel_count")