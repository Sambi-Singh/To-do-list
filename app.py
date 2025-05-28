
#Update
def changeTask():
    pass

#Read
def showTasks():
    pass

#Delete
def deleteTask():
    pass

#Create
def makeTask():
    print("Please enter task name")

def main():
    action = input('i - Inserts 1 task\nd - Deletes 1 task\nm- Modifies 1 existing task\n')
    print(action)
    
    makeTask()

if __name__ == "__main__":
    main()
