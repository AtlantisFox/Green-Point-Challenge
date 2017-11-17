import random

values = list(range(10))

def random_choice():
	for i in range(10):
		print(random.choice(values))

def random_sample():
	for i in range(10):
		print(random.sample(values, i))

# random index

def random_shuffle():
	for i in range(10):
		random.shuffle(values)
		print(values)

def random_int():
	for i in range(10):
		print(random.randint(0, i))
		print(random.random())

# random n bit int
def random_nbit_int():
	print(random.getrandbits(233))

if __name__ == '__main__':
	random_choice()
	random_sample()
	random_shuffle()
	random_int()
	random_nbit_int()
