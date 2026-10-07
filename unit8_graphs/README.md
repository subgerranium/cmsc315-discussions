# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using Breadth-First Search (BFS).
This program represented relationships between songs using an adjacency list and showed how BFS could be used to 
explore those relationships.

## Learning Objectives

- Represent graphs using adjacency lists
- Implement BFS
- Use queues in graph traversal
- Analyze graph traversal behavior

## Requirements

1. Create a graph.
    - I created a graph using an adjacency list. Each node represented a song, and each edge represented a relationship 
   between songs. These relationships could represent similarities such as genre, artist, or listener preferences.  
   The initial graph contained six songs: Song A, Song B, Song C, Song D, Song E, and Song F. The graph contained 
   multiple connections between the songs. For example, Song A was connected to Song B and Song C.
2. Perform BFS traversal.
    - I implemented BFS using deque as a queue. The traversal started at Song A. The initial BFS traversal was: 
   Song A -> Song B -> Song C -> Song D -> Song E -> Song F 
   BFS visited Song A first and then explored its immediate neighbors, Song B and Song C. Then it continued to the next 
   level of connected songs. A set was used to keep track of visited nodes so that songs were not repeatedly processed.
3. Add nodes or edges.
    - I added Song G to the graph and connected it to Song E. The updated graph included:
    Song E: ['Song B', 'Song D', 'Song F', 'Song G']
    The updated BFS traversal was:
    Song A -> Song B -> Song C -> Song D -> Song E -> Song F -> Song G
    This showed how adding a new connection affected the traversal while leaving the existing relationships intact.
4. Demonstrate edge cases.
    - The first test used a starting node that was not contained in the graph: Missing start node (Song Z): []
    The BFS function returned an empty list instead of producing an error.
    - The second test used a graph containing only one node: Single-node graph: ['Song X']
   BFS correctly visited the only available node. 
    - The third test used an empty graph: Empty graph: []
   The function returned an empty list because there were no nodes available to traverse. 
5. Analyze BFS behavior.
    - In this music recommendation example, BFS could be used to find songs that were closely related to a user's 
   current song or listening preferences. Songs directly connected to the starting song could be considered before 
   songs that were more relationships away. BFS would generally be preferred over DFS when finding the shortest path or 
   closest connections in an unweighted graph was important. DFS would be better to use when the goal was to explore 
   deeply through one path before returning to other branches.
6. Create a real-world graph example.
    - A music streaming service could be a real world graph example that would begin with a song a user was listening 
   to and use BFS to explore related songs. The service could first examine songs directly connected to the current song
   and then explore songs connected at greater distances.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare BFS and DFS conceptually and describe real-world applications and use cases.

