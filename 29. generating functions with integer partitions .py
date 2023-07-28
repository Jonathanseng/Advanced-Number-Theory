def generating_function_for_integer_partitions(n):
  """Returns the generating function for the integer partitions of n."""
  result = 0
  for k in range(1, n + 1):
    result += pow(x, k) * sum([pow(x, i) for i in range(k)])
  return result

def main():
  n = 4
  result = generating_function_for_integer_partitions(n)
  print(result)

if __name__ == "__main__":
  main()
