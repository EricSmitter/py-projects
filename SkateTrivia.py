import random
import os
import time

def clear_output(): #Helper function to clear the output.
    os.system('cls' if os.name == 'nt' else 'clear')

q_lib = {1: 'What is the most common name for a 360 shuv-it with a kickflip?', 2: 'Who was the first skater to land a treflip down El Toro?', 3: 'Who invented the kickflip?', 4: 'Who was the first to land a 900 on vert in a comp?', 5: 'Who invented the Ollie?', 6: 'Which company’s motto was ‘Skate or Die’ when it was formed?', 7: 'Who produced the popular “Do a kickflip!” youtube series?', 8: 'Which spot is Aaron ‘Jaws’ Homoki famous for ollieing?', 9: 'What is a ‘Caballerial’?', 10: 'Who took gold in the 2024 Men’s Street Skating Olympics?'}

a_key = {1: 'Treflip', 2: 'Chris Joslin', 3: 'Rodney Mullen', 4: 'Tony Hawk', 5: 'Alan Gelfand', 6: 'Zero', 7: 'The Berrics', 8: 'Lyon 25', 9: 'Fakie 360 Ollie', 10: 'Yuto Horigome', }

choice_bank = {1: ["Three Flip", "360 Kickflip", "Circle Flip", "Three-shuv Flip"], 2: ["Tony Hawk", "Leticia Bufoni", "Adrien Bulard", "Nyjah Huston"], 3: ["Andy Anderson", "Steve Caballero", "Mike McGill","Tony Hawk"], 4: ["Bob Burnquist","Danny Way","Elliot Sloan","Tom Schaar"], 5: ["Rodney Mullen","Bam Margera","Daewon Song","Leticia Bufoni"], 6: ["Thrasher", "Baker", "Spitfire", "Bones"], 7: ["Eric Koston", "Powell-Peralta", "Sean Malto", "Santa Cruz Skateboards"], 8: ["Wallenberg", "El Toro", "Hollywood High", "Canadian Embassy"], 9: ["360 Ollie", "Fakie 180 Ollie", "Nose Grab Aerial", "Fakie Treflip"], 10: ["Keegan Palmer", "Jagger Eaton", "Nyjah Huston", "Tom Schaar"]}


class Question:
  def __init__(self, qnum): #Index is the question number, should be an integer 1-10
    self.qnum = qnum
    self.qtext = q_lib[qnum] #Map to the q_lib dictionary with questions in it.
    self.__ans = a_key[self.qnum]
    self.__choices = choice_bank[self.qnum]
  def get_ans(self):
    return self.__ans
  def get_choices(self):
    return self.__choices
  def build_output(self):
    #choices = self.get_choices() #create a local copy of the choices list
    choices = list(self.get_choices()) #The above was causing an alias crash as it wasn't actually copying the list but modifying it in real time
    choices.remove(random.choice(choices)) #Weird fix to get the choice list down to 4 (4 dummy choices + 1 right ans), del a dummy choice before appending the right answer
    choices.append(self.get_ans()) #Add the correct answer to the list of wrong choices
    lines = ["a","b","c","d"] #Define a list that acts as place holders for the multi-choice options
    output = {}
    for n in lines: #Loop through the lines placeholder list
      current = random.choice(choices) #Create a local var at random from our local list of choices
      output[n] = current
      choices.remove(current) #Remove the last printed options so no repeats
    return output

class Player:
  def __init__(self,name):
    self.name = name
    self.__score = 0
  def give_point(self):
    self.__score += 1
    return self.__score
  def get_total(self):
    #total = self.__score
    return self.__score

#Define all our question objects
def questions_init():
  question_list = []
  for k in q_lib.keys():
    question_list.append(Question(k))
  return question_list



#def init_players():
#  print("Enter each player's name below: ")
#  p1 = player(input("Player 1: "))
#  p2 = player(input("Player 2: "))

def ask_question(qn,player):
  print(f"{player.name}, you're up!")
  time.sleep(0.3)
  currentQ = qn.build_output() #Get a local copy of the build_output
  print(qn.qtext) #print the question
  for k,v in currentQ.items(): #Loop through the dict for printing
    print(f"{k}) {v}")

  while True: #Nested while loop with a try/except to filter bad answers
    response = input("Your answer: ") #Get an answer from the player
    try:
      if currentQ[response] == qn.get_ans(): #Check the answer
        print("Correct")
        player.give_point()
      else:
        print("Wrong answer forehead")
      break
    except KeyError:
      print("invalid response")

def add_players():
  print("Add players (type 'done' when done)")
  print("------------------")
  players = [] #Create a blank list to receive player names
  n = 1 #Init a counter
  while True:
    name = input(f"Player{n}: ") #Set name to the player name
    if name == 'done': #Check if done
      break
    players.append(Player(name)) #make the list a list of player objects
    n += 1
  clear_output()
  return players

def show_scores(players):
  clear_output()
  print("Here's the final score: ")
  for p in players: #Loop through all player objects
    print(f"{p.name}: {p.get_total()} points")


def main():
  print("Welcome to SKATEBOARD TRIVIA!")
  players = add_players() #Create a player list
  q_numbers = list(questions_init())
  while (q_range := int(input("How many questions each? "))) > (len(q_numbers) // len(players)): #Here I borrowed from Zach's code and added a check to divide the question count by the
    print("Sorry, only 10 questions in the bank!")
  clear_output()
  for n in range(0,q_range):
    #q_numbers = [q1,q2,q3] #Move this outside the loop.
    #del q_numbers[question]
    for p in players:
      question = random.choice(q_numbers) #Define the current question as a random choice
      ask_question(question, p) #ask the question
      input("Press Enter to continue")
      clear_output() #Reset the output
      q_numbers.remove(question)#Remove that option from the pool
  show_scores(players)



main()
