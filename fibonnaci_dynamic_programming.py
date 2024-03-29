def fib1(n):
   global numCalls
   numCalls += 1
   print 'fib called with', n
   if n <= 1: return n
   else: return fib1(n-1) + fib1(n-2)
   
numCalls=0
n=6
res=fib1(n)
print 'fib of',n,'=',res,'numCalls = ',numCalls

#def fastFib(n, memo):
#   global numCalls
#   numCalls += 1
#   print 'fib called with', n
#   if not n in memo:
#      memo[n] = fastFib(n-1, memo) + fastFib(n-2, memo)
#     # print 'memo[n]',memo[n]
#   return memo[n]
#
#def fib(n):
#   memo = {0:0, 1:1}
#   return fastFib(n,memo)
#
##numCalls=0
##n=6
##res=fib(n)
##print 'fib of',n,'=',res,'numCalls = ',numCalls
#
#
def maxVal(w, v, i, aW):
   #w-weight list,v-values of list
   #i - lenght of the list.
   #aW - aviable weight
   #print 'maxVal called with:', i, aW
   global numCalls
   numCalls += 1
   if i == 0:
      if w[i] <= aW: return v[i]
      else: return 0
   without_i = maxVal(w, v, i-1, aW)#left branch of tree,dont take weight
   if w[i] > aW: return without_i
   else: with_i = v[i] + maxVal(w, v, i-1, aW - w[i]) #take weight (right branch of tree)
   return max(with_i, without_i)

def fastMaxVal(w, v, i, aW, m):
   global numCalls
   numCalls += 1
   try: return m[(i, aW)]
   except KeyError:
      if i == 0:
         if w[i] <= aW:
            m[(i, aW)] = v[i]
            return v[i]
      else:
         m[(i, aW)] = 0
         return 0
   without_i = fastMaxVal(w, v, i-1, aW, m)
   if w[i] > aW:
      m[(i, aW)] = without_i
      return without_i
   else: with_i = v[i] + fastMaxVal(w, v, i-1, aW - w[i], m)
   res = max(with_i, without_i)
   m[(i, aW)] = res
   return res

def maxVal0(w, v, i, aW):
   m = {}
   return fastMaxVal(w, v, i, aW, m)
   
maxWeight=5
w=[5,3,2,1]
v=[9,7,8,3]
numCalls=0
res=maxVal(w,v,len(v)-1,maxWeight)
print 'max val - ',res,' number of calls =',numCalls

res2=maxVal0(w,v,len(v)-1,maxWeight)
print 'max val fast comp. - ',res,' number of calls =',numCalls
