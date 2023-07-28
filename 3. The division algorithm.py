def division_algorithm(dividend, divisor):
  """Returns the quotient and remainder of the division of dividend by divisor."""
  quotient = 0
  remainder = dividend
  while remainder >= divisor:
    quotient += 1
    remainder -= divisor
  return quotient, remainder

def main():
  dividend = 10
  divisor = 3
  quotient, remainder = division_algorithm(dividend, divisor)
  print(f"The quotient is {quotient}")
  print(f"The remainder is {remainder}")

if __name__ == "__main__":
  main()
