"""
Detect BTHome v2 advertisements

Based on Bleak's detection_callback.py example script.
"""

import argparse
import asyncio
import binascii
import logging

from bleak import BleakScanner
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData
from Cryptodome.Cipher import AES
from kaitai.bthome_service_data import BthomeServiceData

logger = logging.getLogger(__name__)

def decrypt_payload(payload: bytes, mic: bytes, bindkey: bytes, nonce: bytes):
    cipher = AES.new(bindkey, AES.MODE_CCM, nonce=nonce, mac_len=4)
    try:
        return cipher.decrypt_and_verify(payload, mic)
    except ValueError as error:
        print()
        print("Decryption failed:", error)
        return None

def simple_callback(device: BLEDevice, advertisement_data: AdvertisementData):
    try:
        service_data = advertisement_data.service_data[
            "0000fcd2-0000-1000-8000-00805f9b34fb"
        ]
    except KeyError:
        return  # Ignore non-BTHome v2 service data

    print("name:", device.name)
    bthome_data = BthomeServiceData.from_bytes(service_data)
    if bthome_data.device_information.encryption:
        ciphertext = bthome_data.ciphertext
        counter = binascii.b2a_hex(bthome_data.counter.to_bytes(4, "big")).decode("utf-8")
        mic = bthome_data.mic.to_bytes(4, "big")
        print("Ciphertext: ", ciphertext.hex())
        print("Counter: ", counter)
        print("Message Integrity Check: ", mic.hex())
        nonce = binascii.unhexlify("".join([device.address.replace(":", ""), "d2fc", binascii.b2a_hex(service_data[0:1]).decode("utf-8"), counter]))
        print("Nonce: ", nonce.hex())
        decrypted_data = decrypt_payload(ciphertext, mic, bytes.fromhex(args.bindkey), nonce)
        print("Decrypted data:", decrypted_data.hex())
        # Treat the data as unencrypted BTHome data without MAC address
        bthome_service_data = bytearray([service_data[0] & 0xfc])
        bthome_service_data.extend(decrypted_data)
        bthome_service_data = BthomeServiceData.from_bytes(bthome_service_data)
        show_measurements(bthome_service_data.measurement)
    else:
        show_measurements(bthome_data.measurement)

def show_measurements(measurements):
    for measurement in measurements:
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
        "--bindkey",
        help="bindkey to decrypt encrypted BTHome messages",
    )

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
