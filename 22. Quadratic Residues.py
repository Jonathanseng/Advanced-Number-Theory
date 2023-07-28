def is_quadratic_residue(a, p):
  """Returns True if a is a quadratic residue modulo p, False otherwise."""
  if a == 0:
    return True
  else:
    return pow(a, (p - 1) // 2, p) == 1

def main():
  p = 7
  a = 2
  result = is_quadratic_residue(a, p)
  print(result)

if __name__ == "__main__":
  main()
