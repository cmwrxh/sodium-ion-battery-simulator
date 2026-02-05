import numpy as np
from battery_model import Battery

def cost_sweep():
    costs = np.linspace(50, 120, 5)  # potential $/kWh range
    for c in costs:
        na = Battery("Na-ion", 175, 8000, c)
        print(f"At ${c:.0f}/kWh: {na}")

if __name__ == "__main__":
    cost_sweep()
