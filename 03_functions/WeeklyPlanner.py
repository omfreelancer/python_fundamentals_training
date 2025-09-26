#tasks = {"monday":[],"tuesday":[],"wednesday":[],"thursday":[],"friday":[],"saturday":[],"sunday":[]}
    #Functions:
  #add_task(day,task):
#tasks[day].append(task)
  #list_tasks(day):
#return tasks[day]
  #clear_tasks(day):
#tasks[day].clear()
    #Main program
#Show the user the menu(add,list,clear,quit,a,l,c,q)
#ask to choose
#choice = choice_input.strip().lower()
#if user chose something out of options --> print ("Invalid input") and reask
#if chose quit/q end the program
#else:
  #ask for a day and should be valid
  #day = day_user_input.strip().lower()
  #use a loop until chose a day in tasks
    #if choice was (a/add):
      #ask for a task
      #call the function
    #if user choice was (list/l):
      #item_list = list_tasks(day)
      #if not item_list --> print("No tasks planned for this day.")
      #else: --> for index,item in enumerate(item_list):
          #print(f"{index+1}.{item}")
    #if choice was (c/clear):
      #call the function
      #print(f"tasks of {day} was cleared.")

tasks = {"monday":[],"tuesday":[],"wednesday":[],
         "thursday":[],"friday":[],"saturday":[],"sunday":[]
         }

#Functions:
def add_task(day,task):
    tasks[day].append(task)

def list_tasks(day):
    return tasks[day]

def clear_tasks(day):
    count = len(tasks[day])
    tasks[day].clear()
    return count

def get_valid_day():
    while True:
        day = input("Enter a day (e.g., Monday): ").strip().lower()
        if day in tasks:
            return day
        print("Invalid input. Please enter a valid weekday name (e.g., Monday).")

def show_menu():
    print("\n=== Weekly Planner ===")
    print("[A]dd task")
    print("[L]ist tasks")
    print("[C]lear tasks")
    print("[Q]uit")

aliases = {"a": "add", "l": "list", "c": "clear", "q": "quit"}

#Main program:

while True:
  show_menu()
  choice = input("Choose an option: ").strip().lower()
  choice = aliases.get(choice, choice)

  if choice == "quit":
    print("Goodbye!")
    break

  if choice == "add":
      day = get_valid_day()
      task = input(f"Enter the task to add to {day.title()}: ").strip()
      while not task:
          task = input("Task cannot be empty. Enter task: ").strip()
      add_task(day, task)
      print(f"Added to {day.title()}: {task}")

  elif choice == "list":
      day = get_valid_day()
      items = list_tasks(day)
      if not items:
          print("No tasks planned for this day.")
      else:
          print(f"Tasks for {day.title()}: ")
          for i, item in enumerate(items, 1):
              print(f"{i}. {item}")
  
  elif choice == "clear":
      day = get_valid_day()
      n = clear_tasks(day)
      print(f"Cleared {n} task(s) from {day.title()}.")

  else:
      print("Invalid option. Please choose A, L, C, or Q.")