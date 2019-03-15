#Remove all vowels from a string

def anti_vowel(text):
  phrase = ""
  for letter in text:
    for vowel in "aeiouAEIOU":
      if letter == vowel:
        letter = ""
      else:
        letter = letter
    phrase = phrase + letter
  return phrase
