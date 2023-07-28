def chinese_remainder_theorem(a, m, n):
  """Returns the solution to the system of linear congruences ax ≡ b (mod m) for all b in n."""
  product = 1
  for i in range(len(n)):
    product *= m[i]
  result = 0
  for i in range(len(n)):
    inv = pow(m[i], -1, product)
    temp = (a[i] * product * inv) % product
    result += temp * n[i]
  return result % product

def main():
  a = [7, 11, 13]
  m = [15, 21, 23]
  n = [1, 2, 3]
  print(chinese_remainder_theorem(a, m, n))

if __name__ == "__main__":
  main()
