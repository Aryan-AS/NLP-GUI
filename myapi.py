import requests

class API:
  def sentiment_analysis(self,cute):

   url = "https://sentiment-analysis9.p.rapidapi.com/sentiment"
   
   payload = [
   	{
   		"id": "1",
   		"language": "en",
   		"text": cute
   	}
   ]
   headers = {
   	"x-rapidapi-key": "9136cbe998msh78b7572a1d66429p165b86jsn536cddaba829",
   	"x-rapidapi-host": "sentiment-analysis9.p.rapidapi.com",
   	"Content-Type": "application/json",
   	"Accept": "application/json"
   }
   
   response = requests.post(url, json=payload, headers=headers)
   
   result =response.json()
   return result
    
   
