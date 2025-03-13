import streamlit as st
import requests
import pandas as pd

st.title("Weather Forecast 🌤️")
st.write("This is the weather app that uses Open Meteo API that takes your coordinates and returns weather forecast!")

st.sidebar.header("Instructions")
st.sidebar.write("""
1. Enter a location by its longitude and latitude
2. Click enter
3. See the 7 day forecast in table format, and graph format below
4. Modify data using + or - or even change numbers manually
""")

url = "https://api.open-meteo.com/v1/forecast" # https://open-meteo.com/en/docs

st.header("📍 Enter Location")
# default to GT's coordinates
latitude = st.number_input("Enter the Latitude:", value=33.7501, step=0.1)  #NEW
longitude = st.number_input("Enter the Longitude:", value= -84.3885, step=0.1)

st.header("🌦️ Weekly Weather")
information = {
    "latitude": latitude,
    "longitude": longitude,
    "daily": ["temperature_2m_max", "temperature_2m_min"],
    "timezone": "auto"
}
response = requests.get(url, params = information)
weatherFrame = pd.DataFrame()

if response.status_code == 200:
    data = response.json().get("daily")
    if data:
        dates = data["time"]
        max = data["temperature_2m_max"]
        min = data["temperature_2m_min"]

        weatherFrame = pd.DataFrame({
            "Date": dates,
            "Max Temperature(C°)": max,
            "Min Temperature(C°)": min
        })
        st.dataframe(weatherFrame) #NEW
    else:
        st.warning("No data found for that location") #NEW
else:
    st.error("Error, check inputs") #NEW

st.header("📈 Temperature Graph")
if not weatherFrame.empty:
    st.line_chart(weatherFrame.set_index("Date")) #NEW
else:
    st.info("No data provided by API") #NEW