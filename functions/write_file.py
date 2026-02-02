from pathlib import Path
from google.genai import types


def write_file(working_directory, file_path, content):
    abs_working_dir = Path(working_directory).resolve()
    abs_file_path = (abs_working_dir / file_path).resolve()
    if not abs_file_path.is_relative_to(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    if not abs_file_path.is_file():
        _path = Path(abs_file_path)
        try:
            _path.parent.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            return f"Error:Could not create dirs: {_path} = {e}"
        try:
            with open(abs_file_path, "w") as f:
                f.write(content)
                return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        except Exception as e:
            return f"Error:Unable to write {file_path},{e}"
    else:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory or file does not exist'

write_file_tool = types.FunctionDeclaration(
    name="write_file",
    description="Creates or overwrites a file with specific content. It automatically creates parent directories if they don't exist.",
    parameters=types.Schema(
        type="OBJECT",
        properties={
            "file_path": types.Schema(
                type="STRING",
                description="The path where the file should be created, including the filename (e.g., 'scripts/cleaner.py')."
            ),
            "content": types.Schema(
                type="STRING",
                description="The actual text or code content to be written into the file."
            ),
        },
    )
)

