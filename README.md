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

To design and test a lightweight campus scheduling system in Python using knowledge of sorting / searching algorithms and data structures our team collaborated consistently. Each of us worked individually and together, synchronously, to fulfill the requirements of the scheduling system. Rather than assign each other specific sections, we worked fluidly and adaptively to create our own sections, compare, and test each other's contributions. This allowed each of us to don a necessary role within the project process that allowed the project to generate consistent productivity and take feedback from all other teammates in a constructive manner. The consistent collaboration and communication throughout the process allowed us as a team to deliver a polished and effective product. 
	
  While we each worked on separate algorithms, many sections overlapped, allowing us to compare sections and critique each other’s algorithms. Rahul provided a solid foundation by creating the event, DynamicArray, and LinkedList class, each with their own accurate attributes and methods. Isra and Andrea each provided expertise and code to create algorithms for the merge sort, insertion sort, and binary search for both the Dynamic Array and LinkedList. Lily and Rahul also coded insertion and quick sort and algorithms to be applied to both structure types. Each algorithm was then compared objectively to assess which should be included in the final project based on the efficiency and conciseness of the code itself. 
  
For the experimentation and analysis of runtimes for all algorithms, we all worked together to fit the algorithms into the benchmarker. Lily coded an algorithm to create instances of the event class as well as instances of the LinkedList and Dynamic array based on the random events created by the event creator algorithm. Andrea and Isra worked to fit the runtime algorithm to work with the search and sorting algorithms. Andrea also was successful in creating an algorithm for, and plotting, runtimes for the searching algorithms. 
  
The detection of parallel conflicts was also important. Rahul wrote the code for the detection and Lily sketched parallel detection from the algorithm as a flowchart.  
For the completion of the test through the utilization of pytest, Rahul wrote code to assess the potential presence of maladies in the algorithms. Lily attempted a pytest for the binary search. Andrea and Isra also worked on the suggestions for the algorithm optimizations.
  
An analysis of the project’s algorithms theoretical complexities for search, sort, and class methods was done by Lily. Overall commentary regarding effectiveness of the algorithm and the complexity in comparison to other potential algorithms was completed by Andrea, Lily, and Isra.  
For the final steps, Rahul pushed the code and files into the git and made sure we had completed various steps of the project.  He created and managed the github repo. 

# Set up:
The requirement of the scheduling system to be evaluated for the runtimes of its sorting and searching algorithms and tested with pytest necessitated a large amount of prior set up. Firstly, building blocks for the schedule itself were created by the chatting up of the event class. Each event also had to be stored in two different data structures, a Dynamic Array and a Linked List. Object oriented programming facilitated the creation of the event, dynamic array, and linked list class, along with their respective attributes and methods. 

The creation of algorithms to test vital processes for scheduling, such as sorting by time and data and searching by id, was also a large part of the set up. Six algorithms were created for sorting; including for each the dynamic array and linked list, the insertion sort, merge sort, and quick sort. Four algorithms were created for searching by identification number; linear and binary search for the dynamic array and linear and binary search for the linked list. 

To evaluate the aforementioned algorithms for runtime, two algorithms themselves had to be created to efficiently generate  a hypothetical, random, and realistic list of events, stored as instances in the dynamic array and linked list. A benchmarking algorithm which took parameters for schedule sizes and algorithm to be tested was created to calculate runtimes. This allowed each structures’ sorting and searching algorithms to be compared with each other. 

Finally, to evaluate the success of the algorithms, another algorithm was created to test if events ran into each other. We assumed that each event lasted an hour for the parallel detection.  
The successful set of these algorithms and databases was necessary for the overall scheduling system to work robustly for all the operations that needed to occur for the data. 

# Results

Our results for the various data structures and ways to sort and search will allow the heavier weight schedule system to be built robustly and efficiently. 
A large difference was found in the searching of algorithms. When given the task to search for an event by the event id, the binary search on the sorted dynamic array was found to be the most time efficient. From our runtime benchmarker, we found that when searching a schedule with 10,000 events, the binary search drastically outperformed the linear search as the linear search took over 0.00225 seconds. 

Similarly, for sorting linked lists, a necessary process in the implementation of the binary search for unsorted lists, we found that merge sort out-preformed both insertion and quicksort. At its worst case, the worst case time complexity of quicksort is O(n^2).  

This project allowed us to learn and practice technical skills such as the creation and management data structures and classic necessary operations. It was interesting seeing how operations are used in real life situations such as a campus scheduler. This cemented our knowledge of object oriented programming in Python. The group format for the project allowed us to meet and connect with classmates as well as strengthen our skills in collaboration. 





