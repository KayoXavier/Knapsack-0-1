
# Knapsack 0-1

## 🧩 Introdução

Este projeto implementa e compara três algoritmos exatos para resolver o clássico **Problema da Mochila 0-1**: **Programação Dinâmica**, **Backtracking** e **Branch-and-Bound**.
O Problema da Mochila 0-1 busca escolher um conjunto de itens para maximizar seu valor total dentro de uma mochila com capacidade de peso limitada. 
A regra "0-1" dita que cada item deve ser inteiramente pego ou completamente descartado, não sendo possível levar frações. O trabalho foi a implementação prática do problema usando três abordagens diferentes:

- Backtracking: Testa todas as possibilidades, garantindo a resposta certa, mas a que custo de tempo?

- Programação Dinâmica: Resolve subproblemas e guarda os resultados para não ter retrabalho. Rápida, mas "faminta" por memória.

- Branch and Bound : Explora os caminhos mais promissores e "poda" os que não levarão a lugar nenhum. Um equilíbrio poderoso.



O intuito era testar cada implementação com tamanhos e tipos de instâncias diferentes, variando desde o número de itens, até o peso máximo da mochila.

O trabalho foi desenvolvido como parte da disciplina **BCC241 - Projeto e Análise de Algoritmos** da **Universidade Federal de Ouro Preto (UFOP)**.

---

## 📚 Sumário

* [Introdução](#introducao)
* [Instalação](#instalacao)
* [Uso](#uso)
* [Funcionalidades](#funcionalidades)
* [Estrutura do Projeto](#estrutura-do-projeto)
* [Algoritmos Implementados](#algoritmos-implementados)
* [Experimentos](#experimentos)
* [Exemplos](#exemplos)
* [Contribuidores](#contribuidores)

---

## ⚙️ Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/KayoXavier/Knapsack-0-1.git
   cd Knapsack-0-1

   ```

2. Certifique-se de ter Python 3 instalado.


## ▶️ Uso

### Gerar instâncias e rodar os algoritmos:

```bash
python gerador.py
```

### Executar um algoritmo individualmente:

```bash
python dynamic_programming.py <caminho_para_instancia.txt>
python branch_and_bound.py <caminho_para_instancia.txt>
python backtracking.py <caminho_para_instancia.txt>
```

---

## 🌟 Funcionalidades

* Geração automatizada de instâncias com diferentes valores de `n` e `W`.
* Execução e comparação dos algoritmos.
* Cálculo de tempo de execução e lucro máximo.
* Resultados exportados em CSV (`results/results.csv`).

---

## 📁 Estrutura do Projeto

```
Knapsack-0-1/
│
├── Trabalho_Prático_PAA.pdf       # Relatório técnico detalhado
├── implementations/
│   ├── backtracking.py            # Algoritmo de backtracking
│   ├── branch_and_bound.py        # Algoritmo branch-and-bound
│   ├── dynamic_programming.py     # Algoritmo de programação dinâmica
│   └── gerador.py                 # Gerador de instâncias e executor de testes
│
├── instances/                     # Instâncias geradas para os testes
├── results/                       # CSVs com os resultados dos testes
└── README.md
```

---

## 📐 Algoritmos Implementados

* **Programação Dinâmica (`dynamic_programming.py`)**
  Tempo: `O(nW)`, espaço: `O(nW)`. Boa performance para `W` pequeno.

* **Backtracking (`backtracking.py`)**
  Tempo: `O(2^n)`, espaço: `O(n)`. Ineficiente para instâncias grandes.

* **Branch-and-Bound (`branch_and_bound.py`)**
  Tempo: `O(2^n)` no pior caso, mas com excelentes podas na prática.

---

## 🧪 Experimentos

Dois experimentos foram realizados com 20 instâncias aleatórias cada:

* **Experimento 1**: Capacidade `W = 100`, variando número de itens `n` de 10 a 25.600.
* **Experimento 2**: Número de itens `n = 800`, variando a capacidade `W` de 100 a 25.600.

Métricas avaliadas:

* Tempo médio de execução.
* Lucro máximo.
* Itens selecionados.

---

## 💡 Exemplos

Entrada (formato `.txt`):

```
100
12	80
5	50
30	20
...
```

Saída esperada:

```
Lucro máximo: 190
Itens selecionados: [(12, 80), (5, 50), (30, 20)]
Tempo de execução: 0.0024s
```

---

## 👨‍💻 Contribuidores

* **Kayo Xavier Nascimento Cavalcante Leite** – 21.2.4095
* **Thaís Ferreira de Oliveira Almeida** – 21.2.4012
