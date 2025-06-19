class NoFlyZone:
    def __init__(self, id, coordinates, active_time):
        self.id = id
        self.coordinates = coordinates  # [(x1, y1), (x2, y2), ...]
        self.active_time = active_time  # (start_minute, end_minute)
