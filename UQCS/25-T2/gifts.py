if __name__ == "__main__":
	while True:
		# parse whole block at once
		try:
			num_names = int(input())
		except:
			break
		names = input().split(' ')
		people = {}
		for _ in range(num_names):
			line = input().split(' ')
			name = line[0]
			giving = int(line[1])
			num = int(line[2])
			names = line[3:]
			people[name] = { "giving": giving, "num_names": num, "names": names, "receiving": 0, "leftover": 0 }
		for current_name, person in people.items():
			each = person["giving"] // person["num_names"]
			person["leftover"] = person["giving"] % person["num_names"]
			for name in person["names"]:
				people[name]["receiving"] += each
		for name in names:
			net = people[name]["receiving"] - people[name]["giving"] + people[name]["leftover"]
			print(f"{name} {net}")
		print(people)
