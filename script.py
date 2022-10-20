
from contextlib import nullcontext
import json
from Event import Event
import random
import time
from EventType import EventType
from DeviceType import DeviceType


def main():
    content = [1,2,3,4,5,6,7,8,9]
    devices = [DeviceType.ANDROID, DeviceType.DESKTOP, DeviceType.IOS, DeviceType.TV]
    events = [EventType.PLAY, EventType.STOP]
    users = [1,2,3,4,5,6,7,8,9,]
    playing = []
    running = True
    start = time.time()

    while(running):

        if(random.choice([True, False])):

            choice = random.choice(events)

            match choice:
                case EventType.PLAY:
                    #aca arrancamos a ver algo
                    userId = random.choice(users)
                    contentId = random.choice(content)
                    for x in playing:
                        if x.deviceId == userId and x.contentId == contentId:
                            pass
                        
                    eventStart = time.time()
                    event = Event(eventStart, random.choice(devices), userId, contentId, choice, 0)
                    playing.append(event)
                    print(json.dumps(event.__dict__))
                    pass
                case EventType.STOP:
                    userId = random.choice(users)
                    contentId = random.choice(content)
                    device = random.choice(devices)
                    eventStart = time.time()
                    for x in playing:
                        if x.deviceId == userId and x.contentId == contentId and x.deviceType == device:
                            playing.remove(x)
                            event = Event(eventStart, device, userId, contentId, choice, eventStart)
                            pass
                    pass 
        end = time.time()
        for x in playing:
            x.eventType = EventType.PLAYING
            x.currentPosition += end - x.currentPosition
            print(json.dumps(x.__dict__))
        
        if(end - start >= 30):
            running = False

                    




if __name__ == "__main__":
    main()