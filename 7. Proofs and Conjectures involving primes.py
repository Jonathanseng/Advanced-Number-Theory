def is_prime(n):
  """Returns True if n is prime, False otherwise."""
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def twin_primes(n):
  """Returns a list of the twin primes from 2 to n."""
  twin_primes = []
  for i in range(2, n + 1):
    if is_prime(i) and is_prime(i + 2):
      twin_primes.append([i, i + 2])
  return twin_primes

def main():
  n = 100
  twin_primes = twin_primes(n)
  print(twin_primes)

if __name__ == "__main__":
  main()
