import time

def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        W = int(lines[0].strip())
        items = []
        for line in lines[1:]:
            weight, value = map(int, line.strip().split('\t'))
            items.append((weight, value))
        return W, items

class BacktrackingSolver:
    def __init__(self, items, capacity):
        self.items = items
        self.capacity = capacity
        self.best_value = 0
        self.best_items = []
    
    def solve(self):
        self._backtrack(0, 0, 0, [])
        return self.best_value, self.best_items
    
    def _backtrack(self, index, current_weight, current_value, selected):
        if current_weight > self.capacity:
            return
        if current_value > self.best_value:
            self.best_value = current_value
            self.best_items = selected.copy()
        if index >= len(self.items):
            return
        
        # Inclui o item atual
        self._backtrack(index + 1, current_weight + self.items[index][0], current_value + self.items[index][1], selected + [self.items[index]])
        
        # Não inclui o item atual
        self._backtrack(index + 1, current_weight, current_value, selected)

def knapsack_backtracking(filename):
    W, items = read_input(filename)
    solver = BacktrackingSolver(items, W)
    start_time = time.time()
    max_value, selected = solver.solve()
    execution_time = time.time() - start_time

    print("BackTracking:")
    print(f"Maximum profit: {max_value}")
    print(f"Execution time: {execution_time:.6f} seconds")

    return max_value, selected, execution_time

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Uso: python backtracking.py <arquivo_entrada>")
        sys.exit(1)
        
    max_value, selected, elapsed = knapsack_backtracking(sys.argv[1])
    print(f"Lucro máximo: {max_value}")
    print(f"Itens selecionados: {selected}")
    print(f"Tempo de execução: {elapsed:.5f}s")
