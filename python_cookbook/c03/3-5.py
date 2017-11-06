# u2fval 字节问题解决

import os 
import random

if __name__ == '__main__':
	data = os.urandom(128)
	int.from_bytes(data, 'little')
	int.from_bytes(data, 'big')

	x = random.randint(0,100)
	x.to_bytes(4, 'big')
	x.to_bytes(4, 'little')