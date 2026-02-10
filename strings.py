name = "avx"
st = '''🇮🇳 India – T20 World Cup 2026 Squad

Captain: Suryakumar Yadav
Wicket-keepers: Sanju Samson, Ishan Kishan
Batsmen: Suryakumar Yadav (c), Tilak Varma, Rinku Singh
All-rounders: Hardik Pandya, Axar Patel, Washington Sundar, Shivam Dube, Abhishek Sharma
Bowlers: Arshdeep Singh, Jasprit Bumrah, Mohammed Siraj, Kuldeep Yadav, Varun Chakaravarthy'''
print(st)
print(name[0])
print(name[2])
# print(name[4])#Returns index error 

#lopping through the strings
for character in name:
  print(character)
for character in st:
  print(character)
'''String slicing and operations'''
z = "aryan,aakash"
print(z[0:5])
print(len(z))
print(z[0:-3]) 

# String are immutable
# z[0] = "A" # This will give an error because we cannot change the value of a string
a = "arYan! !!!!!!!!!!!!!!"
print(a)
print(a.upper()) # This will print the string in uppercase
print(a.lower()) # This will print the string in lowercase
print(a.rstrip("!")) # This will remove the exclamation marks from the right side of the string
print(a.replace("arYan","Aakash")) # This will replace "arYan" with "Aakash" in the string
print(a.split(" ")) # This will split the string into a list of strings based on the exclamation marks
print(a.endswith("!")) # This will check if the string ends with an exclamation mark
print(a.startswith("arYan")) # This will check if the string starts with "arYan
