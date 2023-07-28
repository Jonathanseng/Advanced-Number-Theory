def decimal_representation(n, base=10):
  """Returns the decimal representation of n in base base."""
  if n == 0:
    return "0"
  else:
    result = []
    while n > 0:
      remainder = n % base
      result.append(str(remainder))
      n //= base
    result.reverse()
    return "".join(result)

def main():
  n = 1234
  base = 2
  result = decimal_representation(n, base)
  print(result)

if __name__ == "__main__":
  main()
