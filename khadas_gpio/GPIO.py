#  Copyright (c) 2023, Federico Rollo. All rights reserved.
#  Licensed under the MIT license. See LICENSE file in the project root for details.

import os

class GPIO:

    gpio_pin: int
    direction: str
    value: int

    def __init__(self, gpio_pin: int, set_input_direction: bool, value: int = -1):

        self.gpio_pin = gpio_pin

        check = os.popen(f'ls /sys/class/gpio/gpio{str(self.gpio_pin)} 2> /dev/null').read()

        if check == "":
            print("Initializing GPIO pin: " + str(self.gpio_pin))
            result = os.popen('echo ' + str(self.gpio_pin) + ' | sudo tee /sys/class/gpio/export').read()

            if str.strip(result) != str(self.gpio_pin):
                print("\033[91mGPIO cannot be exported: " + result + "\033[0m")
            else:
                self.set_direction(set_input_direction)
                if self.direction == 'out' and value != -1:
                    self.set_value(value)
                else:
                    print(f'\033[93mGPIO {str(self.gpio_pin)} in input direction: value not set.\033[0m')
        else:
            print(f'\033[93mGPIO {str(self.gpio_pin)} was already exported.\033[0m')
            self.get_info()


    def __del__(self):

        print("Deleting GPIO pin: " + str(self.gpio_pin))
        result = os.popen('echo ' + str(self.gpio_pin) + ' | sudo tee /sys/class/gpio/unexport').read()

        if str.strip(result) != str(self. gpio_pin):
            print("\033[91mGPIO cannot be unexported:\n" + result + "\033[0m")
        else:
            print("GPIO pin " + str(self.gpio_pin) + " unexported.")


    def set_direction(self, set_input_direction: bool) -> bool:
        
        if set_input_direction:
            self.direction = 'in'
        else:
            self.direction = 'out'
        result = os.popen('echo ' + self.direction + ' | sudo tee /sys/class/gpio/gpio' + str(self.gpio_pin) + '/direction').read()
        
        if str.strip(result) != self.direction:
            print("\033[91mGPIO direction cannot be set:\n" + result+ "\033[0m")
            return False

        print("GPIO direction set: " + self.direction)
        return True


    def set_value(self, value: int) -> bool:
        
        result = os.popen('echo ' + str(value) + ' | sudo tee /sys/class/gpio/gpio' + str(self.gpio_pin) + '/value').read()
        
        if str.strip(result) != str(value):
            print("\033[91mGPIO value cannot be set:\n" + result + "\033[0m")
            return False

        self.value = value
        print("GPIO value set: " + str(self.value))
        return True


    def get_direction(self) -> str:

        direction = os.popen('cat /sys/class/gpio/gpio' + str(self.gpio_pin) + '/direction').read()
        return str.strip(direction)


    def get_value(self) -> int:

        value = os.popen('cat /sys/class/gpio/gpio' + str(self.gpio_pin) + '/value').read()
        return int(str.strip(value))


    def get_info(self) -> None:
        print(f'\033[92mGPIO: {self.gpio_pin}\ndirection: {self.get_direction()}\nvalue: {self.get_value()}\033[0m')



        
