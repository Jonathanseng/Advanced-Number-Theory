def is_prime(n):
  """Returns True if n is prime, False otherwise."""
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def primes_and_composites(n):
  """Returns a list of the primes and composites from 2 to n."""
  primes = []
  composites = []
  for i in range(2, n + 1):
    if is_prime(i):
      primes.append(i)
    else:
      composites.append(i)
  return primes, composites

def main():
  n = 15
  primes, composites = primes_and_composites(n)
  print("Primes:", primes)
  print("Composites:", composites)

if __name__ == "__main__":
  main()
