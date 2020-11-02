#!/usr/bin/env python3
import cgi
import csv
import json
import sys
from os import path
sys.path.insert(0, path.dirname(path.dirname(path.abspath(__file__))))
sys.path.insert(0, path.dirname(path.abspath(__file__)))

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

print("Content-Type: text/html; charset=utf-8")
print()

form = cgi.FieldStorage()

#print(form.keys())

modified = int(form["id"].value)

annotations = []
data = {
    "all": [],
    "rows": {},
}
try:
    with open('annotations.json') as f:
        data = json.load(f)
except:
    pass

all_annotations = json.loads(form["all_annotations"].value)
raw_annotations = json.loads(form["annotations"].value)
#eprint(raw_annotations)
data["rows"][str(modified)] = list(map(
    lambda x: list(map(
        lambda x: all_annotations.index(x),
        x
    )),
    raw_annotations
))
data["all"] = all_annotations

with open('annotations.json', 'w') as f:
    json.dump(data, f)

with open("last", "w") as f:
    f.write(str(modified))

print('<!doctype html><meta http-equiv="refresh" content="0;url=annotate.cgi?id=%s" />' % (modified + 1))
print('Changes saved. Redirecting to next response.')
