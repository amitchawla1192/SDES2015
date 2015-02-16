from gcd import gcd

def test_type():
	gcd(48,16)
	gcd(14.25,12)
def test_value():
	gcd(48,-16)
	gcd(-48,16)
#	print "All tests passed"

if __name__ == '__main__':
	test_type()
	test_value()
