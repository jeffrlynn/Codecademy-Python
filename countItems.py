#count the number of a chosen item in a list

def count(sequence, item):
  total = 0
  for thing in sequence:
    if thing == item:
      total += 1
  return total
