import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime
import time
import random
from random import randint
from time import sleep
from PIL import Image


img = Image.open('pot.png')
image = Image.open('mint.jpg')
resized_image = image.resize((1000,300))

st.set_page_config(page_title ='Smart farm', page_icon=img)
first_lock_1 = False
first_lock_2 = False
data_flag_1 = False
data_flag_2 = False
first_lock_3 = False
data_flag_3 = False

max_humidity = 0
min_humidity = 100

humd_array = np.array([])

st.header('**_Soil moisture [MINT]_**')


st.image(resized_image)

status_text_1 = st.empty()
status_text_2 = st.empty()
status_text_3 = st.empty()
status_text_4 = st.empty()
status_text_5 = st.empty()
status_text_6 = st.empty()
placeholder = st.empty()
my_bar = st.progress(0)


while True: 
    req_body = {
            "humidity": randint(70, 90)
            } #the last bit gets rid of the new-line chars

    humidity = req_body.get('humidity')

    if humidity:

        print("Current Humidity is: ")
        print(humidity)
        data_flag_2 = True
        if humidity >  max_humidity:
            max_humidity = humidity
        if humidity <  min_humidity:
            min_humidity = humidity
    with placeholder.container():
            a1, a2, a3 = st.columns(3)
            a1.metric("Latest humidity", f"{humidity}%")
            a2.metric("Highest humidity", f"{max_humidity}%")
            a3.metric("Lowest humidity", f"{min_humidity}%")    

    #Create a chart first
    if data_flag_2==True:

        if first_lock_1==False and first_lock_2==False:

            first_lock_2 = True
            first_lock_1 = True
            first_lock_3=True
            max_humidity = humidity
            min_humidity = humidity
            total_data = np.array([[humidity]])
            chart_data = pd.DataFrame(total_data,
                                    columns=['Humidity'])
            chart = st.line_chart(chart_data)
            print("Initialize complete ... ")

        else:

            data_flag_1 = False
            data_flag_2 = False
            total_data = np.array([[humidity]])
            chart_data = pd.DataFrame(total_data,
                                    columns=['Humidity'])

            chart.add_rows(chart_data)
            my_bar.progress(humidity)

    time.sleep(1)
