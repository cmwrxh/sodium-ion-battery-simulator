import matplotlib.pyplot as plt
from battery_model import na_ion, lifepo4

def plot_metrics():
    labels = ['Energy Density (Wh/kg)', 'Cycle Life', 'Cost ($/kWh)']
    na_vals = [na_ion.energy_density_whkg, na_ion.cycle_life, na_ion.cost_per_kwh]
    li_vals = [lifepo4.energy_density_whkg, lifepo4.cycle_life, lifepo4.cost_per_kwh]

    x = range(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    ax.bar([i - width/2 for i in x], na_vals, width, label='Sodium-ion')
    ax.bar([i + width/2 for i in x], li_vals, width, label='Li-ion LFP')

    ax.set_ylabel('Value')
    ax.set_title('Sodium vs Lithium-Ion (2026)')
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=15)
    ax.legend()

    plt.tight_layout()
    plt.savefig('comparison_plot.png')
    plt.show()

if __name__ == "__main__":
    plot_metrics()
