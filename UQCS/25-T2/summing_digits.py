def sum_digits(num: int) -> int:
	num = num
	sum = 0
	while num >= 10:
		sum = sum + num % 10
		num = num // 10
	sum = sum + num
	return sum

if __name__ == "__main__":
	while True:
		num = int(input())
		if num == 0:
			break
		while num >= 9:
			num = sum_digits(num)
		print(f"{num}")
