# Artificial Bee Colony (ABC) for Traveling Salesman Problem (TSP)

![Algorithm-ABC](https://img.shields.io/badge/Algorithm-ABC-orange)
![Topic-Optimization](https://img.shields.io/badge/Topic-Optimization-blue)
![Language-Python](https://img.shields.io/badge/Language-Python-yellow)

## 📌 Project Overview
This project implements the **Artificial Bee Colony (ABC)** metaheuristic to solve the **Traveling Salesman Problem (TSP)**. The goal is to find the shortest possible route that visits 10 specific cities (A to J) exactly once and returns to the origin city.

This was completed as part of the **TP5: Metaheuristics** coursework.

## 🐝 How the Algorithm Works
The simulation mimics the foraging behavior of honeybees through three distinct phases:
1. **Employed Bees:** Perform local searches by swapping cities in known routes to find shorter paths.
2. **Onlooker Bees:** Choose the best-performing routes based on a probability (Fitness) and attempt further improvements.
3. **Scout Bees:** Identify "stagnant" solutions that haven't improved after 8 attempts and replace them with a completely new random route to maintain diversity.

## 🗺️ Problem Definition
- **Number of Cities:** 10 (A, B, C, D, E, F, G, H, I, J)
- **Distance Metric:** Euclidean Distance.
- **Fitness Function:** $Fitness = \frac{1}{\text{Total Distance}}$

## 🛠️ Tech Stack
- **Language:** Python 3
- **Libraries:** - `math` & `random` (Logic)
  - `matplotlib` (Visualization of convergence and routes)

## 🚀 How to Run
1. **Ensure you have Python and Matplotlib installed:**
   pip install matplotlib

2. Clone the repo:
git clone [https://github.com/lazyAspirations/Artificial-Bee-Colony-Optimization--ABC-.git](https://github.com/lazyAspirations/Artificial-Bee-Colony-Optimization--ABC-.git)

3. Run the script:
python abc_tsp.py

📊 Results
The Final Best Distance found.
The Optimized Sequence of cities (e.g., ['A', 'H', 'D', ...]).
A Convergence Plot showing how the distance decreased over 50 iterations.
A Map Plot visualizing the final chosen path.