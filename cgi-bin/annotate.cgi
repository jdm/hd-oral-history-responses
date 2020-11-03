#!/usr/bin/env python3
import cgi
import csv
import json
import sys
from os import path
sys.path.insert(0, path.dirname(path.dirname(path.abspath(__file__))))
sys.path.insert(0, path.dirname(path.abspath(__file__)))

print("Content-Type: text/html; charset=utf-8")
print()

form = cgi.FieldStorage()
if "id" not in form:
    try:
        with open("last") as f:
            index = int(f.read())
    except:
        index = 1;
else:
    index = int(form["id"].value)

questions = []
answers = []
with open('responses.csv') as f:
    reader = csv.reader(f)
    for (i, row) in enumerate(reader):
        #print(i, index, row)
        if not questions:
            questions = row
        if i - 1 == index:
            answers = row
            break

# Format:
# {
#   all: [
#     "foo",
#     "bar",
#   ]
#   rows: {
#     "13": [[], [0], [1], [0,1]]
#   }
# }

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

allAnnotations = []
annotations = map(lambda _: "", answers)
try:
    with open('annotations.json') as f:
        data = json.load(f)
        allAnnotations = data["all"]
        row = data["rows"].get(str(index))
        if row:
            annotations = map(
                lambda v: ' '.join(
                    map(lambda x: allAnnotations[x], v)
                ),
                row
            )
except:
    pass

responses = zip(questions, answers, annotations)
#print(answers)
#print(list(responses))

def escape(s):
    return s.replace('"', '\\"').replace('\n', '<br>')#.replace("'", "\\'")

with open('classify_template.html') as f:
    contents = f.read()
    contents = contents.replace(
        "{{responses}}",
        ", ".join(map(lambda a: '["' + escape(a[0]) + '", "' + escape(a[1]) + '", "' + a[2] + '"]', responses)),
    )
    contents = contents.replace(
        "{{annotations}}",
        ", ".join(map(lambda a: '"' + a + '"', allAnnotations)),
    )
    contents = contents.replace("{{id}}", str(index))
    print(contents)
