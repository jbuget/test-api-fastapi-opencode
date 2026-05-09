from typing import List, Optional, Union
from dataclasses import dataclass, field

@dataclass
class FileSystemNode:
    id: str
    name: str

@dataclass
class Document(FileSystemNode):
    file_size: int = 0
    mime_type: str = ""

@dataclass
class Folder(FileSystemNode):
    parent_id: Optional[str] = None
    children: List[Union['Folder', 'Document']] = field(default_factory=list)

    def add_child(self, child: Union['Folder', 'Document']):
        self.children.append(child)
