#Returns the reverse of your input

def reverse(text):
  word = ""
  l = len(text) - 1
  while l >= 0:
    word = word + word[l]
    l = l - 1
  return word
