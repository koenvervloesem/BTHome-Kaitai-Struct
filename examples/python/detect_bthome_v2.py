"""
Detect unencrypted BTHome v2 advertisements

Based on Bleak's detection_callback.py example script.
"""

import argparse
import asyncio
import logging

from bleak import BleakScanner
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData
from kaitai.bthome_service_data import BthomeServiceData

logger = logging.getLogger(__name__)


def simple_callback(device: BLEDevice, advertisement_data: AdvertisementData):
    try:
        service_data = advertisement_data.service_data[
            "0000fcd2-0000-1000-8000-00805f9b34fb"
        ]
    except KeyError:
        return  # Ignore non-BTHome v2 service data

    print("name:", device.name)
    bthome_data = BthomeServiceData.from_bytes(service_data)
    for measurement in bthome_data.measurements:
        print("type:", measurement.object_id.name)
        for attribute, value in vars(measurement.data).items():
            if not (attribute.startswith("_") or attribute == "value"):
                try:
                    print("value:", value.value)
                except AttributeError:  # No composite type
                    print("value:", value)
        try:
            print("unit:", measurement.data.unit)
        except AttributeError:  # Data type has no unit
            pass


async def main(args: argparse.Namespace):
    scanner = BleakScanner(
        simple_callback, args.services, cb=dict(use_bdaddr=args.macos_use_bdaddr)
    )

    while True:
        logger.debug("(re)starting scanner")
        await scanner.start()
        await asyncio.sleep(5.0)
        await scanner.stop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--macos-use-bdaddr",
        action="store_true",
        help="when true use Bluetooth address instead of UUID on macOS",
    )

    parser.add_argument(
        "--services",
        metavar="<uuid>",
        nargs="*",
        help="UUIDs of one or more services to filter for",
    )

    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        help="sets the logging level to debug",
    )

    args = parser.parse_args()

    log_level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="%(asctime)-15s %(name)-8s %(levelname)s: %(message)s",
    )

    asyncio.run(main(args))
