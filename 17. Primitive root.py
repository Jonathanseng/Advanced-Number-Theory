def is_primitive_root(p, g):
  """Returns True if g is a primitive root of p, False otherwise."""
  if g == 0 or g == 1:
    return False
  else:
    for i in range(2, p):
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

if __name__ == "__main__":
  main()
