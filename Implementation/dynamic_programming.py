import time
import sys

def knapsack_dp(filename):
    """Solve the 0/1 knapsack problem using Dynamic Programming with input from a file."""
    try:
        # Open and read the input file
        with open(filename, 'r') as f:
            lines = f.readlines()
        
        # Parse the knapsack capacity from the first line
        W = int(lines[0].strip())
        
        # Parse items (weight, value, original index) from subsequent lines
        items = []
        for idx, line in enumerate(lines[1:], start=0):
            w, v = map(int, line.strip().split('\t'))  # Assumes tab-separated weight and value
            items.append((w, v, idx))  # Store weight, value, and original index

        # Start timing the execution
        start_time = time.perf_counter()

        # Dynamic Programming table initialization
        n = len(items)
        dp = [[0] * (W + 1) for _ in range(n + 1)]
        
        # Fill the DP table
        for i in range(1, n + 1):
            for w in range(W + 1):
                if items[i-1][0] > w:  # If item weight exceeds current capacity
                    dp[i][w] = dp[i-1][w]
                else:
                    dp[i][w] = max(dp[i-1][w], dp[i-1][w - items[i-1][0]] + items[i-1][1])

        # Backtrack to determine included items
        included = []
        i, w = n, W
        while i > 0 and w > 0:
            if dp[i][w] != dp[i-1][w]:
                included.append(items[i-1][2])  # Add original index of included item
                w -= items[i-1][0]
            i -= 1

        # Calculate execution time
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        # Get the maximum value
        max_value = dp[n][W]

        # Print results
        print("Dynamic Programming:")
        print(f"Maximum profit: {max_value}")
        print(f"Items included: {sorted(included)}")
        print(f"Execution time: {execution_time:.6f} seconds")

        # Return results for potential further use
        return max_value, sorted(included), execution_time

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except IOError:
        print(f"Error: Could not read file '{filename}'.")
        sys.exit(1)
    except ValueError:
        print("Error: Invalid input format in the file.")
        sys.exit(1)

# Main execution block
if __name__ == "__main__":
    # Check for correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python dp_knapsack.py <input_file>")
        sys.exit(1)
    
    # Retrieve the file name from command-line arguments
    filename = sys.argv[1]
    knapsack_dp(filename)