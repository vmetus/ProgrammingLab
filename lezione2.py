def sum_list(the_list):
 somma = 0
 for number in myList:
   somma += number

 return somma
  
myList = [1, 2, 3, 4, 5]
print ("somma della lista {}".format(sum_list(myList)))
