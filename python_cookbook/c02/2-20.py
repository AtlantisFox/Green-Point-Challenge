def byte_operation():
	data = b'Hello World'
	data_str = 'Hello World'
	print(data[0:5])
	print(data.startswith(b'Hello'))
	data_str.startswith('Hello')
	data.split()
	data_str.split()
	data = bytearray(b'Hello World')
	data.startswith(b'Hello')
	data.split()

# 大多数情况下，文本字符串上的操作均可用于字节字符串

def index_text():
	a = 'Hello World'
	b = b'Hello World'
	print(a[0], b[0], a[0] == b[0])
	print('a length:{}, b length:{}'.format(len(a), len(b)))
	print(b.decode('ascii'))

if __name__ == '__main__':
	byte_operation()
	index_text()