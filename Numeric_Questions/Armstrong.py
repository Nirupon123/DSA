n=153
total=0
nod=len(str(n))
while n>0:
	last_digit=n%10
	total=total+last_digit**nod
	n=n//10
if n==total:
	print("armstrong")
else:
	print("not a armstrong")