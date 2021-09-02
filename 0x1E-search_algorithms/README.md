# 0x1E. C - Search Algorithms

In computer science, a search algorithm is an algorithm (typically involving a multitude of other, more specific algorithms [1]) which solves a search problem. Search algorithms work to retrieve information stored within some data structure, or calculated in the search space of a problem domain, either with discrete or continuous values.
While the search problems described above and web search are both problems in information retrieval, they are generally studied as separate subfields and are solved and evaluated differently. Web search problems are generally focused on filtering and finding documents that are most relevant to human queries. Classic search algorithms are typically evaluated on how fast they can find a solution, and whether that solution is guaranteed to be optimal. Though information retrieval algorithms must be fast, the quality of ranking, and whether good results have been left out and bad results included, is more important.
The appropriate search algorithm often depends on the data structure being searched, and may also include prior knowledge about the data. Some database structures are specially constructed to make search algorithms faster or more efficient, such as a search tree, hash map, or a database index. [2][full citation needed][3]
Search algorithms can be classified based on their mechanism of searching into 3 types of algorithms: linear, binary, and hashing. Linear search algorithms check every record for the one associated with a target key in a linear fashion.[4] Binary, or half interval searches, repeatedly target the center of the search structure and divide the search space in half. Comparison search algorithms improve on linear searching by successively eliminating records based on comparisons of the keys until the target record is found, and can be applied on data structures with a defined order.[5] Digital search algorithms work based on the properties of digits in data structures that use numerical keys.[6] Finally, hashing directly maps keys to records based on a hash function.[7]
Algorithms are often evaluated by their computational complexity, or maximum theoretical run time. Binary search functions, for example, have a maximum complexity of O(log n), or logarithmic time. This means that the maximum number of operations needed to find the search target is a logarithmic function of the size of the search space.
## Requirements
### General
* Allowed editors: vi, vim, emacs
* All your files will be compiled on Ubuntu 14.04 LTS
* Your programs and functions will be compiled with gcc 4.8.4 using the flags -Wall -Werror -Wextra and -pedantic
* All your files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
* You are not allowed to use global variables
* No more than 5 functions per file
* You are only allowed to use the printf function of the standard library. Any call to another function like strdup, malloc, … is forbidden.
* In the following examples, the main.c files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examples
* The prototypes of all your functions should be included in your header file called search_algos.h
* Don’t forget to push your header file
* All your header files should be include guarded
