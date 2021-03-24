import asyncio
import websockets


async def send_first_record():
    url = "ws://127.0.0.1:5002"
    async with websockets.connect(url) as websocket:
        lat, lng = 32.0004311, -103.548851
        message = 'name:%s,lat:%f,lng:%f' % ("Client01", lat, lng)
        await websocket.send(message)

        greeting = await websocket.recv()
        print(f"< {greeting}")


async def send_second_record():
    url = "ws://127.0.0.1:5002"
    async with websockets.connect(url) as websocket:
        lat, lng = 33.374939, -103.6041946
        message = 'name:%s,lat:%f,lng:%f' % ("Client01", lat, lng)
        await websocket.send(message)

        greeting = await websocket.recv()
        print(f"< {greeting}")


async def send_third_record():
    url = "ws://127.0.0.1:5002"
    async with websockets.connect(url) as websocket:
        lat, lng = 33.374939, -103.6041946
        message = 'name:%s,lat:%f,lng:%f' % ("Client02", lat, lng)
        await websocket.send(message)

        greeting = await websocket.recv()
        print(f"< {greeting}")


asyncio.get_event_loop().run_until_complete(send_first_record())
asyncio.get_event_loop().run_until_complete(send_second_record())
asyncio.get_event_loop().run_until_complete(send_second_record())
asyncio.get_event_loop().run_until_complete(send_third_record())
