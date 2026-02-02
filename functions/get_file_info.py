from pathlib import Path
import os
from google.genai import types

def get_files_content(working_directory, path_file=None):
    # get root
    root_base = Path(__file__).resolve().parent.parent
    # get the working directory
    abs_working_directory = Path(working_directory)
    base = root_base.joinpath(abs_working_directory)
    # check if the file path is not outside the working dir
    path_check = (base / path_file).resolve()
    if not path_check.is_relative_to(base):
        return f"Error: Cannot read {path_file} as it is outside the permitted working directory"

    if not path_check.exists():
        return f"Error: The path {path_file} does not exist."

    exclude = {".git", "node_modules", "__pycache__", ".venv"}
    if path_check.exists():
        for root, dirs, files in os.walk(path_check):
            dirs[:] = [d for d in dirs if d not in exclude]
            root_path = Path(root)
            for file_path in files:
                _file_path = root_path / file_path

                size = _file_path.stat().st_size
                size_kb = size / 1024
                is_dir = _file_path.is_dir()
                print(
                    f"-{_file_path.name} file_size =({size_kb:.2f} KB, is_dir={is_dir})"
                )
    else:
        print(f"❌ folder does exist in {root_base}")

    # check of a direct existing the root
get_files_content_tool = types.FunctionDeclaration(
    name="get_files_content",
    description="Lists and audits files within a directory, providing file sizes and directory status. Excludes sensitive folders like .git and __pycache__.",
    parameters=types.Schema(
        type="OBJECT",
        properties={
            "path_file":types.Schema(
                 type="STRING",
                 description="The specific sub-folder or file path to scan. Defaults to the working directory if not provided."
            )
        }
    )
)