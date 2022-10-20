from enum import Enum

class EventType(str, Enum):
    PLAY = "play"
    PLAYING = "playing"
    STOP = "stop"
