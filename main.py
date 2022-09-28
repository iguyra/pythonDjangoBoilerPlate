

# FUNCTIONS
# def hello(age,name):
#     if name == "ra":
#         return f"you the man of {age}"
#     else:
#         return "you NOT the man"


# names = ["ra","res","boos"]

# for name in names:
#     print(name)


# CLASSES AND ONJECT
# class Phone:
#     def __init__(self, brand,price):
#             self.brand = brand
#             self.price = price

#     def call(self, phoneNumber):
#         print(f"{self.brand} is calling {phoneNumber}")

#     def __str__(self):
#          return f"brand: {self.brand}, price: {self.price}"


# newPhone = Phone("samsung", 400)

# print(newPhone.brand)
# newPhone.call("911")
# print(newPhone)


# DATES
# from datetime import datetime

# # print(datetime.now())
# now = datetime.now()
# print(now)

# print(now.strftime("%d %m %Y %H %M %S"))
# print(now.strftime("%d %B %Y %H %M %S"))


# WORKING WITH FILES

# creating file
# file = open("./data.csv","w")

# writin to file
# file = open("./data.csv","r+")
# file.write("name, age, weight\n")
# #append to file
# file = open("./data.csv","a")
# file.write("boos, bima, boss")

# READING FILE
# file = open("./data.csv","r")
# print(file.read())

# reading file line by line
# for line in file:
#     print(line)

# print(file.readlines())
# file.close()

# with open("./data.csv","r") as file:
#     print(file.read())

# import os.path

# filename = "./data.csv"

# if os.path.isfile(filename):
#     with open(filename,"r") as file:
#         print(file.read())
# else:
#     print(f"file {filename} name does not exist")


# FETCHING DATA FROM THE INTERNET

import pyttsx3
from urllib import request

# r = request.urlopen("http://www.google.com")

# print(r.getcode())
# print(r.read())
# url = "https://dad-jokes.p.rapidapi.com/random/joke/png"
# r = request.urlopen(url)

# print(r.getcode())
# print(r.read())

import requests

url = "https://dad-jokes.p.rapidapi.com/random/joke/png"

headers = {
    "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
    "X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.text)


pyttsx3.speak("hellow world welcoem res")
