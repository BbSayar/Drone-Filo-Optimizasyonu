from datetime import datetime
import math

def is_within_time_window(current_time, time_window):
    start_minute, end_minute = time_window
    return start_minute <= current_time <= end_minute

def calculate_distance(points):
    total = 0
    for i in range(1, len(points)):
        x1, y1 = points[i - 1]
        x2, y2 = points[i]
        total += math.hypot(x2 - x1, y2 - y1)
    return total
