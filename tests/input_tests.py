
import pytest
import os
import pandas as pd
from app.io.input import read_from_file, read_from_file_pandas

# Tests for read_from_file function
def test_read_from_file_success(tmp_path):
    """Test that read_from_file correctly reads content from a file."""
    # Create a temporary test file
    test_content = "This is test content\nfor read_from_file function"
    test_file = tmp_path / "test_file.txt"
    test_file.write_text(test_content)
    
    # Test that function reads the content correctly
    result = read_from_file(str(test_file))
    assert result == test_content


def test_read_from_file_nonexistent():
    """Test that read_from_file handles non-existent files correctly."""
    # Try to read from a file that doesn't exist
    result = read_from_file("nonexistent_file.txt")
    assert "Error: File 'nonexistent_file.txt' not found" in result


def test_read_from_file_permission_error(tmp_path, monkeypatch):
    """Test that read_from_file handles permission errors."""
    # Create a test file
    test_file = tmp_path / "no_permission.txt"
    test_file.write_text("Some content")
    
    # Mock the open function to raise a permission error
    def mock_open(*args, **kwargs):
        raise PermissionError("Permission denied")
    
    monkeypatch.setattr("builtins.open", mock_open)
    
    # Test the function handles the error correctly
    result = read_from_file(str(test_file))
    assert "Error reading file:" in result
    assert "Permission denied" in result
