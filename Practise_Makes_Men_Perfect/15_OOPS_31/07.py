##Exercise 7: Light Class with On/Off State Toggle
##Problem Statement: Write a Python program to create a Light class with three methods: turn_on() that switches the light on, turn_off() that switches it off, and status() that reports whether the light is currently on or off.

class Light:
    def __init__(self):
        self.light = 'OFF'
    def turn_on(self):
        self.light = 'ON'
    def turn_off(self):
        self.light = 'OFF'
    def status(self):
        return self.light

l1 = Light()
print(l1.status())
