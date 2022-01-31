# ACS 1120: Quiz Study Guides

<!-- omit in toc -->
## Table of Contents

1. [General Information](#general-information)
1. [Tips to Prepare](#tips-to-prepare)
1. [Quiz 1 Study Guide](#quiz-1-study-guide)
   1. [Histograms](#histograms)
   1. [Probability & Sampling](#probability-%26-sampling)
   1. [Markov Chains](#markov-chains)
1. [Quiz 2 Study Guide](#quiz-2-study-guide)
   1. [Arrays](#arrays)
   1. [Linked Lists](#linked-lists)
   1. [Linked List Algorithm Analysis](#linked-list-algorithm-analysis)
1. [Quiz 3 Study Guide](#quiz-3-study-guide)
   1. [Hash Tables](#hash-tables)
   1. [Hash Table Algorithm Analysis](#hash-table-algorithm-analysis)
   1. [Histogram Algorithm Analysis](#histogram-algorithm-analysis)
1. [Quiz 4 Study Guide](#quiz-4-study-guide)
   1. [First Order Markov Chains](#first-order-markov-chains)
   1. [Higher Order Markov Chains](#higher-order-markov-chains)
   1. [Regular Expressions](#regular-expressions)

## General Information

* **Time**: First 20 minutes of class (arrive early or on time to use the full time available).
* **Format**: Written on paper (no computers allowed), short answers, drawing diagrams, reading and writing Python code, analyzing algorithm complexity.
* **Grading**: Quizzes will be graded with an answer key by the course instructor (Dani). Some questions may have multiple correct answers. Partial credit given as applicable.
* **Accommodations**: If you have a disability that requires accommodations for quizzes, you must follow the Accommodations Policy, then clarify with the course instructor exactly what accommodations will be made at least 24 hours before the quiz.


## Tips to Prepare

* Review lesson plans (found in the [course repo](README.md)), tutorial and project code.
* Complete the homework assigned after the relevant lessons. Work with other students, discuss your design and code, ask for feedback from others, and improve your code.
* If you were absent for any class sessions, it’s essential to catch up on what you missed. Review the lesson activities, watch the videos of in class activities and recap sessions, do the activities on your own, and discuss with classmates who attended and took notes.
* Use the course Slack channel (#acs-1120) to coordinate study groups with classmates, ask questions when you’re stuck, and share relevant resources you find.


## Quiz 1 Study Guide

### Histograms

[lesson activities and resources](Lessons/Histograms.md)

* Identify how many distinct word types and total word tokens are in a text input.
* Choose an appropriate data structure to store a histogram of word frequencies and explain what makes the data structure you chose effective for a histogram.
* Show the data structure you chose to store a histogram as it appears in Python.
* Write a short snippet of code to retrieve a target word’s frequency in a histogram data structure and update a target word with a new observation from a text input.

### Probability & Sampling

[lesson slides, activities and resources](Lessons/Probability.md)

* Given the implementation of a sampling function, execute it as if you were the Python interpreter to determine its output.

### Markov Chains

[lesson activities and resources](Lessons/MarkovChains.md)

* Draw a conceptual diagram of the Markov chain generated from a text input.
* Show the data structures created to store state transitions in a Markov chain.
* Generate a new sentence by performing a random walk on a Markov chain.
* Highly recommended: Review the histogram, Markov chain, and sampling worksheet completed in class. If you missed class, you should watch the worksheet review video.


## Quiz 2 Study Guide

### Arrays

[lesson slides, activities and resources](Lessons/ArraysLinkedLists.md)

* Draw a diagram of how a dynamic array data structure is organized in memory.
* Show how an array calculates the memory address of an item given its index.
* Describe the steps required to append a new item to a dynamic array that needs to be resized to allocate more space because its underlying static array is full.

### Linked Lists

[lesson slides, activities and resources](Lessons/ArraysLinkedLists.md)

* Identify the ingredients needed to build a linked list data structure with nodes.
* Draw a diagram of how a linked list data structure is organized in memory with node references. Label its head, tail, and each node’s data and next properties.
* List the steps required to add a new item to or find a target item in a linked list.
* Implement a method that is similar to the linked list challenges and starter code.
* Recommended: Review the linked list worksheet completed in class.

### Linked List Algorithm Analysis

[lesson activities and resources](Lessons/AlgorithmAnalysis.md)

* Analyze the best case and worst case time complexity of a linked list method.
* Recommended: Review the linked list time complexity worksheet completed in class. If you missed class, try it yourself, then watch the worksheet review video.


## Quiz 3 Study Guide

### Hash Tables

[lesson slides, activities and resources](Lessons/HashTables.md)

* Identify the ingredients needed to build a hash table data structure with chaining.
* Draw a diagram of how a hash table data structure with chaining is organized in memory. Label the buckets and each bucket’s array index and key-value entries.
* Describe what a hash collision is and how it is resolved with chaining or probing.
* List the steps required to add a new key-value entry, update an existing key with a new value, or find a target key’s associated value in a hash table with chaining.
* Implement a method that is similar to the hash table challenges and starter code.
* **Recommended**: Review the hash table worksheet completed in class.

### Hash Table Algorithm Analysis

[lesson activities and resources](Lessons/AlgorithmAnalysis.md)

* Analyze the best case and average case time complexity of a hash table method.
* Analyze a hash table method to determine if it is implemented efficiently, and if not, how it could be improved.
* Recommended: Review the hash table time complexity worksheet completed in class and watch the worksheet review video that explains the load factor in detail.

### Histogram Algorithm Analysis

[lesson activities and resources](Lessons/AlgorithmAnalysis.md)

* Analyze the time complexity of a function that builds a histogram from a text input and determine if it is implemented efficiently, and if not, how it could be improved.

## Quiz 4 Study Guide

### First Order Markov Chains

[lesson activities and resources](Lessons/MarkovChains.md)

* Draw a conceptual diagram of a 1st order Markov chain generated from a text.
* Show the data structures that store state transitions in a 1st order Markov chain.
* Write a short snippet of code to update a Markov chain’s data structure with a new observation of a pair of words from a text input.
* Write a new sentence generated by a random walk on a 1st order Markov chain.
* Highly recommended: Review the histograms and Markov chain worksheet (page 1) completed in class.

### Higher Order Markov Chains

[lesson activities and resources](Lessons/MarkovChains.md)

* Draw a conceptual diagram of a 2nd order Markov chain generated from a text.
* Show the data structures that store state transitions in a 2nd order Markov chain.
* Write a new sentence that could be generated by performing a random walk on a 1st order Markov chain but could not be generated by a 2nd order Markov chain.
* Highly recommended: Review the higher order Markov chain worksheet (page 2) completed in class.

### Regular Expressions

[lesson slides, activities and resources](Lessons/RegularExpressions.md)

   * **Note**: _Quiz 4 will NOT cover regular expressions_
