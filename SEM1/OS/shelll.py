import os
import shutil

def run_terminal():
    print("Simple Linux Terminal (Python Simulation)")
    print("Type 'exit' to quit.\n")

    while True:
        command = input(f"{os.getcwd()}$ ").strip()

        if command == "exit":
            break

        elif command == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')

        elif command == "pwd":
            print(os.getcwd())

        elif command == "ls":
            try:
                for item in os.listdir():
                    print(item)
            except Exception as e:
                print("ls error:", e)

        elif command.startswith("cd"):
            try:
                path = command[3:].strip()
                if path == "":
                    print("Usage: cd <directory>")
                else:
                    os.chdir(path)
            except Exception as e:
                print("cd error:", e)

        elif command.startswith("mkdir"):
            try:
                dirname = command[6:].strip()
                os.mkdir(dirname)
            except Exception as e:
                print("mkdir error:", e)

        elif command.startswith("touch"):
            try:
                filename = command[6:].strip()
                open(filename, 'a').close()
            except Exception as e:
                print("touch error:", e)

        elif command.startswith("cp"):
            try:
                parts = command.split()
                if len(parts) < 3:
                    print("Usage: cp <source> <destination>")
                else:
                    shutil.copy(parts[1], parts[2])
            except Exception as e:
                print("cp error:", e)

        elif command.startswith("mv"):
            try:
                parts = command.split()
                if len(parts) < 3:
                    print("Usage: mv <source> <destination>")
                else:
                    shutil.move(parts[1], parts[2])
            except Exception as e:
                print("mv error:", e)

        elif command.startswith("rm"):
            try:
                parts = command.split()
                if len(parts) < 2:
                    print("Usage: rm <file/folder>")
                else:
                    target = parts[1]
                    if os.path.isdir(target):
                        shutil.rmtree(target)
                    else:
                        os.remove(target)
            except Exception as e:
                print("rm error:", e)

        elif command.startswith("cat"):
            try:
                parts = command.split()
                if len(parts) < 2:
                    print("Usage: cat <filename>")
                else:
                    with open(parts[1], "r") as f:
                        print(f.read())
            except Exception as e:
                print("cat error:", e)

        else:
            print("Invalid command!")

# Run the terminal
run_terminal()