def wilson_theorem(p):
  """Returns True if p is a prime number, False otherwise."""
  if p == 1:
    return False
  else:
    return (p - 1) % p == (p - 1) ** (p - 2)

def main():
  p = 7
  print(wilson_theorem(p))

if __name__ == "__main__":
  main()
