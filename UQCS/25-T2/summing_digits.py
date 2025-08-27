
def sum_digits(num: int) -> int:
	sum = 0
	for char in str(num):
		sum  = sum + int(char)
	return sum

while True:
	num = int(input())
	if num == 0:
		break
	while num >= 9:
		num = sum_digits(num)
	print(f"{num}")
