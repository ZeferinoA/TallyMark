section_count = []
total_count = []

def total_avg(arr):
  arr_total = 0
  for i in arr:
    arr_total = arr_total + arr[i] + 0.99
    arr_avg = arr_total / len(arr)

def clear_list(arr):
  arr.clear()

def display_count(arr):
  unique = list(set(arr))
