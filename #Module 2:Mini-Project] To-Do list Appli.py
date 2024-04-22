#Module 2:Mini-Project] To-Do list Application
#User Interface(UI)
while True:
    # 1. Add a task
    # 2. View tasks
    # 3. Mark a task as complete
    # 4. Delete a task
    # 5. Quit
    def To_do():
        return 
    response = input("""What would you like to do? 
                1.Add a task
                2. View tasks
                3. Mark a task as complete
                4. Delete a task
                5. Quit""")
#2. To do list
    if response == "1":
            YN = input("did it or not yet")
            if YN == "did it":
                print("complete")
                print("proceed to task 2")
            else:
                YN == "not yet"
                print("Incomplete")
    elif response == "2":
            Y2= input("did it or not yet")
            if Y2 == "did it":
                print("complete")
                print("proceed to task 3")
            else:
                Y2 == "not yet"
                print("Incomplete")
    elif response == "3":
            Y3 = input("did it or not yet")
            if Y3 == "did it":
                    print("complete")
                    print("proceed to task 4")
            else:
                Y3 == "not yet"
                print("Incomplete")
    elif response == "4":
            Y4 = input("did it or not yet")
            if Y4 == "did it":
                    print("complete")
                    print("proceed to task 5")
            else:
                Y4 == "not yet"
                print("Incomplete")
    elif response == "5":
            Y4 = input("did it or not yet")
            if Y4 == "did it":
                     print("complete")
            else:
                Y4 == "not yet"
                print("Incomplete")
    else: 
            print("please enter valid response")
    try:
        To_do()
    except TypeError:
          print("please enter valid response")