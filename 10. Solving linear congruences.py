def solve_linear_congruence(a, b, m):
  """Returns the solution to the linear congruence ax ≡ b (mod m)."""
  gcd, x, y = extended_gcd(a, m)
  if b % gcd != 0:
    return None
  else:
    return (x * b) % m

def extended_gcd(a, b):
  """Returns the extended Euclidean algorithm for a and b."""
  if b == 0:
    return (1, 0, a)
  else:
    (x, y, gcd) = extended_gcd(b, a % b)
    return (y, x - (a // b) * y, gcd)

def main():
  a = 7
  b = 11
  m = 15
  print(solve_linear_congruence(a, b, m))

if __name__ == "__main__":
  main()
