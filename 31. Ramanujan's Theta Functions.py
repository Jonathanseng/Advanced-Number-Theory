def theta_function(n, p):
  """Returns Ramanujan's theta function theta_n(p)."""
  result = 0
  for k in range(1, p + 1):
    result += pow(-1, k) * pow(k, n) / (k * (k + 1))
  return result

def main():
  n = 4
  p = 5
  result = theta_function(n, p)
  print(result)

if __name__ == "__main__":
  main()
