from utils.helpers import is_within_time_window, calculate_distance
from algorithms.a_star import a_star
from algorithms.genetic_algorithm import genetic_algorithm
from visualization.visualize_routes import plot_simulation
from models.drone import Drone
from models.teslimat_noktasi import TeslimatNoktasi
from models.nofly_zone import NoFlyZone
from metrics.performance import calculate_performance_metrics

def main():
    current_time = "00:45"
    current_minute = 0 * 60 + 45

    drones_data = [
        {"id": 1, "max_weight": 4.0, "battery": 12000, "speed": 8.0, "start_pos": (10, 10)},
        {"id": 2, "max_weight": 3.5, "battery": 10000, "speed": 10.0, "start_pos": (20, 30)},
        {"id": 3, "max_weight": 5.0, "battery": 15000, "speed": 7.0, "start_pos": (50, 50)},
        {"id": 4, "max_weight": 2.0, "battery": 8000, "speed": 12.0, "start_pos": (80, 20)},
        {"id": 5, "max_weight": 6.0, "battery": 20000, "speed": 5.0, "start_pos": (40, 70)}
    ]

    deliveries_data = [
        {"id": 1, "pos": (15, 25), "weight": 1.5, "priority": 3, "time_window": (0, 60)},
        {"id": 2, "pos": (30, 40), "weight": 2.0, "priority": 5, "time_window": (0, 30)},
        {"id": 3, "pos": (70, 80), "weight": 3.0, "priority": 2, "time_window": (20, 80)},
        {"id": 4, "pos": (90, 10), "weight": 1.0, "priority": 4, "time_window": (10, 40)},
        {"id": 5, "pos": (45, 60), "weight": 4.0, "priority": 1, "time_window": (30, 90)},
        {"id": 6, "pos": (25, 15), "weight": 2.5, "priority": 3, "time_window": (0, 50)},
        {"id": 7, "pos": (60, 30), "weight": 1.0, "priority": 5, "time_window": (5, 25)},
        {"id": 8, "pos": (85, 90), "weight": 3.5, "priority": 2, "time_window": (40, 100)},
        {"id": 9, "pos": (10, 80), "weight": 2.0, "priority": 4, "time_window": (15, 45)},
        {"id": 10, "pos": (95, 50), "weight": 1.5, "priority": 3, "time_window": (0, 60)},
        {"id": 11, "pos": (55, 20), "weight": 0.5, "priority": 5, "time_window": (0, 20)},
        {"id": 12, "pos": (35, 75), "weight": 2.0, "priority": 1, "time_window": (50, 120)},
        {"id": 13, "pos": (75, 40), "weight": 3.0, "priority": 3, "time_window": (10, 50)},
        {"id": 14, "pos": (20, 90), "weight": 1.5, "priority": 4, "time_window": (30, 70)},
        {"id": 15, "pos": (65, 65), "weight": 4.5, "priority": 2, "time_window": (25, 75)},
        {"id": 16, "pos": (40, 10), "weight": 2.0, "priority": 5, "time_window": (0, 30)},
        {"id": 17, "pos": (5, 50), "weight": 1.0, "priority": 3, "time_window": (15, 55)},
        {"id": 18, "pos": (50, 85), "weight": 3.0, "priority": 1, "time_window": (60, 100)},
        {"id": 19, "pos": (80, 70), "weight": 2.5, "priority": 4, "time_window": (20, 60)},
        {"id": 20, "pos": (30, 55), "weight": 1.5, "priority": 2, "time_window": (40, 80)}
    ]

    nofly_data = [
        {"id": 1, "coordinates": [(40, 30), (60, 30), (60, 50), (40, 50)], "active_time": (0, 120)},
        {"id": 2, "coordinates": [(70, 10), (90, 10), (90, 30), (70, 30)], "active_time": (30, 90)},
        {"id": 3, "coordinates": [(10, 60), (30, 60), (30, 80), (10, 80)], "active_time": (0, 60)}
    ]

    drones = [Drone(**d) for d in drones_data]
    deliveries = [TeslimatNoktasi(**d) for d in deliveries_data]
    nofly_zones = [NoFlyZone(**z) for z in nofly_data]
    charging_stations = [drone.position for drone in drones]

    for drone in drones:
        print(f"\n--- Drone {drone.id} işlemleri başlatılıyor ---")

        if drone.id == 2:
            print(f"[DEBUG] Drone 2 başlangıç noktası: {drone.position}, max ağırlık: {drone.max_weight}")

        while True:
            valid_deliveries = [d for d in deliveries if not d.delivered and is_within_time_window(current_minute, d.time_window)]
            sorted_deliveries = sorted(valid_deliveries, key=lambda d: -d.priority)

            if drone.id == 2:
                print(f"[DEBUG] Drone 2 geçerli teslimatlar:")
                for d in sorted_deliveries:
                    print(f"  ➤ T{d.id} | {d.weight} kg | Öncelik: {d.priority} | Zaman: {d.time_window}")

            carried = []
            total_weight = 0
            for d in sorted_deliveries:
                if total_weight + d.weight <= drone.max_weight:
                    carried.append(d)
                    total_weight += d.weight

            if not carried:
                if drone.id == 2:
                    print(f"[DEBUG] Drone 2 taşıyamıyor. Toplam yük: {total_weight}")
                break

            optimized_sequence = genetic_algorithm(
                start_pos=drone.position,
                deliveries=carried,
                nofly_zones=nofly_zones,
                current_time=current_minute
            )

            route = []
            current_pos = drone.position
            for d in optimized_sequence:
                partial = a_star(
                    start=current_pos,
                    goal=d.pos,
                    nofly_zones=nofly_zones,
                    max_x=100, max_y=100,
                    current_time_str=current_minute,
                    weight=d.weight,
                    priority=d.priority
                )
                if partial:
                    print(f"✅ Drone {drone.id} → Teslimat T{d.id}: {current_pos} → {d.pos}")
                    route += partial[1:]
                    current_pos = d.pos
                    d.delivered = True
                else:
                    print(f"❌ Drone {drone.id} A* başarısız: {current_pos} → {d.pos}")

            if not route:
                break
            drone.route += route
            drone.position = current_pos

        print(f"📦 Drone {drone.id} için toplam rota uzunluğu: {len(drone.route)} nokta")

    print("\n📄 Test Senaryosu: 5 Drone, 20 Teslimat, 3 No-Fly Zone")
    print(f"🕐 Simülasyon saati: {current_time}")
    for drone in drones:
        print(f"🚁 Drone {drone.id}: Rota Uzunluğu: {len(drone.route)} nokta")

    metrics = calculate_performance_metrics(drones)
    print("\n📊 PERFORMANS")
    print(f"✅ Toplam Tamamlanan Teslimat: {metrics['total_deliveries']}")
    print(f"📏 Toplam Rota Mesafesi: {metrics['total_distance']:.2f} m")
    print(f"🔋 Tahmini Enerji Tüketimi: {metrics['estimated_energy']:.2f} birim")

    plot_simulation(drones, deliveries, nofly_zones, charging_stations)

if __name__ == "__main__":
    main()
