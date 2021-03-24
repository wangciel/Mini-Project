import asyncio
import websockets
import re
import time

from Utils.distance_measurement_util import haversine_formula

client_list = {}


async def distance_measurement(websocket, path):
    user_input = await websocket.recv()
    print(f"< {user_input}")

    regex_fmt = r'^name:(?P<name>(\w+)),lat:(?P<lat>-?\d*(.\d+)),lng:(?P<lng>-?\d*(.\d+))'
    match = re.match(regex_fmt, user_input)

    name = str(match.group("name"))
    lat, lng = float(match.group("lat")), float(match.group("lng"))

    if str(name) in client_list:
        client_list[name]["time"].append(time.time())
        client_list[name]["lat"].append(lat)
        client_list[name]["lng"].append(lng)

    else:
        client_list[name] = {"time": [time.time()], "lat": [lat], "lng": [lng]}

    if len(client_list[name]['time']) < 2:
        greeting = f"Hello {name}, your are the first time record your location!"
        await websocket.send(greeting)
    else:
        size = len(client_list[name]["time"]) - 1

        lat1 = client_list[name]["lat"][size - 1]
        lng1 = client_list[name]["lng"][size - 1]
        lat2 = client_list[name]["lat"][size]
        lng2 = client_list[name]["lng"][size]

        distance = haversine_formula(lat1, lng1, lat2, lng2)

        greeting = f"Hello {name}, your current travel distance between last time record is {distance} km!"
        await websocket.send(greeting)
        print(f"> {greeting}")


if __name__ == '__main__':
    start_server = websockets.serve(distance_measurement, "0.0.0.0", 5002)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
