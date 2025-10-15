# About Project
**Group No: 6**

**Group Members: Rahul Hipparkar, Lily Holmes, Andrea Caceres, Isra Marcu**

**Project Name: Campus Event Scheduling System**

**Github Repo link**:  https://github.com/RahulHipparkar/DSA-GP1---Campus-Event-Scheduling-System

**Objective**: We’ve been hired to design a lightweight scheduling system for managing campus events (talks, hackathons, concerts, exams, etc.). The system must allow adding, searching, sorting, and conflict-checking events efficiently as the event list grows from a handful to thousands.

Our group will design and implement custom data structures and algorithms to power the system, compare their performance, and present results.

# Project Structure
The project consists 5 important folders and files:
- **src**: src consists of entire source code including modular python files. It consists of three folders:
  - **models**: Consist of code for event class and data models dynamic array and linked list.
  - **searching**: Consist of functions for searching alogithms such as linear search and binary search and function for conflict detection.
  - **sorting**: Consist of functions for sorting algorithms for both data strutures.
- **tests** : Consist of pytest test scripts.
- **README.md**: To document team roles, project structure and complexity analysis.
- **requirements.txt**:Manage project dependencies.
- **GP1_Hipparkar_Holmes_Caceres_Marcu.ipynb**: Consists of all experiments , graph and scalability solution.

# Time Complexity Analysis:

| Algorithm                      | Time complexity | Space Complexity |
| :-------                       | :------:        | -------: |
| Linear Search                  | O(N)        | O(1)   |
| Binary Search                  | O(log N)        | O(1)  |
| Conflict Detection             |  O(N)         | O(N) : using dictionary data structure to find conflicts  |
| Insertion sort for dynamic array |  O(N^2)                 |   O(1)       |
| Merge sort for dynamic array     | O(NlogN)       | O(N) : using an extra array here to merge sorted arrays|
| Quick sort for dynamic array     | O(NlogN)       | O(1)|
| Insertion sort for linked lists  | O(N^2)         | O(1) |
| Merge sort for linked lists      | O(NlogN) | O(1) : using constant space for storing reference pointers|
| Quick sort for linked lists     | Best case : O(NlogN), Worst case: O(N^2) | O(N)|

Here N is size of dynamic array or number of nodes in the linked list.

# Team roles:




