import requests
from newsapi import NewsApiClient
import json
# api =c4a3fae0ae0e43efa1cb9e515e5fc022
import requests
def speak(str):
    from win32com.client import Dispatch
    speakr = Dispatch("SAPI.SpVoice")
    speakr.Speak(str)
  
  
if __name__=='__main__':
    speak("Deeksha , News for today..")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=c4a3fae0ae0e43efa1cb9e515e5fc022"
    r= requests.get(url).text
    # print(r)
    news= json.loads(r)
    print(news['articles'])
    arts = news['articles']
    no_of_new = news['totalResults']
    speak(f"Today a Total of {no_of_new} news are with us , so , lets start ")
    for titl in arts:
        speak(titl['title'])
        speak("Next news...  ")



    
   

