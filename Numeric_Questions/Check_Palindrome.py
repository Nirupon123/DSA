n=1234
res=0
while n>0:
	rem=n%10
	res=res*10+rem
	n=n//10
#return n==res
if(n==res):
	print("Palindrome")
else:
    print("not a palindrome")