class Battery:
    def __init__(self, chem, energy_density_whkg, cycle_life, cost_per_kwh):
        self.chem = chem
        self.energy_density_whkg = energy_density_whkg
        self.cycle_life = cycle_life
        self.cost_per_kwh = cost_per_kwh

    def __repr__(self):
        return f"{self.chem}: {self.energy_density_whkg} Wh/kg, {self.cycle_life} cycles, ${self.cost_per_kwh}/kWh"


# 2026 example instances
na_ion = Battery("Sodium-ion (CATL Naxtra)", 175, 8000, 85)  # approx mid-range
lifepo4 = Battery("Li-ion LFP", 190, 5000, 90)
