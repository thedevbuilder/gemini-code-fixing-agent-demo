from functions.write_file import write_file
from functions.run_file import run_python_file
from prompts.prompts import SystemPrompts

def main():
    working_dir = "calculator"
    # success
    print(run_python_file(working_directory=working_dir,file_path="main.py",args=["3 + 5"]))
    # failure
    print(run_python_file(working_directory=working_dir,file_path="../../main.py",args=["3 + 5"]))
    print(run_python_file("calculator", "nonexistent.py"))
    #empty arguments
    print(run_python_file(working_directory=working_dir,file_path="main.py"))
    print(SystemPrompts.ROBOT_ON_STRIKE)



main()
