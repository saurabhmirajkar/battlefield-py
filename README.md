# ⚔️ Battlefield: Python Game

A terminal-based RPG battle simulator written in Python.

## 🚀 Features

* **Dynamic Turn-Based Combat:** A `while` loop engine that runs until a win/loss condition is met.
* **Specialized Classes:** Heroes (`Knight`, `Wizard`, `Healer`) inherit from a base `Character` class and override actions using Polymorphism.
* **Stateful Enemies:** The `Villain` class tracks internal state (`turn_counter`) to trigger an Area-of-Effect "Slam" attack every 3 rounds.
* **Smart Targeting:** Healers automatically target the ally with the lowest health, while enemies target random living heroes.

## 🛠️ How to Run

1. Clone this repository to your local machine.
2. Open your terminal and navigate to the project directory.
3. Run the game using Python 3:

   ```bash
   python main.py
