def difference_2_at_distance_1(array):
  """Returns a list of all pairs of elements in array such that the difference between them is 2 and the distance between them is 1."""
  result = []
  for i in range(len(array)):
    for j in range(i + 1, len(array)):
      if array[j] == array[i] + 2 and j - i == 1:
        result.append((i, j))
  return result

def main():
  array = [1, 3, 5, 7, 9]
  result = difference_2_at_distance_1(array)
  print(result)

if __name__ == "__main__":
  main()
