import requests
import streamlit as st

# This program gets and displays Nasa's image of the day using python and streamlit

api_key = "Replace with API Key obtained from NASA's OPEN API website"
get_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# making network get request
response1 = requests.get(get_url)
data = response1.json()  # returns the json from the request

# extracting the necessary data values using json keys
title = data["title"]  # image title
image_url = data["url"]  # this is the image url
description = data["explanation"]  # image description

# downloading the image
image_filepath = "img.png"  # this is the filepath where the image will be stored
response2 = requests.get(image_url)
with open(image_filepath, "wb") as file:  # wb stands for write binary
    file.write(response2.content)

# making the ui
st.title(title)
st.image(image_filepath)
st.write(description)