def main():
  n=input()
  m=input()
  primes = []
  for i in range(n,m):
    if i > 1:
      is_prime = True
      for j in range(2,i):
        if i % j == 0:
          is_prime = False
          break
        else:
          is_prime = True
      if is_prime:
        primes.append(i)
  print len(primes)
main()
