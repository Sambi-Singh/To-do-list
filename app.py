tasks = []
#Update
def changeTask():
    pass

#Read
def showTasks():
    for task in tasks:
        print(f"{task}\n")

#Delete
def deleteTask():
    pass

#Create
def makeTask():
    taskName = input("Please enter task name: ")
    tasks.append(taskName)
    if taskName in tasks:
        print(f"'{taskName}' has been successfully added!")
    else:
        print("ERROR: Task could not be added at this time, please try again")



def main():
    action = input('i - Inserts 1 task\nd - Deletes 1 task\nm- Modifies 1 existing task\n')
    #print(action)
    if action.lower() == 'i':
        makeTask()
        showTasks()
    elif action.lower() == 'd':
        pass
    elif action.lower() == 'm':
        pass
    else:
        print("\nTest test!")


    
    

if __name__ == "__main__":
    main()
