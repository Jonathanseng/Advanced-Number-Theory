def quadratic_reciprocity(a, p):
  """Returns True if the congruence ax^2 ≡ 1 (mod p) has a solution, False otherwise."""
  if a == 0:
    return True
  elif p == 2:
    return True
  elif p % 4 == 1:
    return a % 2 == 1
  else:
    return not quadratic_reciprocity(p, a)

def main():
  p = 7
  a = 2
  result = quadratic_reciprocity(a, p)
  print(result)

if __name__ == "__main__":
  main()
