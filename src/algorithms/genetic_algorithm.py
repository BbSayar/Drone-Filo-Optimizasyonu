import random

def calculate_total_distance(start_pos, deliveries):
    total = 0
    current = start_pos
    for d in deliveries:
        total += abs(current[0] - d.pos[0]) + abs(current[1] - d.pos[1])
        current = d.pos
    return total

def create_initial_population(start_pos, deliveries, size=10):
    population = []
    for _ in range(size):
        individual = deliveries[:]
        random.shuffle(individual)
        population.append(individual)
    return population

def crossover(parent1, parent2):
    size = len(parent1)
    if size < 2:
        return parent1[:]
    start, end = sorted(random.sample(range(size), 2))
    child = [None] * size
    child[start:end] = parent1[start:end]
    pointer = 0
    for d in parent2:
        if d not in child:
            while child[pointer] is not None:
                pointer += 1
            child[pointer] = d
    return child

def mutate(individual, mutation_rate=0.1):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(individual) - 1)
            individual[i], individual[j] = individual[j], individual[i]

def genetic_algorithm(start_pos, deliveries, nofly_zones, current_time, generations=30, pop_size=10):
    if not deliveries:
        return []

    population = create_initial_population(start_pos, deliveries, pop_size)

    for _ in range(generations):
        population = sorted(population, key=lambda d: calculate_total_distance(start_pos, d))
        new_pop = population[:2]  # elit bireyler

        while len(new_pop) < pop_size:
            parent1 = random.choice(population[:5])
            parent2 = random.choice(population[:5])
            child = crossover(parent1, parent2)
            mutate(child)
            new_pop.append(child)

        population = new_pop

    best = min(population, key=lambda d: calculate_total_distance(start_pos, d))
    return best
