import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
charge_pin = 4  # GPIO pin to charge the capacitor
measure_pin = 5  # GPIO pin to measure the voltage across the capacitor

GPIO.setup(charge_pin, GPIO.OUT)
GPIO.setup(measure_pin, GPIO.IN)


def discharge():
    GPIO.output(charge_pin, GPIO.LOW)
    time.sleep(1)  # Wait for the capacitor to fully discharge


def measure_capacitance(resistor_value):
    discharge()
    GPIO.output(charge_pin, GPIO.HIGH)
    start_time = time.time()
    while GPIO.input(measure_pin) == GPIO.LOW:
        pass

    elapsed_time = time.time() - start_time
    capacitance = elapsed_time / resistor_value
    return capacitance * 1e12  # in Pf


resistor_value = 237_000
capacitance = measure_capacitance(resistor_value)
print(f"Capacitance: {capacitance:.2f} pF")

# Clean up the GPIO
GPIO.cleanup()
