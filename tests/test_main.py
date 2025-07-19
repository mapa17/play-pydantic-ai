"""Tests for the main module."""

from play_pydantic_ai.main import hello


def test_hello():
    """Test that hello() returns the expected greeting message."""
    expected_message = "Hello from play-pydantic-ai!"
    actual_message = hello()
    assert actual_message == expected_message


def test_hello_return_type():
    """Test that hello() returns a string."""
    result = hello()
    assert isinstance(result, str)


def test_hello_not_empty():
    """Test that hello() returns a non-empty string."""
    result = hello()
    assert result
    assert len(result) > 0
