from itertools import permutations

def travelling_salesman(distance):
    """
    Solves Travelling Salesman Problem (TSP) using Brute Force / Permutation search.
    Finds the Hamiltonian cycle with the minimum total travel cost.
    """
    n = len(distance)
    start = 0
    cities = list(range(1, n))

    minimum_cost = float('inf')
    best_route = None

    for perm in permutations(cities):
        current_city = start
        current_cost = 0
        route = [start]

        for city in perm:
            current_cost += distance[current_city][city]
            current_city = city
            route.append(city)

        # Return to starting city
        current_cost += distance[current_city][start]
        route.append(start)

        if current_cost < minimum_cost:
            minimum_cost = current_cost
            best_route = route

    return best_route, minimum_cost


if __name__ == "__main__":
    # Distance matrix between 4 cities (A=0, B=1, C=2, D=3)
    distance = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    city_names = ['A', 'B', 'C', 'D']
    print("Distance Matrix between Cities:")
    print("     " + "  ".join(city_names))
    for i, row in enumerate(distance):
        print(f"  {city_names[i]}: {row}")
    print()

    route, cost = travelling_salesman(distance)

    print("Optimal TSP Tour Route:")
    print("  " + " -> ".join([chr(65 + city) for city in route]))
    print("Minimum Distance / Tour Cost:", cost)
