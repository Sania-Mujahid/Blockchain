n=int(input("enter any number "))
i=2
prime=True
while i<n:
    if n%i==0:
          prime=False
    break
    i+=1
    if prime:
          print(n,'is prime')
else:
 print(n,'is not prime')