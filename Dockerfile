FROM python:3.7-slim

RUN python3.7 -m pip install pip

WORKDIR /
RUN pip install flask && pip install pytest
RUN pip install websockets
RUN pip install tzwhere
RUN pip install pytz
RUN pip install pandas
RUN pip install numpy
RUN pip install timezonefinder

COPY Controllers_1_0 /Controllers_1_0
COPY Tests /Tests
COPY Utils /Utils
COPY Websocket_1_0/distance_measurement_websocket.py /distance_measurements_websocket.py
COPY Websocket_1_0/live_measurements_websocket.py /live_measurements_websocket.py
COPY app.py /app.py
COPY config.py /config.py
COPY startup.py /startup.py
COPY Input_csv_files/timezone.csv /Input_csv_files/timezone.csv
COPY parsing_csv_program.py /parsing_csv_program.py

ENTRYPOINT ["python"]