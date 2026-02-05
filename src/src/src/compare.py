from battery_model import na_ion, lifepo4

def print_comparison():
    print("2026 Battery Comparison:")
    print(na_ion)
    print(lifepo4)
    print(f"\nNa-ion advantage in cost: ${lifepo4.cost_per_kwh - na_ion.cost_per_kwh}/kWh")
    print(f"Cycle life ratio: {na_ion.cycle_life / lifepo4.cycle_life:.1f}x")

if __name__ == "__main__":
    print_comparison()
