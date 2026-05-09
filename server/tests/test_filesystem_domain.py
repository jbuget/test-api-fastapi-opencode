from src.domain.filesystem import Folder, Document
import uuid
import pytest
from src.domain.filesystem import Folder, Document

def test_create_folder_successfully():
    """Test that a folder can be created successfully."""
    folder_id = str(uuid.uuid4())
    folder = Folder(id=folder_id, name="Root")
    assert folder.name == "Root"
    assert folder.parent_id is None
    assert len(folder.children) == 0

def test_folder_can_contain_children():
    """Test that a folder can contain other folders or documents."""
    parent_id = str(uuid.uuid4())
    parent_folder = Folder(id=parent_id, name="Parent")
    
    child_id = str(uuid.uuid4())
    child_folder = Folder(id=child_id, name="Child")
    
    parent_folder.add_child(child_folder)
    
    assert len(parent_folder.children) == 1
    assert parent_folder.children[0].name == "Child"

def test_document_creation():
    """Test that a document can be created with metadata."""
    doc_id = str(uuid.uuid4())
    doc = Document(
        id=doc_id,
        name="report.pdf",
        file_size=1024,
        mime_type="application/pdf"
    )
    assert doc.name == "report.pdf"
    assert doc.file_size == 1024
    assert doc.mime_type == "application/pdf"

