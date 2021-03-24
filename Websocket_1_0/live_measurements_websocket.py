import asyncio
import websockets
import re

from Utils.timezone_converter_utils import convert_timestamp_with_coordinates


async def live_measurement(websocket, path):
    user_input = await websocket.recv()

    regex_fmt = r'^name:(?P<name>(\w+)),lat:(?P<lat>-?\d*(.\d+)),lng:(?P<lng>-?\d*(.\d+)),timestamp:(?P<timestamp>-?\d*)'
    match = re.match(regex_fmt, user_input)

    name = str(match.group("name"))
    lat, lng = float(match.group("lat")), float(match.group("lng"))
    timestamp = float(match.group("timestamp"))

    msg = convert_timestamp_with_coordinates(lat, lng, timestamp)
    ret_msg = f"Hello {name}, your current timezone is {msg} !"
    await websocket.send(ret_msg)
    print(f"> {ret_msg}")


if __name__ == '__main__':
    start_server = websockets.serve(live_measurement, "0.0.0.0", 5001)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
