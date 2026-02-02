from functions.run_file import run_python_file

def test_run_python_file_isRelativeToSuccess(tmp_path):
            # Arrange
            working_dir = tmp_path / "calculator"
            working_dir.mkdir()
            my_file = working_dir/"text.py"
            # Act
            result = run_python_file(working_dir,my_file)
            # Assert
            assert "Success✅" in result
def test_run_python_file_isRelativeToFailure(tmp_path):
            # Arrange
            working_dir = tmp_path / "calculator"
            working_dir.mkdir()
            my_file = "../../text.py"
            # Act
            result = run_python_file(working_dir,my_file)
            # Assert
            assert "Error" in result
