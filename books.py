books = {
   'King': 'It',
   'London': 'White Fang',
   'Carroll': 'Alice in Wonderland',
   'Lindgren': 'Karlsson on the Roof'}

#add 2 titles
books['Defoe']='The Adventures of Robinson Crusoe'
books['Dumas']='The Count of Monte Cristo'
#remove S. King
del books['King']
print(books.keys())
print(books.values())
