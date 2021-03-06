# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# DO NOT EDIT THIS FILE!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
from unittest.mock import MagicMock, patch

sleep = MagicMock()
MockRPi = MagicMock()

MockRPi.GPIO.LOW = 0
MockRPi.GPIO.HIGH = 1

pin_status = {}


def clock_generator():
    value = True
    while True:
        yield MockRPi.GPIO.LOW if value else MockRPi.GPIO.HIGH
        value = not value


def clock_pin(pin):
    pin_status.setdefault(pin, clock_generator())
    return next(pin_status[pin])


modules = {
    "RPi": MockRPi,
    "RPi.GPIO": MockRPi.GPIO,
    "time.sleep": sleep,
}
patcher = patch.dict("sys.modules", modules)
