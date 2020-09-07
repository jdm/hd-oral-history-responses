import csv
from random import choice

AGE = 2
FIRST_FANDOM = 3
FIRST_HARRY_POTTER = 4
FIRST_HARRY_DRACO = 5
WHERE_PARTICIPATED = 6
WHERE_ELSE = 7
WHY_HARRY_DRACO = 8
HIGHLIGHTS = 9
WAYS_PARTICIPATE = 10
ENJOY_OR_NOT = 11
PARTICIPATION_CHANGED = 12
FANWORKS = 13
CREATORS = 14

def response(fname):
    with open(fname) as f:
        reader = csv.reader(f)
        questions = []
        responses = []
        indexes = [
            AGE, FIRST_FANDOM, FIRST_HARRY_POTTER, FIRST_HARRY_DRACO,
            WHERE_PARTICIPATED, WHERE_ELSE, WHY_HARRY_DRACO, HIGHLIGHTS,
            WAYS_PARTICIPATE, ENJOY_OR_NOT, PARTICIPATION_CHANGED,
            FANWORKS, CREATORS,
        ]
        for row in reader:
            if not questions:
                questions = row
                continue
            if row[-3] == "Yes":
                responses.append(row)
        
        question = choice(indexes)
        filtered_responses = list(filter(lambda row: row[question], responses))
        answer = choice(filtered_responses)
        return (questions[question], answer[question])

if __name__ == "__main__":
    (question, answer) = response('responses.csv')
    print(question)
    print(answer)
