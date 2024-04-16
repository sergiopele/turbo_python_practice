import csv
import string
from turtle import color
from numpy import size
import pandas

DATA_FILE_PATH = "day25/weather_data.csv"


def read_data_temperature(file_path: str) -> list[int]:
    with open(file_path) as file_data:
        extracted_file: list = list(csv.reader(file_data))
        return [int(extracted_file[1][1]) for i in range(1, len(extracted_file))]


data = pandas.read_csv(DATA_FILE_PATH)
# temp = data["temp"].to_list()
# avarage_temp = data["temp"].mean()
# max_temp = data["temp"].max()
# print(max_temp)

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.temp * 9 / 5 + 32)

# data_ = {
#         "names": ["Alex", "Josh", "Semen"],
#         "scores":[1,3,5]
# }

# data_frame = pandas.DataFrame(data=data_)

# print(data_frame)
data = pandas.read_csv("day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])

table = pandas.DataFrame(
    {"Count": [gray, black, red], "Fur color": ["Gray", "Black", "Red"]}
).to_csv("color_count.csv", index=False)
print(table)
