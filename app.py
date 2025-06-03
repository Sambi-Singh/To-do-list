tasks = []
#Update
def changeTask():
    showTasks()
    taskNum = int(input("Choose the tasks # you wish to modify: "))
    try:
        if taskNum < len(tasks) and taskNum >= 0:
            newTask = input("Enter the name of the new task: ")
            tasks[taskNum] = newTask
            print(f"{newTask} has been added as task number {taskNum}.")
            showTasks()
    
    except:
        print("Invalid task number, please try again")

#Read
def showTasks():
    if not tasks:
        print("There are no tasks pending.")
    else:
        print("Here are your on going tasks:")
        for index,task in enumerate(tasks): #enumerate useful!
            print(f"Task #{index}. {task}")

            #Task #1. Buy Milk

#Delete
def deleteTask():
    showTasks()
    try:
        taskNum = int(input("Enter the # to delete: "))
        if taskNum>=0 and taskNum < len(tasks):
            tasks.pop(taskNum)
            print(f"task #{taskNum} has been removed.")
        
        else:
            print(f"Tasks #{taskNum} was not found.")
            

    except:
        print("Invalid input.")

   

#Create
def makeTask():
    taskName = input("Please enter task name: ")
    tasks.append(taskName)
    if taskName in tasks:
        print(f"'{taskName}' has been successfully added!")
    else:
        print("ERROR: Task could not be added at this time, please try again")



def main():
    while True:
        action = input('i - Inserts 1 task\nd - Deletes 1 task\nm- Modifies 1 existing task\n')
    #print(action)
        if action.lower() == 'i':
            makeTask()
            showTasks()
        elif action.lower() == 'd':
            deleteTask()
        elif action.lower() == 'm':
            changeTask()
        else:
            print("\nexiting!")
            break


    
    

if __name__ == "__main__":
    main()
