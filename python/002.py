cur = 2
prev = 1
sum = 0

while (cur < 4000000):
	if (cur % 2 == 0):
		sum += cur
	cur = cur + prev
	prev = cur - prev

print(sum)