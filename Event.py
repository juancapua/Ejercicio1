

class Event:

    def __init__(self, timeStamp, deviceType, deviceId, contentId, eventType, currentPosition):
        self.timestamp = timeStamp
        self.deviceType = deviceType
        self.deviceId = deviceId
        self.contentId = contentId
        self.eventType = eventType
        self.currentPosition = currentPosition