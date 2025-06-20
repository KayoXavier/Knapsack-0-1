import time
from collections import namedtuple
import heapq
import sys

# Define a Node structure for the priority queue
Node = namedtuple('Node', ['level', 'weight', 'value', 'upper_bound', 'path'])

def compute_upper(sorted_items, n, W, level, current_weight, current_value):
    """Compute the upper bound by greedily adding remaining items fractionally."""
    remaining_capacity = W - current_weight
    upper = current_value
    i = level
    while i < n and remaining_capacity >= sorted_items[i][0]:
        upper += sorted_items[i][1]
        remaining_capacity -= sorted_items[i][0]
        i += 1
    if i < n and remaining_capacity > 0:
        upper += (remaining_capacity / sorted_items[i][0]) * sorted_items[i][1]
    return upper

def knapsack_bb(filename):
    """Solve the 0/1 knapsack problem using Branch and Bound with input from a file."""
    # Read input from the specified file
    with open(filename, 'r') as f:
        lines = f.readlines()
    W = int(lines[0].strip())  # Knapsack capacity
    items = []
    for idx, line in enumerate(lines[1:], start=0):
        w, v = map(int, line.strip().split('\t'))  # Weight and value
        items.append((w, v, idx))  # (weight, value, original_index)

    # Start timing the execution
    start_time = time.perf_counter()

    n = len(items)
    # Sort items by value-to-weight ratio in descending order
    sorted_items = sorted(items, key=lambda x: x[1]/x[0], reverse=True)
    original_indices = [item[2] for item in sorted_items]

    # Initialize priority queue (max-heap using negative upper bounds)
    queue = []
    initial_upper = compute_upper(sorted_items, n, W, 0, 0, 0)
    root = Node(0, 0, 0, initial_upper, [])
    heapq.heappush(queue, (-initial_upper, root))

    best_value = 0
    best_path = []

    # Branch and Bound algorithm
    while queue:
        _, node = heapq.heappop(queue)
        if node.upper_bound <= best_value:
            break  # No better solution possible

        if node.level == n:
            if node.value > best_value:
                best_value = node.value
                best_path = node.path
        else:
            # Exclude the next item
            excl_path = node.path + [0]
            excl_upper = compute_upper(sorted_items, n, W, node.level + 1, node.weight, node.value)
            if excl_upper > best_value:
                excl_node = Node(node.level + 1, node.weight, node.value, excl_upper, excl_path)
                heapq.heappush(queue, (-excl_upper, excl_node))

            # Include the next item if it fits
            if node.weight + sorted_items[node.level][0] <= W:
                incl_path = node.path + [1]
                incl_weight = node.weight + sorted_items[node.level][0]
                incl_value = node.value + sorted_items[node.level][1]
                incl_upper = compute_upper(sorted_items, n, W, node.level + 1, incl_weight, incl_value)
                if incl_upper > best_value:
                    incl_node = Node(node.level + 1, incl_weight, incl_value, incl_upper, incl_path)
                    heapq.heappush(queue, (-incl_upper, incl_node))

    # Map back to original item indices
    included = [original_indices[i] for i in range(n) if best_path[i] == 1]

    # End timing
    end_time = time.perf_counter()
    execution_time = end_time - start_time

    # Output the results
    print("Branch and Bound:")
    print(f"Maximum profit: {best_value}")
    print(f"Items included: {sorted(included)}")
    print(f"Execution time: {execution_time:.6f} seconds")

    return best_value, sorted(included), execution_time

# Main execution block
if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python branch_and_bound.py <input_file>")
        sys.exit(1)
    
    # Get the filename from the command line
    filename = sys.argv[1]
    knapsack_bb(filename)
