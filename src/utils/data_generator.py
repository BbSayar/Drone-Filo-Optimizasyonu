from models.drone import Drone
from models.teslimat_noktasi import TeslimatNoktasi
from models.nofly_zone import NoFlyZone
import csv

def parse_time_to_minutes(time_str):
    hour, minute = map(int, time_str.strip().split(":"))
    return hour * 60 + minute

def load_data_from_txt(filepath):
    drones = []
    deliveries = []
    nofly_zones = []
    section = None

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                if "DRONES" in line:
                    section = "DRONES"
                elif "DELIVERIES" in line:
                    section = "DELIVERIES"
                elif "NOFLY" in line:
                    section = "NOFLY"
                continue

            if section == "NOFLY":
                reader = csv.reader([line])
                parts = next(reader)
            else:
                parts = line.split(",")

            if section == "DRONES":
                id = int(parts[0])
                max_weight = float(parts[1])
                battery = int(parts[2])
                speed = float(parts[3])
                x = int(parts[4])
                y = int(parts[5])
                drones.append(Drone(id, max_weight, battery, speed, (x, y)))

            elif section == "DELIVERIES":
                id = int(parts[0])
                x = int(parts[1])
                y = int(parts[2])
                weight = float(parts[3])
                priority = int(parts[4])
                start_time = parse_time_to_minutes(parts[5])
                end_time = parse_time_to_minutes(parts[6])
                deliveries.append(TeslimatNoktasi(id, (x, y), weight, priority, (start_time, end_time)))

            elif section == "NOFLY":
                id = int(parts[0])
                coords_str = parts[1].strip().strip('"')
                coordinate_pairs = coords_str.split(";")

                coordinates = []
                for pair in coordinate_pairs:
                    if not pair:
                        continue
                    if "," not in pair:
                        continue
                    x_str, y_str = pair.strip().split(",")
                    coordinates.append((int(x_str), int(y_str)))

                start_time = parse_time_to_minutes(parts[2])
                end_time = parse_time_to_minutes(parts[3])
                nofly_zones.append(NoFlyZone(id, coordinates, (start_time, end_time)))

    return drones, deliveries, nofly_zones
