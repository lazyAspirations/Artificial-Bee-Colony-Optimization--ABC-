import math
import random
import matplotlib.pyplot as plt

# Cities coordinates: A to J
cities = [
    (2, 2),  # A
    (2, 6),  # B
    (5, 5),  # C
    (6, 1),  # D
    (8, 3),  # E
    (10, 8), # F
    (1, 9),  # G
    (4, 1),  # H
    (9, 5),  # I
    (7, 9)   # J
]

# Compute distance matrix
dist_matrix = [[0]*10 for _ in range(10)]

for i in range(10):
    for j in range(10):
        dist_matrix[i][j] = math.sqrt(
            (cities[i][0] - cities[j][0])**2 +
            (cities[i][1] - cities[j][1])**2
        )

# Function to calculate total distance
def total_distance(tour):
    dist = 0
    for i in range(9):
        dist += dist_matrix[tour[i]][tour[i+1]]
    dist += dist_matrix[tour[9]][tour[0]]
    return dist

# Fitness function
def fitness(tour):
    return 1 / total_distance(tour)

# Generate random tour
def random_tour():
    tour = list(range(10))
    random.shuffle(tour)
    return tour

# Initialize population (5 bees)
population = []

for _ in range(5):
    tour = random_tour()
    bee = {
        'tour': tour,
        'fitness': fitness(tour),
        'counter': 0
    }
    population.append(bee)

# Initial best
initial_best = min(total_distance(bee['tour']) for bee in population)
print("Initial best distance:", initial_best)

# Track best distances
best_distances = []
best_so_far = float('inf')

# Main loop (50 iterations)
for iter in range(50):

    # Employed Bees Phase
    for bee in population:

        i, j = random.sample(range(10), 2)

        new_tour = bee['tour'][:]
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]

        new_fit = fitness(new_tour)

        if new_fit > bee['fitness']:
            bee['tour'] = new_tour
            bee['fitness'] = new_fit
            bee['counter'] = 0
        else:
            bee['counter'] += 1

    # Onlooker Bees Phase
    total_fit = sum(bee['fitness'] for bee in population)
    probs = [bee['fitness'] / total_fit for bee in population]

    for _ in range(5):

        r = random.random()
        cum = 0
        selected_idx = 0

        for idx, p in enumerate(probs):
            cum += p
            if r <= cum:
                selected_idx = idx
                break

        bee = population[selected_idx]

        i, j = random.sample(range(10), 2)

        new_tour = bee['tour'][:]
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]

        new_fit = fitness(new_tour)

        if new_fit > bee['fitness']:
            bee['tour'] = new_tour
            bee['fitness'] = new_fit
            bee['counter'] = 0
        else:
            bee['counter'] += 1

    # Scout Bees Phase
    limit = 8

    for bee in population:
        if bee['counter'] >= limit:

            print(f"Iteration {iter+1}: Scout bee replaces stagnant solution")

            bee['tour'] = random_tour()
            bee['fitness'] = fitness(bee['tour'])
            bee['counter'] = 0

    # Record best distance (staircase)
    best_dist = min(total_distance(bee['tour']) for bee in population)

    if best_dist < best_so_far:
        best_so_far = best_dist

    best_distances.append(best_so_far)

# Final best
final_best = min(best_distances)
print("Final best distance:", final_best)

# Find best tour
best_bee = min(population, key=lambda b: total_distance(b['tour']))
best_tour = best_bee['tour']

print("Best tour:", [chr(65 + i) for i in best_tour])

# Plot best tour
plt.figure()

x = [cities[i][0] for i in best_tour] + [cities[best_tour[0]][0]]
y = [cities[i][1] for i in best_tour] + [cities[best_tour[0]][1]]

plt.plot(x, y, 'o-')

for i, city in enumerate(best_tour):
    plt.text(cities[city][0], cities[city][1], chr(65 + city),
             fontsize=12, ha='right')

plt.title(f'Best TSP Tour (Distance: {total_distance(best_tour):.2f})')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

plt.savefig('best_tour.png')

print("Best tour plot saved as best_tour.png")

# Plot convergence (STAIR STEP)
plt.figure()

plt.step(range(1, 51), best_distances, where='post')

plt.xlabel('Iteration')
plt.ylabel('Best Distance')
plt.title('Convergence of ABC for TSP (Staircase)')
plt.grid(True)

plt.savefig('convergence.png')

print("Convergence plot saved as convergence.png")