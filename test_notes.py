# test_notes.py
from notes import next_id, find_note_by_id
import pytest

@pytest.fixture
def sample_notes():
    return [{"id": 1, "title": "a", "content": "x"}]

def test_next_id_empty_list():
    assert next_id([]) == 1

def test_next_id_with_existing_notes(sample_notes):
    assert next_id(sample_notes) == 2

def test_find_note_by_id_existing(sample_notes):    
    assert find_note_by_id(sample_notes, 1) == {"id": 1, "title": "a", "content": "x"}

def test_find_note_by_id_not_found(sample_notes):
    assert find_note_by_id(sample_notes, 2) is None