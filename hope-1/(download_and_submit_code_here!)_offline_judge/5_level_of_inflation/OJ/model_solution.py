def take_difference(tup,i=0):
  # print(tup)
  if len(tup) == 2 and tup[0]!=tup[1]: return -1
  if len(set(tup)) == 1: return i
  a = tuple(tup[i-1]-tup[i] for i in range(1,len(tup)))
  return take_difference(a,i+1)

def level_of_inflation(tup):
  depth = take_difference(tup)
  if depth==-1: return "I bite my tongue, it's a bad habit."
  elif depth==0: return "There is no inflation right now"
  else:
    return "There is a constant (but not zero) " + "rate of "*(depth-1) + "inflation right now"
