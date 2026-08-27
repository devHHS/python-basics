# test_notes.py
from notes import next_id, find_note_by_id, add_note, update_note, find_all_by_title, find_all_notes
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

def test_add_note(sample_notes):
    updated_notes = add_note(sample_notes, "b", "y")
    assert len(updated_notes) == 2
    assert updated_notes[-1]["title"] == "b"
    assert updated_notes[-1]["content"] == "y"
    assert updated_notes[-1]["id"] == 2
    assert updated_notes is sample_notes  # Ensure the original list is modified, not a new list created

def test_update_note_existing(sample_notes):
    updated_note = update_note(sample_notes, 1, "new content")
    assert updated_note is not None
    assert updated_note["content"] == "new content"
    assert sample_notes[0]["content"] == "new content"  # Ensure the original note is updated 

def test_update_note_not_found(sample_notes):
    updated_note = update_note(sample_notes, 2, "new content")
    assert updated_note is None

def test_find_all_by_title_existing(sample_notes):
    found_notes = find_all_by_title(sample_notes, "a")
    assert len(found_notes) == 1
    assert found_notes[0]["title"] == "a"

def test_find_all_by_title_not_found(sample_notes):
    found_notes = find_all_by_title(sample_notes, "b")
    assert len(found_notes) == 0

def test_find_all_notes(sample_notes):
    all_notes = find_all_notes(sample_notes)
    assert all_notes == sample_notes

def test_find_all_notes_empty():
    all_notes = find_all_notes([])
    assert all_notes == []