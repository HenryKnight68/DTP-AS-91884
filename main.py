import os
import json


def readJson():
  with open('story.json', 'r') as myfile:
    data = myfile.read()

  # parse file
  story = json.loads(data)
  return story


state = "start"
story = readJson()

while state != "end":
  # print(story[state])
  currentState = story[state]

  print()
  print(currentState["question"])
  answers = currentState["answers"]
  for key in answers.keys():
    print(" " + key + ") " + answers[key]["text"])

  a = input("> ").upper()
  if a in answers:
    #print(answers[a])
    state = answers[a]["next"]
  else:
    print("Error, try again")
    continue
