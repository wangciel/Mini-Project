import asyncio
import websockets


async def hello():
    url = "ws://127.0.0.1:5001"
    async with websockets.connect(url) as websocket:
        lat, lng = -33.865143, 151.209900
        timestamp = 1480933800
        message = 'name:%s,lat:%f,lng:%f,timestamp:%f' % ("Client01", lat, lng, timestamp)
        await websocket.send(message)

        greeting = await websocket.recv()
        print(f"< {greeting}")


asyncio.get_event_loop().run_until_complete(hello())
