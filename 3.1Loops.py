#using while loop
n=int(input("enter the value of n ="))
sum=0
while n>0:
  sum=n+1
  n=n-1
print(f"sum is {sum}")
#using for loop
n=int(input("enter the value of n ="))
i=0
for i in range(1,n+1):
        sum=sum+1
print(f"sum of first natural numbers {n} is {sum}")