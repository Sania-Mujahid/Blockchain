#initial list
ids=[4353,2314,2956,3382,9362,3900]
#1.remove 3382 from list
ids.remove(3382)
#2.get the index of 9362
index=ids.index(9362)
print("the index of 9362 is :",index)
#3.insert 4499 in the list after 9362
ids.insert(index+1,4499)
#4.extend the list by adding [5566,1830] to it
ids.extend([5566,1830])
#5.reverse the list
ids.reverse()
#6.sort the index
ids.sort()
#final output of the list
print("the final output is :",ids)

