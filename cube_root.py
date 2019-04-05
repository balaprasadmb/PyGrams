def main():
    n = int(raw_input())
    for i in range(1, n/3):
		print i**3
		if(i**3 == n):
			print i
			break

main()
