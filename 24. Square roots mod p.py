def modular_sqrt(a, p):
  """Returns a quadratic residue of 'a' modulo 'p', or None if no such residue exists."""
  if a % p == 0:
    return 0
  else:
    g = pow(a, (p - 1) // 2, p)
    if g == 1:
      return g
    else:
      for i in range(2, p):
        if (g * i) % p == 1:
          return i
    return None

def main():
  p = 7
  a = 2
  result = modular_sqrt(a, p)
  print(result)

if __name__ == "__main__":
  main()
