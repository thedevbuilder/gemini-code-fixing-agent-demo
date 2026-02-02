from pathlib  import Path
import subprocess
from google.genai import types

def run_python_file(working_directory:str, file_path:str, args=[]):
           # get root:str
    root_base = Path(__file__).resolve().parent.parent
    # get the working directory
    abs_working_directory = Path(working_directory)
    base = root_base.joinpath(abs_working_directory)
    # check if the file path is not outside the working dir
    path_check = (base / file_path).resolve()
    if not path_check.is_relative_to(base):
        return f"Error: Cannot read {file_path} as it is outside the permitted working directory"
    if not path_check.is_file():
        return f'Error: "{file_path}" does not exist or is not a regular file'
    if path_check.suffix != ".py":
          return f'Error: "{file_path}" is not a Python file'
    try:
        final_input =  ["python",path_check]
        final_input.extend(args)
        output = subprocess.run(
            final_input,
            cwd=abs_working_directory,
            timeout=30,
            capture_output=True,
            text=True
            )
        
        if output.returncode != 0:
              return f"Process exited with code {output.returncode}"
        else:
              return f"STDOUT: {output.stdout.strip() if output.stdout.strip() else '(Success, but no output)'}"
              
    except subprocess.CalledProcessError as e:
        # Failure path: the 'e' object contains the stderr
            error_msg = e.stderr.strip() if e.stderr else "Unknown Error"
            return f"STDERR: {error_msg} (Exit Code: {e.returncode})"
    except Exception as e:
            return f"Error:Can not run {path_check},{e}"        
  

run_python_file_tool = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within a permitted directory and returns the output. Use this to run scripts, data processing tasks, or tests.",
    parameters=types.Schema(
        type="OBJECT",
        properties={
            "file_path": types.Schema(
                type="STRING",
                description="The path to the .py file you want to execute."
            ),
            "args": types.Schema(
                type="ARRAY",
                items=types.Schema(type="STRING"),
                description="Optional list of command-line arguments to pass to the script."
            ),
        }
    )
)
