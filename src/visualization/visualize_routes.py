import matplotlib.pyplot as plt
import os

def plot_simulation(drones, deliveries, nofly_zones, charging_stations):
    plt.figure(figsize=(12, 10))

    # Teslimat noktaları (mor kare)
    for d in deliveries:
        plt.scatter(d.pos[0], d.pos[1], c='purple', marker='s', s=70, label='Teslimat Noktası' if d.id == 1 else "")
        plt.text(d.pos[0], d.pos[1]+1, f"T{d.id}", fontsize=8, ha='center', color='purple')

    # No-fly zones (kırmızı alan)
    for nfz in nofly_zones:
        xs = [p[0] for p in nfz.coordinates]
        ys = [p[1] for p in nfz.coordinates]
        plt.fill(xs + [xs[0]], ys + [ys[0]], color='red', alpha=0.3, label='No-Fly Zone' if nfz.id == 1 else "")
        cx = sum(xs) / len(xs)
        cy = sum(ys) / len(ys)
        plt.text(cx, cy, f"NFZ {nfz.id}", fontsize=10, ha='center', color='darkred')

    # Renk paleti
    colors = ['blue', 'green', 'orange', 'darkred', 'brown']

    # Drone rotaları
    for idx, drone in enumerate(drones):
        color = colors[idx % len(colors)]
        plt.scatter(drone.position[0], drone.position[1], c='gold', edgecolors='black', marker='*', s=250,
                    label='Drone Başlangıç Noktası' if idx == 0 else "")
        plt.text(drone.position[0], drone.position[1]-2, f"Drone {drone.id}", ha='center', fontsize=9)

        if drone.route:
            full_path = [drone.position] + drone.route
            x, y = zip(*full_path)
            plt.plot(x, y, linestyle='-', marker='o', markersize=4, linewidth=2, color=color,
                     label=f"Drone {drone.id} rotası")

    plt.title("Drone Teslimat Rotaları ve No-Fly Zone'lar", fontsize=14)
    plt.xlabel("X Koordinatı", fontsize=12)
    plt.ylabel("Y Koordinatı", fontsize=12)
    plt.grid(True)
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.legend(fontsize=9, loc='upper right')
    plt.tight_layout()

    os.makedirs("screenshots", exist_ok=True)
    plt.savefig("screenshots/senaryo1_düzenli.png")
    plt.show()
