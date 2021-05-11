import random

def main():

  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.read().splitlines()
  f.close()

  last = len(quotes) - 1
  rnd = random.randint(0, last)
  print(quotes[rnd])
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
  main()
