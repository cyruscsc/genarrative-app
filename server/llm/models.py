from enum import Enum
from pydantic import BaseModel


class MessageRole(str, Enum):
    assistant = "assistant"
    system = "system"
    user = "user"


class MessageType(str, Enum):
    text = "text"
    image_url = "image_url"


class TextMessage(BaseModel):
    type: MessageType = MessageType.text
    text: str


class ImageMessage(BaseModel):
    type: MessageType = MessageType.image_url
    image_url: str
