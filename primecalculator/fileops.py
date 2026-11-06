import itertools

known_primes = []

for x in itertools.count(start=2, step=1):
  for p in range(2, x):
    if x % p == 0:
      break
  else:
    print(f"Got another one: {x}")
    known_primes.append(x)
    with open("log.txt", "w") as f:
      for x in known_primes:
        f.write(f"{x} \n")