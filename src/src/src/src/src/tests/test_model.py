from src.battery_model import Battery

def test_creation():
    b = Battery("Test", 150, 4000, 80)
    assert b.energy_density_whkg == 150
    print("Test passed!")

if __name__ == "__main__":
    test_creation()
