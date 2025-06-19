def calculate_performance_metrics(drones):
    total_deliveries = sum(1 for drone in drones if drone.route)
    total_distance = 0
    for drone in drones:
        if drone.route:
            points = [drone.position] + drone.route
            dist = sum(((points[i][0] - points[i-1][0])**2 + (points[i][1] - points[i-1][1])**2)**0.5 for i in range(1, len(points)))
            total_distance += dist

    estimated_energy = total_distance * 0.5  # enerji birim katsayısı

    return {
        "total_deliveries": total_deliveries,
        "total_distance": total_distance,
        "estimated_energy": estimated_energy
    }
