from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.generic import FormView
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from .models import Command, State

#Web scraping libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json

#Create objects outside of functions 

command = Command()
state = State()

def index(request):
    #print(state.state)
    ydata = []
    xdata = []
    dictTraceData = {}
    #Possible Exception raised here by the fact that a random string could be returned
    try:
        #Collect data from the website
        dictTraceData = requests.get("http://flaskosa.herokuapp.com/cmd/TRACE").json()
        ydata = dictTraceData["ydata"]
        xdata = dictTraceData["xdata"]

        #If there was an error in scraping the data from the website
        try:
            urlToScrape = "http://flaskosa.herokuapp.com/cmd/" + command.command
            response = requests.get(urlToScrape)
            data = BeautifulSoup(response.text, "html.parser")
            command.instrumentResponse = str(data)
        except:
            command.instrumentResponse = "ERROR"

    #If there was an error in receiving the data
    except:
        ydata = [0]
        xdata = [0]

        try:
            urlToScrape = "http://flaskosa.herokuapp.com/cmd/" + command.command
            response = requests.get(urlToScrape)
            data = BeautifulSoup(response.text, "html.parser")
            command.instrumentResponse = str(data)
        #If there was an error in scraping the data from the website (i.e. command.command is of None type)
        except:
            command.instrumentResponse = "ERROR"
    return render(request,'forms/index.html', {
        "commands": command,
        "states": state,
        "xdata":xdata,
        "ydata":ydata
    })

#If the user 
@csrf_exempt
def inputCommand(request):
    content = request.POST["content"]
    #Determine what URL to get the data from
    urlToScrape = "http://flaskosa.herokuapp.com/cmd/" + content
    response = requests.get(urlToScrape)
    data = BeautifulSoup(response.text, "html.parser")
    command.command = content
    command.instrumentResponse = str(data)
    
    #Let's user update the state using commands
    if(content == "START"):
        state.state = "R"
    elif(content == "SINGLE"):
        state.state = "RO"
    else:
        state.state = "I"
    return HttpResponseRedirect("/")

# If the user hits one of the buttons
@csrf_exempt
def updateState(request):
    try:
        if(request.POST["dataGraph"] == "start"):
            state.state = "R"
        elif(request.POST["dataGraph"] == "single"):
            state.state = "RO"
        else:
            state.state = "I"
    #In case something messes up with request.POST
    except:
        state.state = "I"
    return HttpResponseRedirect("/")

@csrf_exempt
def displayGraph(request):
    if(state.state == "RO"):
        state.state == "I"      
    return HttpResponseRedirect('/')