from pathlib import Path
from google.genai import types

def get_file_content(working_directory, file_path):
    abs_working_dir = Path(working_directory).resolve()
    abs_file_path = (abs_working_dir / file_path).resolve()
    if abs_file_path.is_file():
        limiter = 1000
        try:
            with abs_file_path.open(mode="r", encoding="utf-8", errors="ignore") as f:
                content = f.read(limiter)
                if f.read(1):
                    content += "\n\n[!] LIMIT REACHED: Content truncated at 10k chars."
                return content
        except FileNotFoundError:
            return f"Error: The file at {file_path} does not exist."
        except PermissionError:
            return f"Error: Permission denied. I can't look inside {file_path}."
        except Exception as e:
            return f"An unexpected error occurred: {e}"
    else:
        return f"Error:❌ Cannot read as it is outside the permitted working directory ' {file_path}' "

get_file_content_tool = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the content of a file within a specific directory. Returns the first 1000 characters.",
    parameters=types.Schema(
        type="OBJECT",
        properties={
           "file_path": types.Schema(
                type="STRING", 
                description="The relative path to the file you want to read."
            ),
        }
    )
)