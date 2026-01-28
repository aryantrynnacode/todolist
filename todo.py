
def display_menu():
    print("----TO-DO LIST----")
    print("1. Add a task")
    print("2. View a task")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Exit")
task_list=[]
while True:
  display_menu()
  try:
    user_choice = int(input("Enter your choice: "))
  except ValueError:
    print("please enter number only.")
  if user_choice == 1:
    task=input("Enter task name: ")
    if task == "":
      print("task can't be empty")
    else:
      task_list.append(task)
      print("task is added")

  elif user_choice == 2:
    print(task_list)

  elif user_choice == 3:
    if len(task_list)==0:
      print("no task to update")
    else:
      for i, task in enumerate(task_list, start=1):
        print(f"{i}.{task}")
    task_number1 = int(input("enter the task number you want to update"))
    if 1 <= task_number1 <= len(task_list):
      new_task = (input("enter the new task ")).strip()
      if new_task == "":
        print("task cant be empty")
      else:
        task_list[task_number1 - 1] = new_task
        print("task updated sucessfully")
    
  elif user_choice == 4:
    if len(task_list)==0:
      print("no task to delete")
    else:
      for i, task in enumerate(task_list, start=1):
        print(i, task)
    task_number = int(input("enter the task number u want to delete"))
    if 1 <= task_number <= len(task_list):
      task_list.pop(task_number-1)
      print("task deleted successfully")
    else:
      print("invalid number")

  elif user_choice == 5:
    print("exiting application...")
    break
  
  else:
    print("Invalid choice")



