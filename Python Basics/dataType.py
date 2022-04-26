x = 101
print(x)
def function():
	
	global x
	print(x)
	x = 'modified value'

	print(x)

function()
print(x)
del(x)
print(x)