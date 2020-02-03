'''
To return new copy of a list/array,
use silce style/operator ':'

'''
arrA=[1,2,3]
#concatation array
arrA+=[4,5]
arrB=arrA[:]
#This will take a referance
arrD=arrA
#This will take a new shalow copy
arrA[0]=4
print(arrB)
print(arrD)
# replace some values
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']
#>>> ['a', 'b', 'C', 'D', 'E', 'f', 'g']

#remove some value
letters[2:5] = []
#>>> ['a', 'b', 'f', 'g']

# clear the list by replacing all the elements with an empty list
letters[:] = []
 #>>> []
 #to-find-list-intersection
lstA= [1,2,3,4,5]
lstB= [1,2,3,4]
#new copy returnd
lstC= lstA and lstB
#>>> [1,2,3,4]
 #to-find-list--outer-intersection
lsA= [1,2,3,4,5]
lsB= [1,2,3,4]
lsC= [item for item in lsA if item not in lsB]
#>>> [5]
#or
lsC=set(lsA)-set(lsB)
#>>> {5}
#or
lsC =set(lsA) ^ set(lsB)
#>>> {5}

#set vs list: all set data memeber must be unique
ls=set([1,2,3,3])
print(ls)
#>>> {1, 2, 3}
#search in list
lst=[1,2,3,4,5,5]
nlst=[x for x in lst if x == 3]
print(nlst)

