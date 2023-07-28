def ramanujan_congruence(n):
  """Returns the value of Ramanujan's famous (mod 5) congruence for n."""
  if n % 5 == 0:
    return 0
  elif n % 5 == 1:
    return 4
  elif n % 5 == 2:
    return 1
  elif n % 5 == 3:
    return -2
  else:
    return 3

def main():
  n = 10
  result = ramanujan_congruence(n)
  print(result)

if __name__ == "__main__":
  main()
