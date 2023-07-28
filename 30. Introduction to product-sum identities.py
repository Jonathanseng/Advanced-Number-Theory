def product_sum_identity(n):
  """Returns the product-sum identity for n."""
  result = 0
  for k in range(1, n + 1):
    result += (k * (k + 1)) / 2 * pow(k, n - k)
  return result

def main():
  n = 4
  result = product_sum_identity(n)
  print(result)

if __name__ == "__main__":
  main()
