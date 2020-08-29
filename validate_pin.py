def validate_pin(pin):
    pinIsValidLength = len(pin) == 4 or len(pin) == 6
    if pinIsValidLength and pin.isnumeric():
        return True
    return False