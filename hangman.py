import random
from nltk.corpus import words

# holds matching letters
def placeholder(tstr, char, pos):
  ltstr = list(tstr)
  for i in pos:
    ltstr[i]=char
  res="".join(ltstr)
  return res

# finds position of letter in word
def charpos(word,char):
  pos = [] 
  for i in range(len(word)):
    if char == word[i]:
      pos.append(i)
  return pos

# read user input
def getuserinput(answord):
  while True:
    userip = input("Enter characters:")
    if userip == 'Guess Word':
      guessip = input("Enter Word:")
      if guessip == answord:
        print("You won!")
        exit()
      else:
        print("You lose ... the word was %s" % answord)
        exit()
    elif len(userip) != 1:
      print("Please enter single alphabet")
      continue
    elif userip.isalpha():
      return userip
    else:
      print("Please enter alphabet...")
      continue


def hangman(lives=8):
  
  answord = random.choice(word_list)
  tmpstr = ''
  for i in range(len(answord)):
    tmpstr = tmpstr+'_'
  # lets print number of letters in secret word that user has to guess
  print("Guess what is %s" % tmpstr)
  
  while lives > 0:
    userip=getuserinput(answord)
    if userip in answord:
      positions=charpos(answord, userip)
      tmpstr=placeholder(tmpstr, userip, positions)
      print("you got it right! - %s with %d lives left" % (tmpstr, lives))
      if tmpstr==answord:
        print('You won!  lives %d' % lives)
        return 
    else:
      lives=lives-1
      print("Letter not found!")
      print("%s and lives left %d" % (tmpstr, lives))
      continue
  print("Out of lives, game over! the word was %s" % answord)
  

word_list = words.words()


# main code to play

while True:
  print("Let's Play Hangman!")
  hangman(lives=8)
  playagain=input("Do you want to play again? Yes/No")
  if playagain=='Yes':
    continue
  else:
    break
