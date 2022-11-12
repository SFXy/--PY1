from pprint import pprint
n = 15
pprint([{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(0, n + 1)])
