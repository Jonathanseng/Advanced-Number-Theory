import math

def discrete_log(g, x, p):
  """Returns the discrete logarithm of x to the base g modulo p."""
  if x == 0:
    return 0
  else:
    order = math.gcd(p - 1, g - 1)
    for i in range(1, order + 1):
      if (g ** i) % p == x:
        return i
    return None

def main():
  p = 11
  g = 2
  x = 8
  result = discrete_log(g, x, p)
  print(result)

if __name__ == "__main__":
  main()
