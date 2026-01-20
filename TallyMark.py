from collections import Counter
import datetime

def total_avg(arr):
  arr_total = 0
  arr_avg = 0
  for i in range(len(arr)):
    arr_total = arr_total + (arr[i]*100) + 99
    arr_avg = arr_total / len(arr)
  return arr_total, arr_avg

def clear_list(arr):
  clearInput = ""
  while clearInput != "y":
    clearInput = input("Are you sure? Insert n for no or y for yes\n")
    if clearInput == "y":
      arr.clear()
    elif clearInput == "n":
      break
    else:
      print("Invalid input, please try again")

def display_count(arr):
  display = Counter(arr)
  tallymark = sorted(display.items())
  print("TallyMark list produced:")
  for i in tallymark:
    print(i)
  print("")

def remove_recent(arr):
  del arr[len(arr)-1]

def main():
  user_input = ""
  section_count = []
  complete_count = []

  print("Welcome to the TallyMark Program")
  while user_input != "quit":
    user_input = input("Insert a number or input 'quit' to exit\n")
    if user_input.isdigit():
      timestamp = datetime.datetime.now()
      user_input = int(user_input)
      section_count.append(user_input)
      complete_count.append(user_input)

      sect_total, sect_avg = total_avg(section_count)

      complete_total, complete_avg = total_avg(complete_count)

      print("Input inserted at " + timestamp.strftime("%X"))
      print("Section Price Average: " + str(round((sect_avg / 100), 2)) + "\nSection Price Total: " + str(sect_total / 100) + "\nSection Item Count: " + str(len(section_count)) + "\nTotal Price Average: " + str(round((complete_avg / 100), 2)) + "\nTotal Price Amount: " + str(round((complete_total / 100), 2)) + "\nComplete Item Count: " + str(len(complete_count)))

    elif user_input == "r":
      print(section_count)
      remove_recent(section_count)
      print(section_count)
      print(complete_count)
      remove_recent(complete_count)
      print(complete_count)

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
