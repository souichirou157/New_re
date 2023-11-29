import json

class WeatherAPI:
    
    def __init__(self,api_key,api_host):
        self.api_key = api_key
        self.api_host= api_host    
    
    def Getweather(self,location,days=1):
        
        url = "https://weatherapi-com.p.rapidapi.com/current.json"#api-url
        querystring = {"q":location,"days":days}#地名と日にちをリクエスト
        
        headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": self.api_host
        }
        
        response = requests.request("GET", url, headers=headers, params=querystring)
        
        weather = json.loads(response.text)
        
        return weather
    
    
api_key = "273733282amsh7b756a1313157cbp1dc6c1jsn02544ccf13f0"
api_host = "weatherapi-com.p.rapidapi.com"
weather_api = WeatherAPI(api_key, api_host)
print(weather_api)
print('\n')
weather = weather_api.Getweather("location:",'fukuoka')


print(weather["location"]["region"])
print(weather["location"]["localtime"])
print(weather["current"]["temp_c"])





