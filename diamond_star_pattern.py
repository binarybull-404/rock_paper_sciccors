'''

***
* *
***

*****
** **
*   *
** **
*****

'''

def oddn(msg):
    ans=int(input(msg))
    while ans%2==0:
        print('Input ODD NUMBER ONLY for this pattern !')
        ans=int(input(msg))
    return(ans)

while True:
    try:
        n=oddn("Number of pattern u want? (Odd number only) : ")
        break

    except ValueError:
        print("Enter Valid Numerical Value! ")
        


gaps=" "
z=n//2
pattern=input('Symbol of Pattern u want? : ')

print(n*pattern)

for i in range(1,z+1):
    gaps=" "*(2*i-1)
    tempgaps=(z+1-i)*pattern
    print(tempgaps+gaps+tempgaps)


for j in range(z-1,0,-1):
    gaps=" "*(2*j-1)
    tempgaps=(z+1-j)*pattern
    print(tempgaps+gaps+tempgaps)

print(n*pattern)

