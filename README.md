# MicroPython MPU6050 Driver

This repository provides a MicroPython module for the MPU6050 6-DoF Accelerometer and Gyro sensor. This module is **directly inspired by and converted from the Adafruit Arduino MPU6050 library**, available at [https://github.com/adafruit/Adafruit_MPU6050](https://github.com/adafruit/Adafruit_MPU6050).

## Overview

The `mpu6050.py` module facilitates communication with the MPU6050 sensor via the I2C protocol. It utilizes the **MicroPython `machine.I2C` module** for I2C communication.

**MicroPython** is a lean and efficient implementation of the Python 3 programming language that includes a small subset of the Python standard library and is optimized to run on microcontrollers and in constrained environments. You can find more information about MicroPython on its official website: [https://micropython.org/](https://micropython.org/).

## Documentation

A comprehensive **Doxygen** documentation for this module is provided in HTML format.
**Doxygen** is a documentation generator that extracts documentation from source code. You can learn more about Doxygen at [https://doxygen.nl](https://doxygen.nl).

The HTML documentation for this specific module is hosted on GitHub Pages: [https://roman-wolfensperger.github.io/MPU6050/](https://roman-wolfensperger.github.io/MPU6050/).

## Example Usage

An example file, `main.py`, is provided in the `example/` directory of this repository. This example demonstrates how to:
* Initialize the I2C bus on your microcontroller.
* Create an instance of the `MPU6050` class.
* Continuously read and print accelerometer, gyroscope, and temperature data from the sensor.

**Important Note for Thonny users:** When working with MicroPython in the [Thonny IDE](https://thonny.org/), ensure that you save the `mpu6050.py` module directly to your microcontroller device (e.g., as `main.py` or `mpu6050.py` on the device's filesystem) before attempting to run the example script. Do not run it from your computer's local filesystem if it's meant to interact with the connected device.

## How to Use the Module

To use the `mpu6050.py` module in your MicroPython project:

1.  **Transfer `mpu6050.py` to your microcontroller:**
    * Using Thonny, you can open `mpu6050.py`, then go to `File -> Save as... -> MicroPython device`. Save it as `mpu6050.py` in the root directory of your device.
    * Alternatively, use `ampy`, `rshell`, or other tools to copy the file to your microcontroller.

2.  **Import the module in your main script:**
    In your main MicroPython script (e.g., `main.py` on your device), you can import the `MPU6050` class:

    ```python
    import machine
    from mpu6050 import MPU6050
    from time import sleep_ms

    # Initialize I2C (adjust pins for your board)
    i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9), freq=400000)

    # Create MPU6050 object
    mpu = MPU6050(i2c)

    print("MPU6050 Initialized. Reading data...")

    while True:
        all_data = mpu.get_all_data()
        print(f"Temp: {all_data['temp']:.2f}°C")
        print(f"Accel (m/s^2): X={all_data['accel'][0]:.2f}, Y={all_data['accel'][1]:.2f}, Z={all_data['accel'][2]:.2f}")
        print(f"Gyro (°/s): X={all_data['gyro'][0]:.2f}, Y={all_data['gyro'][1]:.2f}, Z={all_data['gyro'][2]:.2f}")
        sleep_ms(500)
    ```

## Tested Environment

This MicroPython module has been tested using the following setup:
* **Microcontroller:** ESP32-WROOM
* **IDE:** [Thonny](https://thonny.org/) - Thonny is a user-friendly Python IDE designed for beginners, offering features like a simple debugger and MicroPython support.
* **MPU-6050 Module:** GY-521 MPU-6050 sensor module provided by Az-Delivery. You can find more details about this module here: [https://www.az-delivery.de/fr/products/gy-521-6-achsen-gyroskop-und-beschleunigungssensor](https://www.az-delivery.de/fr/products/gy-521-6-achsen-gyroskop-und-beschleunigungssensor).

## License

This project is released under the **BSD License**. Please refer to the `LICENSE.txt` file in this repository for more details.

Portions Copyright (c) 2019 Bryan Siepert for Adafruit Industries.
