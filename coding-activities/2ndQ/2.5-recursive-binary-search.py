# needle - the item to search for in the collection
# haystack - the collection of items
# NOTE: assume the haystack is ALWAYS sorted, no need to sort it yourself

# the binary search function to be exposed publicly
# returns the index if needle is found, returns None if not found
def binary_search(needle, haystack):
    if len(haystack) == 0:
        return None;
    else:
        return _binary_search_rec(needle, haystack, 0, len(haystack) - 1)

# the recursive binary search function (not public)
# returns the index if needle is found, returns None if not found
def _binary_search_rec(needle, haystack, start_index, end_index):
    # IMPLEMENT!
    if start_index > end_index:
      return None
    else:
      mid_index = (start_index + end_index) // 2
      if needle == haystack[mid_index]:
        return mid_index
      elif needle < haystack[mid_index]:
        return _binary_search_rec(needle, haystack, start_index, mid_index-1)
      else:
        return _binary_search_rec(needle, haystack, mid_index+1, end_index)
        

# SAMPLE TESTS:
print(binary_search(2, [])) # None
print(binary_search(2, [2, 4, 6])) # 0
print(binary_search(2, [1, 2, 3])) # 1
print(binary_search(10, [4, 6, 10, 7, 9])) # 2
print(binary_search(4, [4, 6, 10, 7, 9])) # 0
print(binary_search(8, [3, 4, 6, 7])) # None
