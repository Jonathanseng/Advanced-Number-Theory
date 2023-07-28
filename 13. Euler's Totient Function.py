def euler_phi(n):
  """Returns the euler phi function for n."""
  phi = 1
  for i in range(2, n + 1):
    if gcd(i, n) == 1:
      phi += 1
  return phi

def main():
  n = 15
  print(euler_phi(n))

if __name__ == "__main__":
  main()
