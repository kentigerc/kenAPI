import requests
from django.shortcuts import render



def home(request):
  #USING APIS=> Example 1
  response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=40" + "&lon=-74")
  data = response.json()
  results = data['message']

  #Example 2
  response2 = requests.get("https://api.openweathermap.org/data/2.5/weather?")
  data2 = response2.json()
  results2 = data2['message']
  return render(request, 'templates/index.html', {'results': results}, {'results2': results2})