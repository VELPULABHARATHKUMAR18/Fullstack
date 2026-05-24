# Create a class Person whose constructor takes age as an argument. Raise a
# ValueError if the age is less than 0.



# ============================================================
# ENCAPSULATION QUESTIONS (1-10)
# ============================================================

# 1. BankAccount class
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # private

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

acc = BankAccount("ACC001", 1000)
acc.deposit(500)
acc.withdraw(200)
print("Balance:", acc.get_balance())

# Direct access attempt
try:
    acc.__balance = 99999  # This does NOT change the real private attribute
    print("Direct set appeared to work, but real balance:", acc.get_balance())
except:
    print("Cannot access private attribute.")


# ============================================================
# 2. Student class with marks validation
class Student:
    def __init__(self, name):
        self.name = name
        self.__marks = 0

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            print(f"Marks set to {self.__marks}")
        else:
            print("Invalid marks! Must be between 0 and 100.")

    def get_marks(self):
        return self.__marks

s = Student("Alice")
s.set_marks(85)
s.set_marks(150)   # Invalid
print("Marks:", s.get_marks())

# Direct access attempt
try:
    s.__marks = 200
    print("Direct set appeared to work, but real marks:", s.get_marks())
except:
    print("Cannot access private attribute.")


# ============================================================
# 3. SecureFile class
class SecureFile:
    def __init__(self, content, password):
        self.__content = content
        self.__password = password
        self.__log = []

    def read(self, password):
        if password == self.__password:
            return self.__content
        else:
            self.__log.append("Unauthorized attempt")
            return "Access Denied!"

    def get_log_count(self):
        return f"Total unauthorized attempts: {len(self.__log)}"

sf = SecureFile("Secret Data", "pass123")
print(sf.read("wrongpass"))
print(sf.read("wrongpass"))
print(sf.read("pass123"))
print(sf.get_log_count())
#

# ============================================================
# 4. Employee class with hidden salary
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
        self.__access_log = 0

    def get_salary(self):
        self.__access_log += 1
        print(f"Salary accessed. Total accesses: {self.__access_log}")
        return self.__salary

    def update_salary(self, new_salary):
        if new_salary > self.__salary:
            self.__salary = new_salary
            print(f"Salary updated to {self.__salary}")
        else:
            print("New salary must be higher than current salary.")

emp = Employee("Bob", 50000)
print(emp.get_salary())
emp.update_salary(60000)
emp.update_salary(40000)  # Not allowed
print(emp.get_salary())


# ============================================================
# 5. Product class with price and discount validation
class Product:
    def __init__(self, price, discount):
        self.__price = price
        self.__discount = discount

    def __calculate_final_price(self):     # private method
        return self.__price - (self.__price * self.__discount / 100)

    def get_final_price(self):
        if self.__price < 0:
            print("Price cannot be negative.")
            return None
        if self.__discount > 70:
            print("Discount cannot exceed 70%.")
            return None
        return self.__calculate_final_price()

p = Product(1000, 30)
print("Final Price:", p.get_final_price())

p2 = Product(-500, 30)
print(p2.get_final_price())

p3 = Product(1000, 80)
print(p3.get_final_price())


# ============================================================
# 6. Character class with health limits
class Character:
    def __init__(self, max_health):
        self.__max_health = max_health
        self.__health = max_health

    def damage(self, points):
        self.__health -= points
        if self.__health < 0:
            self.__health = 0
        print(f"Damaged! Current health: {self.__health}")

    def heal(self, points):
        self.__health += points
        if self.__health > self.__max_health:
            self.__health = self.__max_health
        print(f"Healed! Current health: {self.__health}")

    @property
    def health(self):
        return self.__health

c = Character(100)
c.damage(30)
c.heal(20)
c.damage(200)  # Goes to 0, not negative
c.heal(500)    # Capped at max


# ============================================================
# 7. Engine and Car class
class Engine:
    def __init__(self):
        self.__temperature = 0

    def start(self):
        self.__temperature = 90
        print(f"Engine started. Temp: {self.__temperature}")

    def cool(self):
        self.__temperature = 30
        print(f"Engine cooled. Temp: {self.__temperature}")

class Car:
    def __init__(self):
        self.__engine = Engine()  # Engine is private

    def start_car(self):
        self.__engine.start()

    def cool_engine(self):
        self.__engine.cool()

car = Car()
car.start_car()
car.cool_engine()

# Direct access attempt - dangerous and blocked
try:
    car.__engine.temperature = 9999
    print("Direct access worked!")
except AttributeError:
    print("Cannot directly access engine - encapsulation works!")


# ============================================================
# 8. ShoppingCart class
class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add(self, item):
        self.__items.append(item)
        print(f"Added: {item}")

    def remove(self, item):
        if item in self.__items:
            self.__items.remove(item)
            print(f"Removed: {item}")
        else:
            print(f"{item} not found in cart.")

    def get_items(self):
        return list(self.__items)  # Returns a copy, not the original list

cart = ShoppingCart()
cart.add("Apple")
cart.add("Banana")
cart.remove("Apple")
print("Cart items:", cart.get_items())

# Getting a copy means outside changes don't affect the cart
copy = cart.get_items()
copy.append("Mango")
print("Cart after outside modification:", cart.get_items())  # Unchanged


# ============================================================
# 9. Attendance - Wrong vs Right way

# WRONG WAY
class AttendanceBad:
    def __init__(self):
        self.attendance = []  # Public - anyone can modify

bad = AttendanceBad()
bad.attendance.append("Monday")
bad.attendance.append("Monday")   # Duplicate - no control!
bad.attendance.remove("Monday")   # Can delete directly!
print("Bad attendance:", bad.attendance)

# RIGHT WAY
class AttendanceGood:
    def __init__(self):
        self.__attendance = []  # Private

    def mark(self, day):
        if day not in self.__attendance:
            self.__attendance.append(day)
            print(f"Attendance marked for {day}")
        else:
            print(f"Already marked for {day}")

    def get_attendance(self):
        return list(self.__attendance)

good = AttendanceGood()
good.mark("Monday")
good.mark("Monday")   # Duplicate blocked
good.mark("Tuesday")
print("Good attendance:", good.get_attendance())


# ============================================================
# 10. @property and @setter - Python encapsulation pitfalls
class Temperature:
    def __init__(self, value):
        self._value = value   # _ means "protected by convention"

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value < -273:
            print("Temperature below absolute zero is invalid!")
        else:
            self._value = new_value

# Correct usage
t = Temperature(25)
print("Temp:", t.value)
t.value = 100
print("Temp:", t.value)
t.value = -300   # Blocked by validation

# PITFALL 1: Forgetting underscore breaks encapsulation
class BadTemp:
    def __init__(self, value):
        self.value = value   # No underscore - conflicts with @property!

# PITFALL 2: Setter without validation
class NoValidationTemp:
    def __init__(self):
        self._value = 0

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v   # No check - anyone can set any value!

nv = NoValidationTemp()
nv.value = -99999   # No error raised - dangerous!
print("No validation temp:", nv.value)


============================================================
ABSTRACTION QUESTIONS (11-20)
============================================================

from abc import ABC, abstractmethod
import math

# 11. Abstract Shape with Circle, Rectangle, Triangle
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h
#
    def perimeter(self):
        return 2 * (self.w + self.h)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return round(math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c)), 2)

    def perimeter(self):
        return self.a + self.b + self.c

shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]
for shape in shapes:
    print(f"{shape.__class__.__name__} -> Area: {shape.area()}, Perimeter: {shape.perimeter()}")

# What if subclass doesn't implement a method?
try:
    class BadShape(Shape):
        def area(self):
            return 0
        # Missing perimeter!
    b = BadShape()
except TypeError as e:
    print(f"Error: {e}")


# ============================================================
# 12. Abstract PaymentGateway
class PaymentGateway(ABC):
    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

class UPIPayment(PaymentGateway):
    def authenticate(self):
        print("UPI: Authenticated via UPI PIN")

    def pay(self, amount):
        print(f"UPI: Paid ₹{amount}")

    def refund(self, amount):
        print(f"UPI: Refunded ₹{amount}")

class CardPayment(PaymentGateway):
    def authenticate(self):
        print("Card: Authenticated via OTP")

    def pay(self, amount):
        print(f"Card: Paid ₹{amount}")

    def refund(self, amount):
        print(f"Card: Refunded ₹{amount}")

class NetBankingPayment(PaymentGateway):
    def authenticate(self):
        print("NetBanking: Authenticated via Net Banking ID")

    def pay(self, amount):
        print(f"NetBanking: Paid ₹{amount}")

    def refund(self, amount):
        print(f"NetBanking: Refunded ₹{amount}")

# Main program doesn't care about payment type
for payment in [UPIPayment(), CardPayment(), NetBankingPayment()]:
    payment.authenticate()
    payment.pay(500)
    payment.refund(100)
    print()


# ============================================================
# 13. Abstract VehicleControl
class VehicleControl(ABC):
    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def brake(self):
        pass

    @abstractmethod
    def steer(self, direction):
        pass

class CarControl(VehicleControl):
    def accelerate(self):
        print("Car: Accelerating smoothly")

    def brake(self):
        print("Car: Braking with ABS")

    def steer(self, direction):
        print(f"Car: Steering {direction}")

class BikeControl(VehicleControl):
    def accelerate(self):
        print("Bike: Accelerating fast")

    def brake(self):
        print("Bike: Hand brake applied")

    def steer(self, direction):
        print(f"Bike: Leaning {direction}")

class TruckControl(VehicleControl):
    def accelerate(self):
        print("Truck: Slowly accelerating")

    def brake(self):
        print("Truck: Air brakes applied")

    def steer(self, direction):
        print(f"Truck: Wide turn {direction}")

for vehicle in [CarControl(), BikeControl(), TruckControl()]:
    vehicle.accelerate()
    vehicle.brake()
    vehicle.steer("left")
    print()


============================================================
14. Abstract DatabaseDriver
class DatabaseDriver(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute(self, query):
        pass

    @abstractmethod
    def close(self):
        pass

class MySQLDriver(DatabaseDriver):
    def connect(self):
        print("MySQL: Connected")

    def execute(self, query):
        print(f"MySQL: Executing -> {query}")

    def close(self):
        print("MySQL: Connection closed")

class PostgresDriver(DatabaseDriver):
    def connect(self):
        print("Postgres: Connected")

    def execute(self, query):
        print(f"Postgres: Executing -> {query}")

    def close(self):
        print("Postgres: Connection closed")

class SQLiteDriver(DatabaseDriver):
    def connect(self):
        print("SQLite: Connected")

    def execute(self, query):
        print(f"SQLite: Executing -> {query}")

    def close(self):
        print("SQLite: Connection closed")
#
# Main code works the same for any database
def run_query(driver: DatabaseDriver, query):
    driver.connect()
    driver.execute(query)
    driver.close()

for driver in [MySQLDriver(), PostgresDriver(), SQLiteDriver()]:
    run_query(driver, "SELECT * FROM users")
    print()


============================================================
15. Abstract ReportGenerator
class ReportGenerator(ABC):
    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def export(self):
        pass

class PDFReport(ReportGenerator):
    def load_data(self):
        print("PDF: Loading data...")

    def process(self):
        print("PDF: Processing data...")

    def export(self):
        print("PDF: Exporting as PDF file.")

class ExcelReport(ReportGenerator):
    def load_data(self):
        print("Excel: Loading data...")

    def process(self):
        print("Excel: Processing data...")

    def export(self):
        print("Excel: Exporting as Excel file.")

for report in [PDFReport(), ExcelReport()]:
    report.load_data()
    report.process()
    report.export()
    print()


# ============================================================
# 16. Abstract RobotCommand
class RobotCommand(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class PickCommand(RobotCommand):
    def execute(self):
        print("Robot: Picking up object")

    def undo(self):
        print("Robot: Putting object back")

class PlaceCommand(RobotCommand):
    def execute(self):
        print("Robot: Placing object")

    def undo(self):
        print("Robot: Removing placed object")

class MoveCommand(RobotCommand):
    def execute(self):
        print("Robot: Moving forward")

    def undo(self):
        print("Robot: Moving backward")

for cmd in [PickCommand(), PlaceCommand(), MoveCommand()]:
    cmd.execute()
    cmd.undo()
    print()


# ============================================================
# 17. Abstract MLModel
class MLModel(ABC):
    @abstractmethod
    def train(self, data):
        pass

    @abstractmethod
    def predict(self, x):
        pass

    @abstractmethod
    def evaluate(self, test_set):
        pass

class LinearRegressionModel(MLModel):
    def train(self, data):
        print("LinearRegression: Training with linear equations")

    def predict(self, x):
        print(f"LinearRegression: Predicting for {x}")

    def evaluate(self, test_set):
        print("LinearRegression: Evaluating with MSE")

class DecisionTreeModel(MLModel):
    def train(self, data):
        print("DecisionTree: Training by splitting nodes")

    def predict(self, x):
        print(f"DecisionTree: Predicting for {x}")

    def evaluate(self, test_set):
        print("DecisionTree: Evaluating with accuracy score")

# Generic training loop - works for any model
def generic_training(model: MLModel):
    model.train("training data")
    model.predict("new input")
    model.evaluate("test data")

for model in [LinearRegressionModel(), DecisionTreeModel()]:
    generic_training(model)
    print()


# ============================================================
# 18. Without vs With abstraction - Notifier

# WITHOUT ABSTRACTION - messy if/else
def send_notification_bad(type, message):
    if type == "email":
        print(f"Email: Sending '{message}'")
    elif type == "sms":
        print(f"SMS: Sending '{message}'")
    elif type == "push":
        print(f"Push: Sending '{message}'")
    else:
        print("Unknown type")

send_notification_bad("email", "Hello!")
send_notification_bad("sms", "Hello!")
send_notification_bad("push", "Hello!")

# WITH ABSTRACTION - clean
class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailSender(Notifier):
    def send(self, message):
        print(f"Email: Sending '{message}'")

class SMSSender(Notifier):
    def send(self, message):
        print(f"SMS: Sending '{message}'")

class PushSender(Notifier):
    def send(self, message):
        print(f"Push: Sending '{message}'")

for notifier in [EmailSender(), SMSSender(), PushSender()]:
    notifier.send("Hello!")


# ============================================================
# 19. Abstract MediaPlayer
class MediaPlayer(ABC):
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class MP3Player(MediaPlayer):
    def load(self):
        print("MP3: Loading MP3 file")

    def play(self):
        print("MP3: Playing MP3")

    def stop(self):
        print("MP3: Stopped")

class WAVPlayer(MediaPlayer):
    def load(self):
        print("WAV: Loading WAV file")

    def play(self):
        print("WAV: Playing WAV")

    def stop(self):
        print("WAV: Stopped")

class AACPlayer(MediaPlayer):
    def load(self):
        print("AAC: Loading AAC file")

    def play(self):
        print("AAC: Playing AAC")

    def stop(self):
        print("AAC: Stopped")

for player in [MP3Player(), WAVPlayer(), AACPlayer()]:
    player.load()
    player.play()
    player.stop()
    print()


# ============================================================
# 20. Abstract Sensor
class Sensor(ABC):
    def __init__(self, calibration_factor):
        self.__calibration_factor = calibration_factor
        self.__raw_value = 0

    def _set_raw(self, value):
        self.__raw_value = value

    def _get_calibrated(self):
        return self.__raw_value * self.__calibration_factor

    @abstractmethod
    def read_value(self):
        pass

    @abstractmethod
    def calibrate(self):
        pass

    def get_reading(self):
        self.read_value()
        return self._get_calibrated()

class TemperatureSensor(Sensor):
    def read_value(self):
        self._set_raw(25)   # Simulated raw reading

    def calibrate(self):
        print("TemperatureSensor: Calibrated")

class PressureSensor(Sensor):
    def read_value(self):
        self._set_raw(101)

    def calibrate(self):
        print("PressureSensor: Calibrated")

class HumiditySensor(Sensor):
    def read_value(self):
        self._set_raw(60)

    def calibrate(self):
        print("HumiditySensor: Calibrated")

for sensor in [TemperatureSensor(1.1), PressureSensor(1.0), HumiditySensor(0.95)]:
    sensor.calibrate()
    print(f"{sensor.__class__.__name__} Reading: {sensor.get_reading()}")
    print()
