class OldResistor:
    def __init__(self, ohms):
        self._ohms = ohms

    def get_ohms(self):
        return self._ohms

    def set_ohms(self, ohms):
        self._ohms = ohms

r0 = OldResistor(50e3)
print(f"Before: {r0.get_ohms()}")
r0.set_ohms(10e3)
print(f"After: {r0.get_ohms()}")

# bad example : 연산이 있는 경우 set,get 은 지저분하다
r0.set_ohms(r0.get_ohms() - 4e3)
assert r0.get_ohms() == 6e3

class Resistor:
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0

r1 = Resistor(50e3)
r1.ohms = 10e3
r1.ohms += 5e3


class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms

r2 = VoltageResistance(1e3)
print(f"Before: {r2.current:.2f} amps")

r2.voltage = 10  # volatage 를 바꿨더니만 current 가 바뀐다
print(f"After: {r2.current:.2f} amps")


class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError(f"{ohms} ohms must be > 0")
        self._ohms = ohms

r3 = BoundedResistance(1e3)
#r3.ohms = 0 # raise ValueError(f"{ohms} ohms must be > 0")

#BoundedResistance(-5) # ValueError: -5 ohms must be > 0


class FixedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, "_ohms"):
            raise AttributeError("Can't set attribute")
        self._ohms = ohms

r4 = FixedResistance(1e3)
#r4.ohms = 2e3 # AttributeError: Can't set attribute

class MysteriousResistor(Resistor):
    @property  # property 에서는 다른 어트리뷰트를 설정하면 안된다
    def ohms(self):
        self.voltage = self._ohms * self.current
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        self._ohms = ohms

r7 = MysteriousResistor(10)
r7.current = 0.01
print(f"Before: {r7.voltage:.2f}")
r7.ohms
print(f"After: {r7.voltage:.2f}")

