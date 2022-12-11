# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 13:45:14 2022

@author: jainp
"""


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import os
import pandas as pd


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')
