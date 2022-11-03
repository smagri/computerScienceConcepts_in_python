#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
#                          GRAPHS as datasstructures                      #
###############################################################################
# Graphs  offer  a  structure  for   capturing  a  wide  diversity  of
# relationships and  the connections that are  formed.  Eg connections
# between  cities, airplains,  to  ecological webs  among species,  to
# social networks.




# In a graph, we call the _"things” that we’re representing a “vertex”
# or a  node.  These are the  cities in our example.   The connections
# between nodes are edges. In our  example, these are the roads. Edges
# let  us know  that  there’s  a relation  between  the two  nodes—for
# example, that they’re connected by a road.

# The more  global option is  to represent a  graph as two  lists: one
# list of nodes and one list of edges.


# Each node  will contain  information about itself.  So, each  of our
# city nodes might contain just the name of a city, or each node could
# also  contain  other  information,  such  as  city  population,  GPS
# coordinates for the city, and so on.

# An edge would have the names of  the two nodes—in this case, the two
# cities that  it connects. If it’s  a weighted graph, the  edge would
# also store a weight, which in this  case might be the length of that
# road, in miles or kilometers.

# Let’s try to write code to support this. We’ll want two classes, one
# for the nodes and one for the  edges. Remember that a class helps us
# encapsulate the stuff  that goes together, so the  node class should
# incorporate  the  stuff  in  a  node,  and  the  edge  class  should
# incorporate the stuff in an edge.

# The node class will have a name for the city and a population. We’ll
# set these with  our initialization routine, which  sets the instance
# attributes  “_name” and  “_pop.”  This  is why  we  have the  “self”
# reference; each  node can have  a different name and  population. We
# make  sure that  we can  access  the name  and population  variables
# through two accessor functions, “getName” and “getPopulation.”


###############################################################################
#                      SELF self. and _init_ constructor#
###############################################################################
class node:
    def __init__(self, name, population=0): # i think this is the CONSTRUCTOR
        self._name = name
        self._pop = population
def getName(self):
    return self._name
def getPopulation(self):
    return self._pop


class edge:
    def __init__(self, name1, name2, weight=0):
        # city1 joins city2 by a road of length weight
        self._city1 = name1
        self._city2 = name2
        self._distance = weight
    def getName1(self):
        return self._city1
    def getName2(self):
        return self._city2
    def getNames(self):
        return (self._city1, self._city2)
    def getWeight(self):
        return self._distance

    
# define two lists, cities/nodes and roads/edges
cities = []
roads = []
city = node('Rivertown', 1000)
cities.append(city)
city = node('Brookside', 1500)
cities.append(city)
city = node('Hillsview', 500)
cities.append(city)
city = node('Forrest City', 800)
cities.append(city)
city = node('Lakeside', 1100)
cities.append(city)
road = edge('Rivertown', 'Brookside', 100)
roads.append(road)
road = edge('Rivertown', 'Hillsview', 50)
roads.append(road)
road = edge('Hillsview', 'Brookside', 130)
roads.append(road)
road = edge('Hillsview', 'Forrest City', 40)
roads.append(road)
road = edge('Forrest City', 'Lakeside', 80)
roads.append(road)


print(cities)
print(roads)



# In  addition to  the first  method  of storing  graphs—by keeping  a
# global list  of edges—there is  a second way:  by keeping a  list of
# edges in each node. This second type is called an adjacency list.

# The global list of all the edges is probably most useful if you find
# yourself regularly needing  to look at all of the  edges. That’s the
# approach commonly used to represent geometric models, like you would
# have in three-dimensional graphics.

# The second approach—the adjacency list, where you keep a list of the
# edges within each  node—is useful in most  typical graph operations,
# such  as  airline  connections,  social networks,  and  so  on.  The
# adjacency list works well because  most graph algorithms are already
# designed  to  work just  looking  at  one node  at  a  time and  its
# neighbors.


# The global list of all the edges is probably most useful if you find
# yourself regularly needing  to look at all of the  edges. That’s the
# approach commonly used to represent geometric models, like you would
# have in three-dimensional graphics.

# The second approach—the adjacency list, where you keep a list of the
# edges within each  node—is useful in most  typical graph operations,
# such as airline connections, social networks, and so on. T

# There is  also a third method  to store graphs, called  an adjacency
# matrix, in  which, instead  of list, there  are matrix  entries that
# note which nodes  are connected.  This can be  useful for operations
# where you need to quickly run  over many different values or perform
# certain computations that can be expressed using linear algebra.

#  An  adjacency matrix  can  be the  most compact  form  of a  graph,
#  especially when  there are many  edges. This  is a key  factor when
#  graphs are  huge.  And it’s  the fastest of the  representations if
#  you need to check whether a particular pair of cities is connected.

# Graph  algorithims examples:  Breadth-first  Search, Undirected  and
#  Directed  graphs, directions  between nodes/verticies  along edges.
#  Web pages and the links between  them form a directed graph. If web
#  page A has a  link to web page B, there’s  not necessarily one from
#  web page B back to web page A.  Others are connected and cycle.(see
#  notes in pdf).



###############################################################################
#                                  TREES as datastructures                    #
###############################################################################

# A  connected, undirected  graph that  does  not contain  a cycle  is
# called a tree. Trees are such a useful structure that a whole set of
# algorithms have been developed just for trees.

