import machine
from time import sleep_ms
from mpu6050 import MPU6050 # Import the MPU6050 class from the mpu6050.py file

# 1. I2C bus initialization
# Adapt the pins (sda, scl) to your wiring.
# Pico: sda=Pin(8), scl=Pin(9) is a common configuration for I2C0.
# ESP32: sda=Pin(21), scl=Pin(22) is the default configuration.
try:
    i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9), freq=400000)

    # 2. Create an instance of the MPU6050 object
    # The constructor handles the initial check and configuration.
    mpu = MPU6050(i2c)

    print("MPU6050 Found. Reading data...")

    # 3. Main loop to read data
    while True:
        # Retrieve all data in a single call (more efficient)
        all_data = mpu.get_all_data()

        accel = all_data['accel']
        gyro = all_data['gyro']
        temp = all_data['temp']
        
        # Display formatted data
        print(f"Temp: {temp:.2f}°C")
        print(f"Accel (m/s^2): X={accel[0]:.2f}, Y={accel[1]:.2f}, Z={accel[2]:.2f}")
        print(f"Gyro (°/s): X={gyro[0]:.2f}, Y={gyro[1]:.2f}, Z={gyro[2]:.2f}")
        
        sleep_ms(500)

except Exception as e:
    print(f"An error occurred: {e}")
