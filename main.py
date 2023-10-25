#---------------------------Libraries and Module Used-----------------------------------------------#
import requests
import json
import pyttsx3
from iso3166 import countries
#---------------------------------------------------------------------------------------------------#


#---------------------------initialization of speech-----------------------------------------------#
engine = pyttsx3.init()
#--------------------------------------------------------------------------------------------------#


#---------------------------Welcome speech when program start--------------------------------------#
engine.say("Welcome you to the Weather App")
print("Please Wait....")
engine.runAndWait()
#--------------------------------------------------------------------------------------------------#


#---------------------------api key to fetch details-----------------------------------------------#
API_key = "e7713e3aeb55755448c7c9f9fa285bfd"
#--------------------------------------------------------------------------------------------------#


# ---------------------------All functions Used------------------------------------------------------#
def selection(): # function to call selection
        print("\n" + "Press 1 to Enter City Name or Press 'q' to Quit".center(70, "*"))
        selection = input("\nEnter your input : ")
        return selection

def fetch_data(city_name):# function for getting data from api convert it in json format
        res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}")
        data = json.loads(res.text)
        return data

def kel_to_cel(temp): # function to change temperature from kelvin to Celsius
	temp = float(temp)-273.15
	return str(round(temp, 1))

def head_foot_format(txt): # function to format "-" in the header and footer
	txt = txt.center(40, "-")
	return txt

def result(data): # function to show final result
        city = data["name"]
        country = countries.get(data["sys"]["country"]).name
        weather = data["weather"][0]["main"]
        temp = kel_to_cel(data["main"]["temp"])
        max_temp = kel_to_cel(data["main"]["temp_max"])
        min_temp = kel_to_cel(data["main"]["temp_min"])

        try:
                print(f'\n{head_foot_format(" Weather Details ")}\nCity : {city}\nCountry : {country} \nWeather : {weather} \nTemperature : {temp} \N{DEGREE SIGN}C \nMaximum Temperature : {max_temp} \N{DEGREE SIGN}C \nMinimum Temperature : {min_temp} \N{DEGREE SIGN}C \n{head_foot_format("")}')

                print("Please Wait....")

                engine.say(f'You Entered City Name {data["name"]}')
                engine.say(f'Country Name {country}')
                engine.say(f'Weather {weather}')
                engine.say(f'Temperature {temp} \N{DEGREE SIGN}C')
                engine.say(f'Maximum Temperature {max_temp} \N{DEGREE SIGN}C')
                engine.say(f'Minimum Temperature {min_temp} \N{DEGREE SIGN}C')
        except:
                print("Entered Wrong City Name. Please Try Again")
                engine.say(f'You Entered Wrong City Name. Please Try Again !')
                print("Please Wait....")
        engine.runAndWait()
# -----------------------------------------------------------------------------------------------------#



#------------------------------------------Program-----------------------------------------------------#
while(True):
        selection_value = selection()
        if selection_value == "1":
                city_name = input("\nEnter the name of the city for Weather Details : ")
                data = fetch_data(city_name)
                result(data)
                continue
        elif selection_value == "q":
                print(selection_value)
                break
#------------------------------------------------------------------------------------------------------#    

        
        
