from typing import ClassVar

class DanmakuElem:
    @property
    def id(self) -> int: ...
    @property
    def progress(self) -> int: ...
    @property
    def mode(self) -> int: ...
    @property
    def fontsize(self) -> int: ...
    @property
    def color(self) -> int: ...
    @property
    def mid_hash(self) -> str: ...
    @property
    def content(self) -> str: ...
    @property
    def ctime(self) -> int: ...
    @property
    def action(self) -> str: ...
    @property
    def pool(self) -> int: ...
    @property
    def id_str(self) -> str: ...
    @property
    def attr(self) -> int: ...
    @property
    def animation(self) -> str: ...

class DmSegMobileReply:
    @property
    def elems(self) -> list[DanmakuElem]: ...
    @staticmethod
    def decode(data: bytes) -> DmSegMobileReply: ...

class CommentPosition:
    Scroll: ClassVar[CommentPosition]
    Top: ClassVar[CommentPosition]
    Bottom: ClassVar[CommentPosition]
    Reversed: ClassVar[CommentPosition]
    Normal: ClassVar[CommentPosition]
    Special: ClassVar[CommentPosition]

class Comment:
    timeline: float
    timestamp: int
    no: int
    comment: str
    pos: CommentPosition
    color: int
    size: float
    height: float
    width: float

def read_comments_from_xml(text: str, fontsize: float) -> list[Comment]: ...
def read_comments_from_protobuf(data: bytes, fontsize: float) -> list[Comment]: ...
