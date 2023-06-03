import os
import re
import json

#################################################
###                                           ###
###  Functions                                ###
###                                           ###
#################################################


def readJson():
  with open('story.json', 'r') as myfile:
    data = myfile.read()

  # parse file
  story = json.loads(data)
  return story


#################################################
###                                           ###
###  Game Initialization                      ###
###                                           ###
#################################################

state = "001Q1"
story = readJson()

username = None
while username == None:
  tmp = input("what is your username?"
              "\n"
              "").strip()
  regexp = re.compile(".*[\.\$#].*")
  if regexp.match(tmp) or tmp == "":
    print("ERROR contains undetectable symbols (.*[\.\$#].*) ")
    continue
  uncheck = input("Do you want your username to be " + tmp + "? "
  "\n"
  "Y)Yes"
  "\n"
  "N)No"
  "\n").upper()
  
  if uncheck == "N" or uncheck == "NO":
    continue
  elif uncheck == "Y" or uncheck == "YES":
    username = tmp
  else:
    print("Sorry thats not a vaild anwser so we will asume you typed N")
    continue




# Username()

  
print("Hi " + username + " I hope your doing great today,"
      "\n"
"lets get to asking you a few questions shall we.")
#################################################
###                                           ###
###  Game Loop Below This                     ###
###                                           ###
#################################################

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
