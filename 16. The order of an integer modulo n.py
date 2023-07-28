def order(a, n):
  """Returns the order of a modulo n."""
  if a % n == 0:
    return 0
  else:
    o = 1
    while (a ** o) % n != 1:
      o += 1
    return o

def main():
  a = 2
  n = 10
  print(order(a, n))

if __name__ == "__main__":
  main()
