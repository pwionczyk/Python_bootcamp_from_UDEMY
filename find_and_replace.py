'''
find_and_replace('story.txt', 'Alice', 'Colt') 
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
'''

def find_and_replace(file_name, a, b):
  with open(file_name) as file:
    text = file.read()
  with open('new '+file_name, 'w') as file:
    file.write(b.join(text.split(a)))

find_and_replace('story.txt', 'Alice', 'Colt') 