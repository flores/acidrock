#!/usr/bin/env python

import json
import math
from flask import Flask

def co2(kh,ph):
  return round(3 * kh * 10**(7-ph), 1)

app = Flask(__name__)
@app.route('/khph')

def khph():
  results = []
  dataset = {}
  for k in range(1, 10):
    #print "k is %d" % k
    for p in range(50, 80):
      #print p
      ph = round(p * 0.1, 1)
      dataset['kh'] = k
      dataset['ph'] = ph 
      dataset['co2'] = co2(k,ph)
      results.append(dataset)
      # i suck
      dataset = {}
  return json.dumps(results)

@app.route('/kh/<value>')

def fromkh(value):
  kh = float(value)
  ph = [round(x * 0.1, 1) for x in range(50, 80)]
  dataset = {}
  results = []
  for p in ph:
    dataset[p] = co2(kh,p)
  results.append(dataset)
  return json.dumps(results)

app.run(host='0.0.0.0',debug=True)
