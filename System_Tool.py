# import the used libraries
import os
import shutil
import socket
import os.path
# function to link the input with the tasks
def choice(task_number):
    if task_number == "1" :
        monitor_resources()
    elif task_number == "2" :
        list_content()
    elif task_number == "3" :
        exit_tool()
# function to take number of the task from the user and do it.
def menu_input():
    task_number  = input( "Enter the number of task : ")
    if task_number != "1" and task_number != "2" and task_number != "3" : 
        print("Please enter 1 or 2 or 3 ")
        return menu_input() #if the user didn't enter 1 or 2 or 3 > ask him again
    else:
        choice(task_number) #call the choice function and pass "task_number for it"
# function to display the menu for the user
def menu_output():
    print("""
          Hi!, Welcome to our tool 
          
          These are our menu of tasks : 
          
          Task [1] : Monitor System Resources.
          Task [2] : List Directory Contents.
          Task [3] : Exit the Tool.
          """)
    menu_input()
# function to go back after doing the task
def go_back():
    menu_again = input("Enter [0] to go back to the menu : ")
    if menu_again == "0":
                    menu_output()
    else :
                print("Invalid choice , please enter [0] .")
                go_back()
# function for the first task "monitor resources"
def monitor_resources ():
    host_name = socket.gethostname()
    try: #error handling
        ip_address = socket.gethostbyname(host_name)
    except Exception as e:
        ip_address = "Unable to fetch IP address"
    usage = shutil.disk_usage(".")
    total_disk_space = usage.total / (2 ** 30)
    used_disk_space = usage.used / (2 ** 30)
    free_disk_space = usage.free / (2 ** 30)
    information = f"""
    
    Device Information : 
    
    Device host name : {host_name} 
    Device IP : {ip_address} 
    
    Disk Information : 
    
    Total disk space = {round( total_disk_space , 2)} GB
    Used disk space = {round(used_disk_space , 2)} GB
    Free disk space = {round(free_disk_space , 2)} GB
    """
    print(information)
    go_back()
# function for the second task "list content"
def list_content ():
    path = input("Enter the path of the directory you want to list : ")
    if os.path.exists(path) :
        files = os.listdir(path)
        print("The content of the path : ")
        for file in files:
            file_path = os.path.join(path, file)  
            if os.path.isfile(file_path):
                print(f"File name: {file} [file]")
            elif os.path.isdir(file_path):
                print(f"Directory name: {file} [directory]")
        go_back()       
    else :
        inputt = input("The path does not exist X \nenter a valid path [or] enter [0] to go back to the menu : ")
        if inputt == "0" :
            menu_output()
        return list_content()
# function for the third task "exit the tool"
def exit_tool():
        print("Goodbye! Thank you for using the tool.")
        exit() 
menu_output()


