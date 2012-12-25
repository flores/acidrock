#!/usr/bin/env python

import json
import math
from flask import Flask

def co2(kh,ph):
  return round(3 * kh * 10**( 7 - ph ), 1)

app = Flask(__name__)
@app.route('/khph')

def kh_ph_range():
  results = []
  dataset = {}
  for k in range(10, 100):
    kh = round(k * 0.1, 1)
    #print "k is %d" % k
    for p in range(50, 80):
      #print p
      ph = round(p * 0.1, 1)
      dataset['kh'] = kh
      dataset['ph'] = ph 
      dataset['co2'] = co2(kh,ph)
      results.append(dataset)
      # i suck
      dataset = {}
  return json.dumps(results)

@app.route('/kh/<khvalue>/ph/<phvalue>/')

def kh_ph_known(khvalue,phvalue):
  kh = round(float(khvalue),2)
  ph = round(float(phvalue),2)
  return co2(kh,ph)

app.run(host='0.0.0.0',debug=True)
