def euler_phi(n):
  """Returns the euler phi function for n."""
  phi = 1
  for i in range(2, n + 1):
    if gcd(i, n) == 1:
      phi += 1
  return phi

def euler_theorem(a, n):
  """Returns the solution to the linear congruence ax ≡ 1 (mod n) using Euler's Theorem."""
  phi = euler_phi(n)
  return (a ** (phi - 1)) % n

def main():
  a = 7
  n = 15
  print(euler_theorem(a, n))

if __name__ == "__main__":
  main()
