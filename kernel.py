import os

user = input("please verify your username: ")
print("the auroraborealis kernel")

# Function to create 'my_project' directory and README.txt
def create_project():
    try:
        project_dir = "my_project"
        if not os.path.exists(project_dir):
            os.mkdir(project_dir)
            print(f"Directory '{project_dir}' created.")
            
            # Create README file
            readme_content = """\
Wow, I didn't think people would read this. Well...
Hello, I am Graham and I love to make programs with my friend Milo, and this is one of those. 
Hope you find it useful!
"""
            readme_file = os.path.join(project_dir, "README.txt")
            with open(readme_file, 'w') as f:
                f.write(readme_content)
                
            print(f"Created file 'README.txt' in '{project_dir}'.")
            
        else:
            print(f"Directory '{project_dir}' already exists.")
    except PermissionError:
        print("Permission denied. Cannot create directory.")

# Function to read contents of README.txt if in 'my_project' directory
def read_readme():
    current_dir = os.getcwd()
    project_dir = os.path.abspath("my_project")
    if current_dir == project_dir or current_dir.startswith(project_dir + os.sep):
        try:
            readme_file = os.path.join(current_dir, "README.txt")
            with open(readme_file, 'r') as f:
                contents = f.read()
                print(f"Contents of '{readme_file}':")
                print(contents)
        except FileNotFoundError:
            print("README.txt not found. Make sure 'my_project' directory and README.txt exist.")
    else:
        print("You are not in 'my_project' or its subdirectory. Change directory to access README.")

# Check and create 'my_project' directory and README.txt on startup
create_project()

while True:
    usertxt = input("command: ")
    if usertxt == "help":
        print("help")
        print("ping")
        print("auroraver")
        print("whoami")
        print("ls")
        print("cd_my_project")
        print("read_readme")  # Added command to read contents of README.txt
        print("exit")
    elif usertxt == "ping":
        print("this kernel can only ping:")
        print("192.168.0.1 or a LinureOS server")
        try:
            pingamount = int(input("ping how many times?: "))
            print("okay we will ping:", pingamount, "times")
            for i in range(pingamount):
                print("pinged: 192.168.0.1")
        except ValueError:
            print("Please enter a valid number.")
    elif usertxt == "auroraver":
        print("aurora kernel version:")
        print("0.2.4 python3")
    elif usertxt == "whoami":
        print(user, "online welcome!")
    elif usertxt == "ls":
        try:
            path = input("Enter directory path (leave empty for current directory): ").strip()
            if not path:
                path = "."
            contents = os.listdir(path)
            print(f"Contents of {os.path.abspath(path)}:")
            for item in contents:
                print(item)
        except FileNotFoundError:
            print("Directory not found. Please enter a valid directory path.")
        except PermissionError:
            print("Permission denied. You do not have access to this directory.")
    elif usertxt == "cd_my_project":
        try:
            os.chdir("my_project")
            print("Changed directory to 'my_project'.")
        except FileNotFoundError:
            print("'my_project' directory not found.")
        except PermissionError:
            print("Permission denied. Cannot change directory.")
    elif usertxt == "read_readme":
        read_readme()
    elif usertxt == "exit":
        print("Exiting the kernel. Goodbye!")
        break
    else:
        print("Unknown command. Type 'help' for a list of available commands.")
