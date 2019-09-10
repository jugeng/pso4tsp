#Using Particle Swarm Algorithm to solve Travelling Salesman problem 
#Object programming approach for the sake of fun
#By Jugen Gawande started 10/09/19

import random 
import math

#For Terminal messages.


PopulationSize = 0 #Number of particles
TotalCities = -1  # Use a function to identify the number of cities present
cities = [] # Empty array of cities
distance_matrix = []
gBest_fitness = 0
gBest_route = []
iteration = 0

#learning rate
c1 = 0
c2= 0
""""
x = [5,10,12,2,14,15,3,6,8]
y = [6,5,11,1,6,10,8,6,10,2]
"""
x = [1,2,3,1,3,4,5]
y = [3,3,3,1,1,1,1]

class Particle:
    
    def __init__(self):
        self.pBest_fitness = -1
        self.pBest_route = []
        self.route = []
        self.fitness = 0
        #creates initial population
        for x in range(TotalCities):
            self.route.append(x)

        temp = self.route.pop(0)
        random.shuffle(self.route)
        self.route.insert(0, temp) 
        self.route.append(0)
        
        #To evaluate the routes generated uncomment below statement
        #print("CHECK: Particle created successfully -> ",self.route)

        
    def CalculateFitness(self):

        total_distance = 0
        global gBest_fitness

        for i in range(TotalCities):  
            total_distance = total_distance  + distance_matrix[self.route[i]][self.route[i+1]]
        
        #Using inverse because shorter the distance the better
        self.fitness = 1 / total_distance

        #Checking the best fitness of particle until this moment 
        if self.fitness > self.pBest_fitness:
            self.pBest_fitness = self.fitness
            #Clearing the best route of the particle to update with new one
            self.pBest_route.clear()
            self.pBest_route.extend(self.route)
            #print("MSG: Local best of particle updated ->", self.pBest_fitness,"-- route ->",self.pBest_route)
        
        if gBest_fitness < self.pBest_fitness:
            gBest_fitness = self.pBest_fitness
            #Clearing the best route of the particle to update with new one
            gBest_route.clear()
            gBest_route.extend(self.route)
            print("MSG: Global best updated ->", gBest_fitness,"-- route ->",gBest_route)
        
    def Crossover(self):
        int_route = []
        
        k = random.randint(1,TotalCities-1)
        #Crossover length
        m = c1 * random.randint(1,TotalCities-1) % TotalCities   #For Local Best
        n = c1 * random.randint(1,TotalCities-1) % TotalCities    #For Global Best

        int_route.append(0)
        #Crossover between pbest and gbest
        for x in range(n):

            if (k + x) >= TotalCities:
                
                r = (k + x) % TotalCities + 1
                int_route.append(gBest_route[r])
         
            else:
                int_route.append(gBest_route[k+x]) 
    
        #Cross over between pbest and x
        for x in range(m):
            if (k + x) >= TotalCities:
                r = (k + x) % TotalCities +1 
                int_route.append(self.pBest_route[r]) if self.pBest_route[r] not in int_route else int_route
            else:
                int_route.append(self.pBest_route[k+x]) if self.pBest_route[k+x] not in int_route else int_route 
  
        for x in range(len(self.route)): 
            int_route.append(self.route[x]) if self.route[x] not in int_route else int_route
        
        self.route = int_route[:]
        self.route.append(0)

    def Variation(self):
        k = random.random()
        if(k > 0.5):
            reverseVar()


    def reverseVar(self):
        s = random.randint(1,TotalCities / 2) % TotalCities
        e = random.randint(s,TotalCities) % TotalCities

        self.route[s:e] = reversed(self.route[s:e]) 

            

#int_route.append(self.pBest_route[k+x]) if self.pBest_route[k+x] not in int_route else int_route
class PSO:
    
    def __init__(self):
        self.swarm = []
        self.BuildGraph()
        self.DistanceMatrix()

    #Initialize the graph 
    def BuildGraph(self):
        global TotalCities

        for i in range(len(x)):
            cities.append( [x[i] ,y[i]])
            
        #To verify the list of cities and their coordinates (x,y) uncomment the line below
        #print(cities)
        TotalCities = len(cities)
        #Verify if city array is filled
        if len(cities)  > 0 :
            print('CHECK:',len(cities),"cities graphed successfully")
    
    def DistanceMatrix(self):
        a = []
        for x in range(TotalCities):
            cityA = cities[x]
            
            a = []
            for i in range(TotalCities):
                cityB = cities[i]   
                #Using Euclidean formula to calcualte distances
                a.append(math.sqrt(math.pow((cityB[0] - cityA[0]), 2) + math.pow((cityB[1] - cityA[1]), 2  )    ) )
             

            distance_matrix.append(a) 


    def GenerateSwarm(self):
        for i in range(PopulationSize):
            self.swarm.append(Particle())
        
        if len(self.swarm) == PopulationSize:
            print('CHECK: Intial population generated successfully')

        for i in range(PopulationSize):
            self.swarm[i].CalculateFitness()


    def runAlgo(self):
        for j in range(iteration):
                   
            print("Iteration:", j+1)
            for i in range(PopulationSize):
                self.swarm[i].Crossover()
                self.swarm[i].CalculateFitness()

            print("RESULT: Best distance =",1 / gBest_fitness )    
      
       
    

#print("MSG: Global best updated ->", gBest_fitness,"-- route ->",gBest_route)   

#PopulationSize = int(input("Enter population size: "))
PopulationSize =15

print('Set learning rate: {recommended-> 2}\n')
#c1 = int(input("c1: "))
#c2 = int(input("c2: "))
#iteration = int(input("Set number of iteration: "))
iteration = 50
c1 = 2
c2 = 2


#Assigning the number of cities detected to an integer variable
#TotalCities = len(cities)


#Create an instance of algorithm to run 
pso = PSO()

pso.GenerateSwarm()
pso.runAlgo()
