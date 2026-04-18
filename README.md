# ⚔️ Battlefield: Python Game

A terminal-based RPG battle simulator written in Python. 

## 🚀 Features
* **Dynamic Turn-Based Combat:** A `while` loop engine that runs until a win/loss condition is met.
* **Specialized Classes:** Heroes (`Knight`, `Wizard`, `Healer`) inherit from a base `Character` class and override actions using Polymorphism.
* **Stateful Enemies:** The `Villain` class tracks internal state (`turn_counter`) to trigger an Area-of-Effect "Slam" attack every 3 rounds.
* **Smart Targeting:** Healers automatically target the ally with the lowest health, while enemies target random living heroes.

## 🛠️ How to Run
```bash
python main.py