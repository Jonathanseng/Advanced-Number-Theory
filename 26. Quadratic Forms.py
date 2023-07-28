def representable(n, a, b, c):
  """Returns True if n is representable by the quadratic form ax^2 + bxy + cy^2, False otherwise."""
  if n < 0:
    return False
  else:
    result = 0
    for i in range(n + 1):
      for j in range(i + 1):
        result += (a * i * i + b * i * j + c * j * j)
    return result == n

def main():
  n = 10
  a = 1
  b = 2
  c = 3
  result = representable(n, a, b, c)
  print(result)

if __name__ == "__main__":
  main()
