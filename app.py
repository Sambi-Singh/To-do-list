tasks = []
#Update
def changeTask():
    pass

#Read
def showTasks():
    print("Here are your on going tasks:")
    for task in tasks:
        print(f"{task}\n")

#Delete
def deleteTask():
    tasks.append("berry")
    tasks.append("cherry")
    tasks.append("lary")

    for i in range(len(tasks) - 1):
        print(f"{tasks[i]} has been successfully removed! :)")
        tasks.pop(i)


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
        deleteTask()
    elif action.lower() == 'm':
        pass
    else:
        print("\nTest test!")


    
    

if __name__ == "__main__":
    main()
