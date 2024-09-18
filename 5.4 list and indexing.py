#define the lis
my_list=[1,2,3,4,5]
#move the last element to the first/front
my_list=[my_list[-1]]+my_list[:-1]
print("the rotated lis is :",my_list)