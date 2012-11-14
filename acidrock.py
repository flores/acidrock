#!/usr/bin/env python

import json
import math
from flask import Flask

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
      co2 = round(3 * k * 10**(7-p), 1)
      dataset[p] = co2
    results.append(dataset)
  return json.dumps(results)

app.run(debug=True)
