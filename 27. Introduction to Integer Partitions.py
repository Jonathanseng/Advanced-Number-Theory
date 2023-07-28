def integer_partitions(n):
  """Returns a list of all integer partitions of n."""
  if n == 0:
    return [[]]
  else:
    result = []
    for i in range(1, n + 1):
      for partition in integer_partitions(n - i):
        result.append([i] + partition)
    return result

def main():
  n = 4
  result = integer_partitions(n)
  print(result)

if __name__ == "__main__":
  main()
