print(type(2+3))
print(type(6/2 ))
print(type(2 != 3))
print(2+3)
print(len(["abc", 2]))
a = 2
b=3
c="abc"
print(a)
print(a,b,c)
print(a,b,c,sep="")
print(c*(a-b))
d=c.find("b")
print(d)
print(d and b)
print(d==True)
e=str(a)+str(b)+str(c)+str(d)
print(e)

#check if number is odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
#practice check if number is odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

#sum of first N numbers
n = int(input("Enter a positive integer: "))
total = 0
i = 1

while i <= n:
    total += i
    i += 1

print(f"The sum of the first {n} natural numbers is {total}.")


#check if text is a palyndrome
text = input("Enter a string: ").lower().replace(" ", "")
if text == text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")