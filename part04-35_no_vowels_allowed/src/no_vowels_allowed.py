# Write your solution her'

def no_vowels(string):
  vowels =['a','e','i','o','u']
  for vowel in vowels:
    string = string.replace(vowel,'')
  return string