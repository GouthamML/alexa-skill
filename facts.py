from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode
import random

app = Flask(__name__)
ask = Ask(app, "/fact")

@app.route('/')
def homepage():
    return 'hello world skill running perfectly fine :)'

def getfact():
    facts = [
    'first christmas fact', 
    'second christmas fact', 
    'third christmas fact', 
    'fourth christmas fact', 
    'five christmas fact', 
    'six christmas fact', 
    'seven christmas fact', 
    'eight christmas fact', 
    'nine christmas fact', 
    'ten christmas fact']
    
    return random.choice(facts)

@ask.launch
def launch():
    fact = getfact()
    response = fact + '...........Do you want more?'
    return question(response)

@ask.intent('YesIntent')
def yesIntent():
    fact = getfact()
    response = fact + '...........Do you want more?'
    return question(response)

@ask.intent('NoIntent')
def noIntent():
    response = 'Okay...hmmm...Bye'
    return statement(response)

@ask.intent('AMAZON.HelpIntent')
def help():
    response = 'This skill tell you facts about christmas!'
    return question(response)

if __name__ =='__main__':
    app.run(debug=True)