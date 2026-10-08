class DCMotorBackEMFCalculator:
    def __init__(self, supply_voltage, armature_current, armature_resistance):
        self.supply_voltage = supply_voltage
        self.armature_current = armature_current
        self.armature_resistance = armature_resistance

    def calculate_back_emf(self):
        # Back EMF equation: Eb = V - IaRa
        back_emf = self.supply_voltage - (
            self.armature_current * self.armature_resistance
        )
        return back_emf

    def display_result(self):
        back_emf = self.calculate_back_emf()

        print("----- DC Motor Back EMF Calculator -----")
        print(f"Supply Voltage       : {self.supply_voltage:.2f} V")
        print(f"Armature Current     : {self.armature_current:.2f} A")
        print(f"Armature Resistance  : {self.armature_resistance:.2f} Ohm")
        print(f"Back EMF             : {back_emf:.2f} V")


# Example values
supply_voltage = 230
armature_current = 10
armature_resistance = 0.5

calculator = DCMotorBackEMFCalculator(
    supply_voltage,
    armature_current,
    armature_resistance
)

calculator.display_result()
