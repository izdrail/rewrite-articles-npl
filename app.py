
import time
import sys
import os
import json
from flask import Flask, Request, Response
from text_rewrite import TextRewrite



@app.route('/')
def welcome():
	text = 'I love coding and creating software'
	new_sentence = TextRewrite(text).work()
    return new_sentence 

if __name__ == '__main__':
    app.run(debug=True)


