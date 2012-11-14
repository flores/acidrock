#!/usr/bin/env python

import json
import math
from flask import Flask

def co2(kh,ph)
  round(3 * kh * 10**(7-ph), 1)

app = Flask(__name__)
@app.route('/khph')

def khph():
  ph = [round(x * 0.1, 1) for x in range(50, 80)]
  kh = range(1, 10)

  results = []
  dataset = {}
  for k in kh:
    dataset['kh'] = k
    for p in ph:
      dataset[p] = co2(k,p)
    results.append(dataset)
  return json.dumps(results)

@app.route('/kh/<kh>')
  ph = [round(x * 0.1, 1) for x in range(50, 80)]
  dataset = {}
  results = []
  for p in ph:
    dataset[p] = co2(kh,p)
  results.append(dataset)
  return json.dumps(results)

app.run(debug=True)
