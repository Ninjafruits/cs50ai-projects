# Degrees of Separation

This project implements a breadth-first search (BFS) algorithm to determine the shortest path between two actors based on movies they have starred in together — a variation on the "Six Degrees of Kevin Bacon" problem.

---

## 📁 Project Overview

- **Course**: CS50's Introduction to Artificial Intelligence with Python
- **Project**: Degrees
- **Goal**: Given two actors, find the shortest chain of co-stars that connects them.
- **Approach**: Graph search using **Breadth-First Search (BFS)**

---

## 🧠 How It Works

- Each **person** is a node.
- An **edge** exists between two people if they acted in a movie together.
- BFS is used to find the shortest path from source to target.

---

## 🗃️ File Structure

degrees/
├── degrees.py # Main program with BFS logic
├── util.py # Queue and Node utility classes
├── small/ # Small test dataset
├── large/ # Full IMDB-like dataset
└── README.md # This file

##Notes
- default it reads large as the dataset but a quick change in degrees.py/ main function: change large to small

##Output example
Name: Emma Watson
Name: Tom Hanks

2 degrees of separation.
1: Emma Watson and Daniel Radcliffe starred in Harry Potter and the Prisoner of Azkaban
2: Daniel Radcliffe and Tom Hanks starred in [Some Movie]
