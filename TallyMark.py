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
  arr.clear()

def display_count(arr):
  display = Counter(arr)
  tallymark = sorted(display.items())
  print("TallyMark list produced:")
  for i in tallymark:
    print(i)
  print("")

def remove_recent(arr):
  del arr[len(arr)-1]

def bulk_remove(arr):
  bulkDel = int(input("How many items would you like to delete?"))
  for i in range(1, bulkDel):
    del arr[len(arr)-i]

def bulk_add(arr, numItem, bulkItem):
  for i in range(bulkItem):
    with open(filename, "a") as countAppend:
        countAppend.write(str(numItem) + "\n")
    arr.append(numItem)

def main():
  user_input = ""
  section_count = []
  complete_count = []
  with open(filename, "r") as countRead:
    for line in countRead:
      processed_line = line.strip()
      if processed_line == "SC":
        clear_list(section_count)
      else:
        complete_count.append(int(line.strip()))
        section_count.append(int(line.strip()))

  while user_input != "quit":
    user_input = input("Insert a number or input 'quit' to exit\n")
    if user_input.isdigit():
      timestamp = datetime.datetime.now()
      user_input = int(user_input)
      section_count.append(user_input)
      complete_count.append(user_input)
      with open(filename,"a") as countWrite:
        countWrite.write(str(complete_count[len(complete_count)-1]) + "\n")

      sect_total, sect_avg = total_avg(section_count)

      complete_total, complete_avg = total_avg(complete_count)

      print("Input inserted at " + timestamp.strftime("%X"))
      print("Section Price Average: " + str(round((sect_avg / 100), 2)) + "\nSection Price Total: " + str(sect_total / 100) + "\nSection Item Count: " + str(len(section_count)) + "\nTotal Price Average: " + str(round((complete_avg / 100), 2)) + "\nTotal Price Amount: " + str(round((complete_total / 100), 2)) + "\nComplete Item Count: " + str(len(complete_count)))

    elif user_input == "r":
      with open(filename, 'r') as f:
        lines = f.readlines()
        lines = lines[:-1]
      with open(filename, 'w') as f:
        f.writelines(lines)
      remove_recent(section_count)
      remove_recent(complete_count)

    elif user_input == "b":
      numItem = int(input("What amount would you like to add in bulk?\n"))
      bulkItem = int(input("How many would you like to add\n"))
      bulk_add(section_count,numItem,bulkItem)
      bulk_add(complete_count,numItem,bulkItem)

    elif user_input == "br":
      bulk_remove(section_count)
      bulk_remove(complete_count)

    elif user_input == "a":
      display_count(complete_count)
    
    elif user_input == "d":
      display_count(section_count)

    elif user_input == "c":
      with open(filename, "a") as countAppend:
        countAppend.write("SC\n")
      clearInput = ""
      while clearInput != "y":
        clearInput = input("Are you sure? Insert n for no or y for yes\n")
        if clearInput == "y":
          clear_list(section_count)
        elif clearInput == "n":
          break
        else:
          print("Invalid input, please try again")

    elif user_input == "e":
      display_count(section_count)
      with open(filename, "a") as countAppend:
        countAppend.write("SC\n")
      clear_list(section_count)

    elif user_input == "quit":
      print("Goodbye!")

    else:
      print("Invalid input, please try again")



if __name__=="__main__":
  filename = str(datetime.date.today()) + ".txt"
  
  try:
    with open(filename, 'x') as f:
      print("Start of the Day")  
  except FileExistsError:
    print("Welcome Back")
  main()
