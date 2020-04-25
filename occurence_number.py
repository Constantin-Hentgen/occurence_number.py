liste = [0,1,2,3,4,5,6,7,8,9,0,0,0,0,0,0,0,0,0]
number = 0
search = int(input('Enter a value : '))
counter = 0

for i in range(0,len(liste)):
    if liste[i] == search:
        counter += 1
             
print('There is ', counter, ' times "', search, '"')
