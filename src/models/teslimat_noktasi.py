class TeslimatNoktasi:
    def __init__(self, id, pos, weight, priority, time_window):
        self.id = id
        self.pos = pos
        self.weight = weight
        self.priority = priority
        self.time_window = time_window
        self.delivered = False  # Teslimat durumu
