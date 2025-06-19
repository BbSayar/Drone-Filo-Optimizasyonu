class Drone:
    def __init__(self, id, max_weight, battery, speed, start_pos):
        self.id = id
        self.max_weight = float(max_weight)
        self.battery = float(battery)
        self.speed = float(speed)
        self.position = start_pos
        self.route = []
        self.current_payload = 0
        self.status = "idle"
