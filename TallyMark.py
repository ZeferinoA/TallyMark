from collections import Counter

def total_avg(arr):
  arr_total = 0
  arr_avg = 0
  for i in range(len(arr)):
    arr_total = arr_total + (arr[i]*100) + 99
    arr_avg = arr_total / len(arr)
  return arr_total, arr_avg

def clear_list(arr):
  arr.clear()

def display_count(arr):
  arr.sort()
  display = Counter(arr)
  print("")
  print(display)
  print("")

def main():
  user_input = ""
  section_count = []
  complete_count = []

  print("Welcome to the TallyMark Program")
  while user_input != "quit":
    user_input = input("Insert a number or input 'quit' to exit\n")
    if user_input.isdigit():
      user_input = int(user_input)
      section_count.append(user_input)
      complete_count.append(user_input)

      sect_total, sect_avg = total_avg(section_count)

      complete_total, complete_avg = total_avg(complete_count)

      print("Section Average: " + str(round((sect_avg / 100), 2)) + "\nSection Total: " + str(sect_total / 100) + "\nTotal Average: " + str(round((complete_avg / 100), 2)) + "\nTotal Amount: " + str(complete_total / 100))

    elif user_input == "a":
      display_count(complete_count)
    
    elif user_input == "d":
      display_count(section_count)

    elif user_input == "c":
      clear_list(section_count)

    elif user_input == "quit":
      print("Goodbye!")

    else:
      print("Invalid input, please try again")



if __name__=="__main__":
  main()
