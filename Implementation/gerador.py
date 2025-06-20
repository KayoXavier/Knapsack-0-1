import os
import csv
import time
import random
from dynamic_programming import knapsack_dp  # Importe suas outras implementações
from branch_and_bound import knapsack_bb     # Importe suas outras implementações
from backtracking import knapsack_backtracking  # Novo import

# Diretórios
INSTANCE_DIR = "instances/"
RESULT_DIR = "results/"

# Function to generate instances (from your query)
def generate_instance(filename, W, n):
    with open(filename, 'w') as f:
        f.write(f"{W}\n")  # Knapsack capacity
        for _ in range(n):
            weight = random.randint(1, 30)  # Weight between 1 and 30
            value = random.randint(1, 100)  # Value between 1 and 100
            f.write(f"{weight}\t{value}\n")

# Function to generate instances (from your query)
def generate_instance(filename, W, n):
    with open(filename, 'w') as f:
        f.write(f"{W}\n")  # Knapsack capacity
        for _ in range(n):
            weight = random.randint(1, 30)  # Weight between 1 and 30
            value = random.randint(1, 100)  # Value between 1 and 100
            f.write(f"{weight}\t{value}\n")

# Function to generate all instances
def generate_all_instances():
    os.makedirs(INSTANCE_DIR, exist_ok=True)
    
    # Experiment 1: Fixed W = 100, varying n
    W = 100
    n_values = [100, 10, 20, 30, 40, 50, 60, 65, 70, 200, 400, 800, 1600, 3200, 6400, 12800]
    for n in n_values:
        for i in range(20):  # 20 instances per n
            filename = os.path.join(INSTANCE_DIR, f"instance_n{n}_{i}.txt")
            generate_instance(filename, W, n)

    # Experiment 2: Fixed n = 800, varying W
    n = 800
    W_values = [100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600]
    for W in W_values:
        for i in range(20):  # 20 instances per W
            filename = os.path.join(INSTANCE_DIR, f"instance_W{W}_{i}.txt")
            generate_instance(filename, W, n)


def run_algorithm(algorithm, filename):
    start_time = time.perf_counter()
    try:
        if algorithm == "dp":
            max_profit, selected_items, _ = knapsack_dp(filename)
        elif algorithm == "bb":
            max_profit, selected_items, _ = knapsack_bb(filename)
        else:
            raise ValueError("Algoritmo desconhecido")
        
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        return max_profit, selected_items, execution_time
    except Exception as e:
        print(f"Erro processando {filename} com {algorithm}: {e}")
        return None, None, None

def main():
    os.makedirs(RESULT_DIR, exist_ok=True)
    print("Gerando instâncias...")
    generate_all_instances()

    instance_files = [f for f in os.listdir(INSTANCE_DIR) if f.endswith(".txt")]
    print(f"{len(instance_files)} instâncias encontradas.")

    with open(os.path.join(RESULT_DIR, "results.csv"), "w", newline="") as csvfile:
        fieldnames = ["instancia", "algoritmo", "lucro_maximo", "itens_selecionados", "tempo_execucao"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for instance in instance_files:
            instance_path = os.path.join(INSTANCE_DIR, instance)
            print(f"Processando {instance}...")

            # Executa todos os algoritmos
            for algo in ["dp", "bb"]:  # sem backtracking
                profit, items, exec_time = run_algorithm(algo, instance_path)
                if profit is not None:
                    writer.writerow({
                        "instancia": instance,
                        "algoritmo": algo,
                        "lucro_maximo": profit,
                        "itens_selecionados": str(items),
                        "tempo_execucao": f"{exec_time:.5f}"
                    })

    print(f"Resultados salvos em {os.path.join(RESULT_DIR, 'resultados_completos.csv')}")

if __name__ == "__main__":
    main()
