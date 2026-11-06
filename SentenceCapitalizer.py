punc = ['!','.','?']

def capitalize(sentence):
  new_sentence = "" #create a blank string and we can append each letter to
  #for x in sentence: #iterate through each character in the string
  for i, x in enumerate(sentence): #Okay had to change up a bit, now I get "i" as the position and "x" as the character
    cap_next = False
    if i == 0:
      cap_next = True #If we're in the first position, then cap
    elif sentence[i-1] in punc: #If the character behind "i" is in our punctuation list
      cap_next = True #Then set the flag true
    elif sentence[i-1] == " ": #If the previous character is a space,
      if sentence[i-2] in punc: #Check if the character before that is a punction mark
        cap_next = True #If it is, then we'll capitalize it
      elif sentence[i-2] == " ": #Same test as above, looking back another space
        if sentence[i-3] in punc:
          cap_next = True
    if cap_next == True: #If one of the tests indicates that the character should be capital, then the flag would be true
      new_sentence += x.upper() #Append that character as an upper case letter
    else:
      new_sentence += x #If the flag is false, then append the character as is
  return new_sentence #Return the new string / print to screen

capitalize(input("type a sentence: ")) #Call the function with the argument being input options.
