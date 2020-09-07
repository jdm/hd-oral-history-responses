#!/usr/bin/env python3
import sys
from os import path
sys.path.insert(0, path.dirname(path.dirname(path.abspath(__file__))))
sys.path.insert(0, path.dirname(path.abspath(__file__)))
from random_response import response
print("Content-Type: text/html; charset=utf-8")
print()
(q, a) = response('responses.csv')
with open('template.html') as f:
    print(f.read().replace("{{question}}", q).replace("{{answer}}", a))
