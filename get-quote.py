import random
def primary():
   

  f = open("quotes.txt")
  quotes = f.readlines()
  newlist = []
  for i in quotes:
    newlist.append(i.rstrip('\n'))
  f.close()
  last = 13
  rnd = random.randint(0, last)
  print(newlist[rnd])

if __name__== "__main__":
  primary()
