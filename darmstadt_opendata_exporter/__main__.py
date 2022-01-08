#!/usr/bin/env python3

import requests
import time
import sys
from datetime import datetime
from prometheus_client import start_http_server, Gauge, Counter, REGISTRY


INTERVAL = 60

UNIT = {
    "µg/m³": "micrograms_per_cubic_meter",
    "mg/m³": "milligrams_per_cubic_meter",
}

SENSOR_MAPPING = {
    'dust_pm2.5': 'pm2_5',
    'dust_pm10': 'pm10',
}

METRICS = {}


for name in list(REGISTRY._names_to_collectors.values()):
    try:
        REGISTRY.unregister(name)
    except KeyError:
        pass

def now() -> str:
    # 2021-07-05T22:44:44.036Z
    date_format = "%Y-%m-%dT%H:%M:%S.000Z"
    return datetime.utcnow().strftime(date_format)


def fetch(url: str) -> dict:
    response = requests.get(url, params={"date": now()})
    if response.status_code != 200:
        print(f"HTTP {response.status_code} for URL {response.url}", file=sys.stderr)
        return {}
    return response.json()



def get_or_create_metric(metric, prefix, sensor, description, unit, labels):
    if sensor in SENSOR_MAPPING:
        sensor = SENSOR_MAPPING[sensor]

    if sensor in METRICS:
        return METRICS[sensor]

    namespace = "darmstadt"

    unit = UNIT[unit]
    _metric = metric(f'{namespace}_{prefix}_{sensor}_{unit}', description, labels)

    METRICS[sensor] = _metric
    return _metric


def update_environment(events):
    for sensor, measurements in events[0].items():
        if not isinstance(measurements, dict):
            continue
        for measurement in measurements.values():
            if not isinstance(measurement, dict):
                continue
            metric = get_or_create_metric(
                Gauge,
                "environment",
                measurement["sensorLabel"],
                f"Environment measurement for {measurement['sensorLabel']}",
                measurement["unit"],
                [
                    #'lat',
                    #'lon',
                    'sensor'
                ]
            )

            value = float(measurement['value'])

            labels = {
                #"lat": measurement["lat"],
                #"lon": measurement["lon"],
                "sensor": measurement["SID"]
            }

            metric.labels(**labels).set(value)


def update_traffic(events):
    for direction, hours in events[0].keys():
        # unclear and probably useless data format (hourly counters?!)
        pass



ENDPOINTS = [
    ("https://datenplattform.darmstadt.de/EnvironmentGeneric/events", update_environment),
    #("https://datenplattform.darmstadt.de/TrafficDirections/events", update_traffic),
]

def update() -> None:
    for url, callback in ENDPOINTS:
        # the events index > 0 holds historic data
        response = fetch(url)
        try:
            events = response["events"]
            callback(events)
        except KeyError:
            print(f"Missing 'events' field in response for URI {url}", file=sys.stderr)
            continue


def main() -> None:
    start_http_server(64283)

    while True:
        update()
        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()
