""""Given an integer, , perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird"""

n = int(input())
if n%2==1:
    print("Weird")    
elif n%2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n%2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")
	
	
# To compute the square of each number that falls below in N	
n = int(input())
if 1 <= n <=20:
    for i in range(n):
        print(i**2)
		
# leap year function
def is_leap(year):
    leap = False   
    if (year >= 1900 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        leap = True    
    return leap
year = int(input())
print(is_leap(year))

# printing numbers in a sequence without using string function
num = int(input("Enter number: "))
for i in range(1, num+1):
    print(i, end='')
	
#If set  is subset of set , print True.
#If set  is not a subset of set , print False.


# to find if A is superset of multiple sets
A = set(input().split())
n = int(input())
flag = True
for i in range(0,n): 
    B = set(input().split())
    flag = A.issuperset(B)
    if(flag == False):
        break
print(flag)
	
