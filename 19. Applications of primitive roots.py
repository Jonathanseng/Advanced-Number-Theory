import math

def is_primitive_root(p, g):
  """Returns True if g is a primitive root of p, False otherwise."""
  if g == 0 or g == 1:
    return False
  else:
    order = math.gcd(p - 1, g - 1)
    for i in range(2, order + 1):
      if (g ** i) % p == 1:
        return False
    return True

def find_primitive_roots(p):
  """Returns a list of all primitive roots of p."""
  pr = []
  for i in range(2, p):
    if is_primitive_root(p, i):
      pr.append(i)
  return pr

def main():
  p = 11
  pr = find_primitive_roots(p)
  print(pr)

  # Use primitive roots to generate a sequence of pseudorandom numbers
  sequence = []
  g = pr[0]
  for i in range(10):
    sequence.append(g ** i % p)
  print(sequence)

if __name__ == "__main__":
  main()
