import streamlit as st
import requests
API_KEY = "9edb14a6e913ec7c76f993b09a08da19"

def convert_to_celcius(temprature_in_kelvin):
      return temprature_in_kelvin -273.15


def find_current_weather(city):
    #base_url  = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    weather_data = requests.get(base_url).json()    
    try:
          general = weather_data['weather'][0]['main']
          icon_id = weather_data['weather'][0]['icon']
          temprature = round(convert_to_celcius(weather_data['main']['temp']))
          icon = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    except KeyError:
          st.error("City Not Found")
          st.stop()
    return general,temprature,icon


def main():      
        st.header("Find the Weather")
        city = st.text_input("Enter the City").lower()
        if st.button("Find"):
            general,temperature,icon = find_current_weather(city)
            col_1,col_2 = st.columns(2)
            with col_1:
                  st.metric(label= "Temprature",value=f"{temperature}°C")
            with col_2:
                  st.write(general)
                  st.image(icon)


    
if __name__ == '__main__':
        main()