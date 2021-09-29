import time
class Cycle:
    def __init__(self, cycle, period, GPIO, pin):
        self.cycle = cycle
        self.period = period
        self.GPIO = GPIO
        self.pin = pin
        GPIO.setmode(GPIO.BOARD)
        self.GPIO.setup(pin, GPIO.OUT)
    def on(self):
        ts = time.time()
        return (ts % self.cycle) < self.period
    def check_pin(self):
        if self.on():
            self.GPIO.output(self.pin, self.GPIO.HIGH)
            print(f'{self.pin} ON')
        else:
            self.GPIO.output(self.pin, self.GPIO.LOW)
            print(f'{self.pin} OFF')
