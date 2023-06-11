import os
import re
import json
import textwrap

#################################################
###                                           ###
###  Functions                                ###
###                                           ###
#################################################


def readJson():
  ''' Reads in the story from a json file '''
  # Opens the story jason file as in read mode and calls it my file
  with open('story.json', 'r') as myfile:
    #reads my file into a variable called data
    data = myfile.read()
  
  # converts the json into a python dictionary
  story = json.loads(data)
  return story


def printWrappedText(text):
  ''' Makes sure the text that is printed out is wraped for the consles width '''
  # Works out the size of the terminal 
  size = os.get_terminal_size()
  # Makes sure that the text dose not have half words go of to the text line
  wrapped = textwrap.wrap(text, width=size.columns)
  for line in wrapped:
    print(line)


def askUsername():
  ''' this asks your username and gives character size and unwanted character use limits'''
  # Starts the while loop until we have a valid username
  username = None
  while username == None:
    tmp = input("what is your username?"
                "\n"
                "").strip()
    # Use a regular experestion to make sure no bad character are entered
    regexp = re.compile(".*[\.\$#].*")
    if regexp.match(tmp):
      print("ERROR contains unwanted symbols (.*[\.\$#].*) ")
      continue
    # Checks to see if the username has the right amout of characters 
    if len(tmp) > 16 or len(tmp) < 3:
      print("incorrect character amount 3 to 16 characters only")
      continue
    # Checks to see if the user is happy with their username 
    uncheck = input("Do you want your username to be " + tmp + "? "
                    "\n"
                    "Y)Yes"
                    "\n"
                    "N)No"
                    "\n").upper()

    if uncheck == "N" or uncheck == "NO":
      continue
    elif uncheck == "Y" or uncheck == "YES":
      # Sets your username variable and ends loop only if you have passed all the checks 
      username = tmp
    else:
      print("Sorry thats not a vaild anwser so we will asume you typed N")
      continue
  return username


#################################################
###                                           ###
###  Game Initialization                      ###
###                                           ###
#################################################
state = "001Q1"
story = readJson()
username = askUsername()

# Welcome the player
printWrappedText("Hi " + username + " I hope your doing great today,")
printWrappedText("lets get to asking you a few questions shall we.")

#################################################
###                                           ###
###  Game Loop Below This                     ###
###                                           ###
#################################################

# The game loops till you reach the end state
while state != "end":
  current_question = story[state]

  print()
  printWrappedText(current_question["question"])
  answers = current_question["answers"]
  #loop through and print out all the answers
  for key in answers.keys():
    printWrappedText(" " + key + ") " + answers[key]["text"])
  #getting the users input
  user_input = input("> ").upper()
  #checking that the user has made a valid input
  if user_input in answers:
    state = answers[user_input]["next"]
  else:
    print("Error, try again")
    continue
