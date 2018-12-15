import random
import numpy as np
from graphics import *

class Utility:
   @staticmethod
   def matrixGenerator(row, col):
       Matrix = [[0 for x in range(col)] for y in range(row)]
       probabDistribution = [[0 for x in range(col)] for y in range(row)]
       intialProbability = 1/(row*col)
       for i in range(0, row, 1):
            for j in range(0, col, 1):
                prob = random.random()
                probabDistribution[i][j] = intialProbability
                if prob < 0.2:
                    Matrix[i][j] = 1
                elif prob < 0.4:
                    Matrix[i][j] = 2
                elif prob < 0.5:
                    Matrix[i][j] = 3
                else:
                    Matrix[i][j] = 4
       return Matrix, probabDistribution

   #method to update the probabilities and normalizing
   @staticmethod
   def updateProbabilities(probMatrix,falseNegative,row, col,location_x,location_y,grid,rowWindowSize,colWindowSize,textMatrix):
       denominator = probMatrix[location_x][location_y] * falseNegative + 1 - probMatrix[location_x][location_x]
       updateInGrid = False #make it true to update the grid
       sum = 0.0
       for i in range(0, row, 1):
           for j in range(0, col, 1):
               if i==location_x and j == location_y:
                   probMatrix[i][j] = (probMatrix[location_x][location_y] * falseNegative) / denominator
               else:
                   probMatrix[i][j] = probMatrix[i][j] / denominator;
               #print(probMatrix[i][j])
               sum = sum + probMatrix[i][j]
               if updateInGrid:
                   number = round(probMatrix[i][j], 2)
                   text = format(number, '0.3f')
                   if number < 0.001:
                       text = '<0.001'
                   textMatrix[i][j].setText(text)

       for i in range(0, row, 1):
           for j in range(0, col, 1):
               probMatrix[i][j] = probMatrix[i][j]*(1/sum)

   #Rule 1: At any time, search the cell with the highest probability of containing the target.
   @staticmethod
   def getProbabContainTarget(probMatrix,row,col,location_x,location_y):
       max = -1.0
       x_coord = 0;
       y_coord = 0;
       for i in range(0, row, 1):
           for j in range(0, col, 1):
               if probMatrix[i][j] > max:
                  max = probMatrix[i][j]
                  x_coord = i
                  y_coord = j
       return x_coord, y_coord, (abs((x_coord -location_x)) + abs((y_coord-location_y)))

   #Rule 2: At any time, search the cell with the highest probability of finding the target.
   @staticmethod
   def getProbabFindingTarget(probMatrix,probOfLandScapes,originalMatrix,row,col,location_x,location_y):
       max = -1.0
       x_coord = 0;
       y_coord = 0;
       for i in range(0, row, 1):
           for j in range(0, col, 1):
               temp_probab = probMatrix[i][j]*(1-probOfLandScapes[originalMatrix[i][j]-1])
               if temp_probab > max:
                  max = temp_probab
                  x_coord = i
                  y_coord = j
       return x_coord, y_coord, (abs((x_coord -location_x)) + abs((y_coord-location_y)))

   @staticmethod
   def resetProbabilityDistribution(probMatrix,row,col):
       intialProbability = 1/(row*col)
       for i in range(0, row, 1):
            for j in range(0, col, 1):
                probMatrix[i][j] = intialProbability

   @staticmethod
   def calculateLocation(row, col,location_x,location_y,probOfLandScapes,originalMatrix,probMatrix):
       min = -1.0
       d = 0
       x_coord = 0;
       y_coord = 0;
       for i in range(0,row,1):
           for j in range(0,col,1):
               if i==location_x and j == location_y:
                   continue
               d = abs((i-location_x)) + abs((j-location_y))
               temp_probab = ((probMatrix[i][j]* probOfLandScapes[originalMatrix[i][j]-1]) / (d))
               if(min <  temp_probab):
                   min = temp_probab
                   x_coord = i;
                   y_coord = j;
       return x_coord,y_coord,d

   @staticmethod
   def makeTransitions(row,col,location_x, location_y,originalMatrix,transitions):
       transitions.append(originalMatrix[location_x][location_y])
       tempLandScapes = []
       if location_x - 1 >= 0 and originalMatrix[location_x-1][location_y] != originalMatrix[location_x][location_y]:
         tempLandScapes.append(originalMatrix[location_x-1][location_y])
       if location_x + 1 < row and originalMatrix[location_x+1][location_y] != originalMatrix[location_x][location_y]:
         tempLandScapes.append(originalMatrix[location_x+1][location_y])
       if location_y - 1 >= 0 and originalMatrix[location_x][location_y-1] != originalMatrix[location_x][location_y]:
         tempLandScapes.append(originalMatrix[location_x][location_y-1])
       if location_y + 1 < col and originalMatrix[location_x][location_y+1] != originalMatrix[location_x][location_y]:
         tempLandScapes.append(originalMatrix[location_x][location_y+1])
       if len(tempLandScapes)!=0:
         transitions.append(random.choice(tempLandScapes))

   @staticmethod
   def updateMovementProbability(row,col,trasitions, probMatrix,originalMatrix,temporaryProbability):
       sum = 0.0
       if len(trasitions)<=1:
           return
       for i in range(0,row,1):
          for j in range(0,col,1):
              if originalMatrix[i][j] in trasitions:
                  intermediate = float(0.0)
                  if i - 1 >= 0 :
                     if originalMatrix[i - 1][j] != originalMatrix[i][j] and originalMatrix[i - 1][j] in trasitions :
                            intermediate+=probMatrix[i-1][j]
                  if i + 1 < row:
                     if originalMatrix[i + 1][j] != originalMatrix[i][j] and originalMatrix[i + 1][j] in trasitions:
                            intermediate+=probMatrix[i+1][j]
                  if j - 1 >=0:
                     if originalMatrix[i][j-1] != originalMatrix[i][j] and originalMatrix[i][j-1] in trasitions:
                            intermediate+=probMatrix[i][j-1]
                  if j + 1 < col:
                     if originalMatrix[i][j+1] != originalMatrix[i][j] and  originalMatrix[i][j+1] in trasitions:
                            intermediate+=probMatrix[i][j+1]
                  temporaryProbability[i][j] = intermediate
                  #print("intermediate:", intermediate)
              else:
                  temporaryProbability[i][j] = 0.0

              sum+=temporaryProbability[i][j]
              #print("moving target sum :" , sum)
       #print("here")
       for i in range(0,row,1):
            for j in range(0,col,1):
                   probMatrix[i][j] = temporaryProbability[i][j]/sum
