import heapq
from math import floor

def heuristic(a, b):
    """Manhattan mesafesi hesaplama."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def is_in_nofly_zone(pos, nofly_zones, current_time):
    x, y = pos
    for zone in nofly_zones:
        if zone.active_time[0] <= current_time <= zone.active_time[1]:
            xs = [coord[0] for coord in zone.coordinates]
            ys = [coord[1] for coord in zone.coordinates]
            if min(xs) <= x <= max(xs) and min(ys) <= y <= max(ys):
                return True
    return False

def a_star(start, goal, nofly_zones, max_x, max_y, current_time_str, weight, priority):
    # 🔧 Float koordinatları integer grid’e çeviriyoruz
    start = (floor(start[0]), floor(start[1]))
    goal = (floor(goal[0]), floor(goal[1]))

    # 🕒 Zamanı tam sayı olarak ele al
    current_time = int(current_time_str) if isinstance(current_time_str, int) else 0

    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            # ✅ Hedefe ulaşıldı, rota oluştur
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        x, y = current
        # 4 yönlü komşular (up/down/left/right)
        neighbors = [(x + dx, y + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]

        for neighbor in neighbors:
            nx, ny = neighbor
            if not (0 <= nx <= max_x and 0 <= ny <= max_y):
                continue
            if is_in_nofly_zone(neighbor, nofly_zones, current_time):
                continue

            tentative_g = g_score[current] + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f, neighbor))

    return None  # ❌ Yol bulunamadıysa
