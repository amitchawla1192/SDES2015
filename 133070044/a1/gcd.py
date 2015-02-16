#Let us start with writing a Test Code for GCD
def gcd(a,b):
	allowed = [int,long]
	if ((type(a) not in allowed) or (type(b) not in allowed)):
		raise TypeError ("Either of input is not int or long")
	if ((a < 0) or (b<0)):
		raise ValueError ("Either of the inputs is negative")
	if a == 0:
		return b
	while b != 0:
		if a > b:
			a = a - b
		else:
			b = b-a
	return a



def test_gcd():
	assert gcd(48, 64) == 16
	assert gcd(15,92) == 3
	assert gcd(-12,42)==7
	assert gcd(12.35,15)==8
#	print "All tests passed"


if __name__ == "__main__":
	test_gcd()
