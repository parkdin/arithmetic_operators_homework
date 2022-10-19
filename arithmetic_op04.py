#Create a variable called 'number' and assign it the three-digit number.
number = 125
#Find the 'number' first digit and assign to x1.
x1 = number%10
print(x1)
#Find the 'number' second digit and assign to x2.
number = number//10
x2 = number%10
#Find the 'number' third digit and assign to x3.
number = number//10
x3 = number%10
#Create a variable called 'answer' and assign it the sum of the three digits.
answer = x1+x2+x3
#print the sum of the three digits.
print(answer)