tasks = [] 
def menu():
    print("TO-DO list menu")
    print("1.Add task")
    print("2.View taks") 
    print("3.Update tasks")
    print("4.Delete tasks")
    print("5.exit")
while True:
    menu()
    choice = input("enter your choice:")
    if choice == '1':
        task = input("Enter new tasks:")
        tasks.append(task) 
        print("Tasks added successfully")
    elif choice == '2':
        if len(tasks) == 0:
            print(" no tasks available")
        else:
            print("\nYour tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
    elif choice == '3':
        if len(tasks) == 0:
            print("no tasks to update")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
            num = int(input("Enter task number to update:"))
            if 1<= num <= len(tasks):
                new_tasks = input("Enter updated task:")
                tasks[num-1] = new_tasks
                print("tasks updated successfully")
            else:
                print("invalid task number")
    elif choice == '4':
        if len(tasks) == 0:
            print("no tasks to deleted")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
            num = int(input("enter task number to delete:"))
            if 1<= num <= len(tasks):
                tasks.pop(num-1)
                print("tasks deleted sucessfully")
            else:
                print("invalid task number")
    elif choice == '5':
        print("exit to-do list")
        break
    else:
        print("invalid choice!!")