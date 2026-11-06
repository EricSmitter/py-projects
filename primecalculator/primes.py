import itertools

known_primes = []

with open("log2.txt", "r") as f:
    known_primes = [line.strip() for line in f]

begin = known_primes[-1]
end = known_primes[-1] ** known_primes[-1]

for x in range(begin,end):
  x_root = int(x ** 0.5)
  for p in range(3, x_root, 2):
    if x % 2 ==0:
      break
    if x % p == 0:
      break
  else:
    print(f"Got another one: {x}")
    known_primes.append(x)
    with open("log2.txt", "w") as f:
      for x in known_primes:
        f.write(f"{x} \n")