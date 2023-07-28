def hensel(f, p, a, d):
  """Returns the unique solution to f(x) ≡ 0 (mod p^d) using Hensel's Lemma."""
  if d == 0:
    return a
  else:
    x = hensel(f, p, a, d - 1)
    y = (x + p ** (d - 1)) // p
    return (y if f(y) % p == 0 else x)

def main():
  f = lambda x: x ** 3 - 2 * x + 1
  p = 7
  a = 2
  d = 2
  print(hensel(f, p, a, d))

if __name__ == "__main__":
  main()
