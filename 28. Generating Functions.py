def generating_function(sequence):
  """Returns the generating function for the sequence."""
  result = 0
  for term in sequence:
    result += term * pow(x, len(sequence) - 1 - term)
  return result

def main():
  sequence = [1, 2, 3, 4]
  result = generating_function(sequence)
  print(result)

if __name__ == "__main__":
  main()
