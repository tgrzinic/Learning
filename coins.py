import sys
def coins(V,Sum):
    min=[sys.maxint]*30
    min[0]=0
    n=len(V)
    i=1
    for i in range(Sum+1):
        for j in range(n):
            if(V[j]<=i and (min[i-V[j]]+1)<min[i]):
                #print 'Iteration j=',j,', V[j]=',V[j],'. i=',i,' min[i-V[j]]',min[i-V[j]]
                min[i]=min[i-V[j]]+1
    return min[Sum]
    
Sum=11
V=[1,3,5]
num_coins=coins(V,Sum)
print 'Minimm number of coins to get the sum of',Sum,' is ',num_coins
                                                                                                                                                                                                                                                                                                                                                                                     