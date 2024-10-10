# import requests

# class API:
#  def sentiment_analysis(self,text):
#   url = "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/"

  
#   querystring = text

#   headers = {
# 	"x-rapidapi-key": "e595913211msh89f5988df939177p1a0427jsn8076c2e4d727",
# 	"x-rapidapi-host": "twinword-sentiment-analysis.p.rapidapi.com"
# }

#   response = requests.get(url, headers=headers, params=querystring)
#   print(response)

# import paralleldots

# class API:
#     def __init__(self):
#         # Replace with your actual API key from ParallelDots
#         paralleldots.set_api_key("XXYd2KTC61CaOv2owJYEqGJAEg9HtotX")
    
#     def sentiment_analysis(self, text):
#         # Call Paralleldots sentiment analysis API
#         response = paralleldots.sentiment(text)
#         return response

import requests

class API:
 def sentiment_analysis(self, cute):
  url = "https://api.apilayer.com/sentiment/analysis"

  payload = cute
  headers= {
   "apikey": "XXYd2KTC61CaOv2owJYEqGJAEg9HtotX"
}

  response = requests.request("POST", url, headers=headers, data = payload)

  status_code = response.status_code
  result = response.text
  return result

