from evdev import InputDevice, list_devices

devices = [InputDevice(path) for path in list_devices()]
for device in devices:
    print(f"Device path: {device.path}, Name: {device.name}, Phys: {device.phys}")
