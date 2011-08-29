def bubbleSort(L):
   for j in range(len(L)):
      print L
      for i in range(len(L) - 1):
         if L[i] > L[i+1]:
            temp = L[i]
            L[i] = L[i+1]
            L[i+1] = temp

def bubbleSort2(L):
   swapped = True
   while swapped:
      swapped = False
      print L
      for i in range(len(L) - 1):
         if L[i] > L[i+1]:
         temp = L[i]
         L[i] = L[i+1]
         L[i+1] = temp
         swapped = True

def testBubbleSort():
   test1 = [1,6,3,4,5,2]
   raw_input('run bubble
   bubbleSort(test1)
   test2 = [6,1,2,3,4,5]
   raw_input('run bubble
   bubbleSort(test2)
   test3 = [6,5,4,3,2,1]
   raw_input('run bubble
   bubbleSort(test3)
   test4 = [1,2,3,4,5,6]
   raw_input('run bubble
   bubbleSort(test4)


