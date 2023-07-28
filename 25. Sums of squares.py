def sums_of_squares(n):
  """Returns a list of all sums of squares up to n."""
  if n == 0:
    return [0]
  else:
    result = []
    for i in range(n + 1):
      for j in range(i + 1):
        if i * i + j * j <= n:
          result.append(i * i + j * j)
    return result

def main():
  n = 10
  result = sums_of_squares(n)
  print(result)

if __name__ == "__main__":
  main()
