import numpy as np

# No diagonal movements:
# a cell has at most 4 possibilities for a next step
def search_neighbors(array, pos):
    neighbors = set()
    if pos[0] > 0:
        neighbors.add((pos[0]-1, pos[1]))
    if pos[0] < len(array)-1:
        neighbors.add((pos[0]+1, pos[1]))
    if pos[1] > 0:
        neighbors.add((pos[0], pos[1]-1))
    if pos[1] < len(array[0])-1:
        neighbors.add((pos[0], pos[1]+1))
    return neighbors

# Preallocate a NumPy array
array = np.empty((52, 52), dtype=int)

# Read file and populate the array
with open("aoc2024day10.txt", 'r') as file:
    for i, line in enumerate(file):
        array[i, :] = list(line.strip())

print(array)

# Star 1
# A trail starts at trailhead 0, and progresses in increments of 1, ending at 9
# A trailhead's score is the number of distinct 9s that can be reached from it
# What is the sum of all trailheads' scores?

def depth_first(visited, array, current_node):
    
    # Depth-first search looks for the next step in the vertex's neighbors
    # When the search finds a 9, the 9's coordinates are added to a
    # 'visited' list to prevent counting a single path multiple times
    if array[current_node] == 9 and current_node not in visited:
        print(f"Found 9 at {current_node}!")
        visited.add(current_node)
        return

    neighbors = search_neighbors(array, current_node)
    for neighbor in neighbors:
        if array[neighbor] == array[current_node]+1:
            print(f"Found next step {array[neighbor]} at {neighbor}")
            # Search continues recursively at next step
            depth_first(visited, array, neighbor)
        else:
            continue

    return

zerorow, zerocol = np.where(array == 0)
sum = 0
for i in range(len(zerorow)):
    # List of visited 9s is cleared after every path from zero is traversed
    visited = set()
    print(f"Evaluating path at {(zerorow[i], zerocol[i])}: 0")
    depth_first(visited, array, (zerorow[i], zerocol[i]))
    sum += len(visited)

# Sum of scores for each 0
print(sum)

# Star 2
# Same as Star 1, except count each distinct path to a 9 as distinct 9

zerorow, zerocol = np.where(array == 0)
sum = 0

def depth_first(array, current_node):
    # Using a global sum variable instead of a 'visited' list this time
    global sum
    
    if array[current_node] == 9:
        print(f"Found 9 at {current_node}!")
        sum += 1
        return

    neighbors = search_neighbors(array, current_node)
    for neighbor in neighbors:
        if array[neighbor] == array[current_node]+1:
            print(f"Found next step {array[neighbor]} at {neighbor}")
            depth_first(array, neighbor)
            
    return

for i in range(len(zerorow)):
    print(f"Evaluating path at {(zerorow[i], zerocol[i])}: 0")
    depth_first(array, (zerorow[i], zerocol[i]))
print(sum)