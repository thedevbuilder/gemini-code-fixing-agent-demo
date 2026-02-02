from google.genai import types
from functions.get_file_info import get_files_content_tool,get_files_content
from functions.get_file_content import get_file_content_tool,get_file_content
from functions.run_file import run_python_file_tool,run_python_file
from functions.write_file import write_file_tool,write_file
from config import WORKING_DIR
available_functions =  types.Tool(
            function_declarations=[
                get_file_content_tool,
                get_files_content_tool,
                run_python_file_tool,
                write_file_tool,
            ]
        )

function_map = {
    "get_file_content": get_file_content,
    "get_files_content":get_files_content,
    "run_python_file":run_python_file,
    "write_file":write_file
    }
def call_function(function_call, verbose=False):  
    result = ""
    if verbose:
        print(f"Calling function: {function_call.name}({function_call.args})")
    else:
     print(f" Calling function: {function_call.name}")
    
    if  function_call.name  ==   "get_file_content":
        result =  get_file_content(working_directory=WORKING_DIR,**function_call.args)
    if  function_call.name  ==   "get_files_content":
            result = get_files_content(working_directory=WORKING_DIR,**function_call.args)
    if  function_call.name  ==   "run_python_file":
        result =  run_python_file(working_directory=WORKING_DIR,**function_call.args)
    if  function_call.name  ==   "write_file":
        result =  write_file(working_directory=WORKING_DIR,**function_call.args)
    if  result == "":
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call.name,
                    response={"error": f"Unknown function: {function_call.name}"},
                )   
            ],
                )
   
    return types.Content(
role="tool",
parts=[
    types.Part.from_function_response(
        name=function_call.name,
        response={"result": result},
    )
],
)