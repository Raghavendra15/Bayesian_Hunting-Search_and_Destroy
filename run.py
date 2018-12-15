import numpy as np
from stationaryTarget import *
from movingTarget import *
from Utility import *
from GridGenerator import *
#All the algorithms are written in Utility(Helper) class
#Stationary Target File is used when the target is fixed
#Moving target file is used when the target is constantly jumping from one cell to another
#paramters can be passed for Rule1, Rule 2 and if Rule 3 is passed it will handle the Question 4 of the assignment
#uncomment line 39-88 for analysing stationary target
windowsize=400
rowSize = 3
colSize = 3
rowWindowSize = windowsize
colWindowSize = windowsize
rowRem = rowWindowSize% rowSize
colRem = colWindowSize % colSize
if rowRem!=0:
    rowWindowSize-=rowRem
xr = rowWindowSize//rowSize
if colRem!=0:
    colWindowSize-=colRem
xc = colWindowSize//colSize
probOfLandScapes = [0.1, 0.3, 0.7, 0.9] #negative probabilities
originalMatrix, probabilityDistribution = Utility.matrixGenerator(rowSize,colSize)
print(originalMatrix)
gridobj=GridGenerator(originalMatrix,rowWindowSize,colWindowSize,probabilityDistribution)
#solvedGrid,textMatrix = gridobj.generate_grid(rowSize,colSize,xr,xc)
solvedGrid = []
textMatrix = []
target_x = 2
target_y = 2
landScapeTypes = {1:'flat', 2:'hill', 3:'forest' ,4:'cave'}
resultsRule1Cost = {'flat':0, 'hill':0, 'forest':0 ,'cave':0}
resultsRule1NumberOfSearches = {'flat':0, 'hill':0, 'forest':0 ,'cave':0}
stationaryTarget(originalMatrix,probabilityDistribution,probOfLandScapes,target_x,target_y,rowSize,colSize,solvedGrid,xr,xc,textMatrix,'Rule 1', landScapeTypes[originalMatrix[target_x][target_y]]).solve(resultsRule1NumberOfSearches,resultsRule1Cost)
# solvedGrid.getMouse()
# solvedGrid.close()
# print("******************************************stationary target analysis*****************************")
# map = {}
# map[1] = 0
# map[2] = 0
# map[3] = 0
# map[4] = 0
# landScapeTypes = {1:'flat', 2:'hill', 3:'forest' ,4:'cave'}
# resultsRule1NumberOfSearches = {'flat':0, 'hill':0, 'forest':0 ,'cave':0}
# resultsRule1Cost = {'flat':0, 'hill':0, 'forest':0 ,'cave':0}
# resultsRule2NumberOfSearches = {'flat':0, 'hill':0, 'forest':0 ,'cave':0}
# resultsRule2Cost = {'flat':0, 'hill':0, 'forest':0 ,'cave':0}
# resultsRule3NumberOfSearches = {'flat':0, 'hill':0, 'forest':0 ,'cave':0}
# resultsRule3Cost = {'flat':0, 'hill':0, 'forest':0 ,'cave':0}
# count = 0
# i = 0
# rule1NumberOfSearches= []
# rule1Cost = []
# rule2NumberOfSearches= []
# rule2Cost = []
#locationArray = []
# while i < 40:
#    target_x = np.random.randint(rowSize)
#    target_y = np.random.randint(rowSize)
#    originalMatrix, probabilityDistribution = Utility.matrixGenerator(rowSize,colSize)
#    print(i)
#    if map[originalMatrix[target_x][target_y]] < 10:
#       map[originalMatrix[target_x][target_y]]+=1
#       print("Rule 1")
#       rule1NumberOfSearches.append(stationaryTarget(originalMatrix,probabilityDistribution,probOfLandScapes,target_x,target_y,rowSize,colSize,solvedGrid,xr,xc,textMatrix,'Rule 1', landScapeTypes[originalMatrix[target_x][target_y]]).solve(resultsRule1NumberOfSearches,resultsRule1Cost).to_dict())
#       print("Rule 2")
#       rule2NumberOfSearches.append(stationaryTarget(originalMatrix,probabilityDistribution,probOfLandScapes,target_x,target_y,rowSize,colSize,solvedGrid,xr,xc,textMatrix,'Rule 2', landScapeTypes[originalMatrix[target_x][target_y]]).solve(resultsRule2NumberOfSearches,resultsRule2Cost).to_dict())
#       print("Rule 3")
#       rule2NumberOfSearches.append(stationaryTarget(originalMatrix,probabilityDistribution,probOfLandScapes,target_x,target_y,rowSize,colSize,solvedGrid,xr,xc,textMatrix,'Rule 3', landScapeTypes[originalMatrix[target_x][target_y]]).solve(resultsRule3NumberOfSearches,resultsRule3Cost).to_dict())
#       i+=1
#       print("##########################################")
#    count +=1
# print("count:" ,count)
# print("map: ", map)
# print("Rule 1 result searches:" , resultsRule1NumberOfSearches)
# print("Rule 1 result cost:" , resultsRule1Cost)
# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# print("Rule 2 result searches:" ,resultsRule2NumberOfSearches)
# print("Rule 2 result cost:" , resultsRule2Cost)
# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# print("Rule 3 result searches:" ,resultsRule3NumberOfSearches)
# print("Rule 3 result cost:" , resultsRule3Cost)
# print("*************************")
# print("Rule 1 Array :" ,rule1NumberOfSearches)
# print("*****************************************")
# print("Rule 2 Array :" ,rule2NumberOfSearches)

# print("******************************************moving target analysis*****************************")
# map = {}
# map[1] = 0
# map[2] = 0
# map[3] = 0
# map[4] = 0
# landScapeTypes = {1:'flat', 2:'hill', 3:'forest' ,4:'cave'}
# resultsRule1NumberOfSearches = {'flat':0, 'hill':0, 'forest':0 ,'cave':0}
# resultsRule1Cost = {'flat':0, 'hill':0, 'forest':0 ,'cave':0}
# resultsRule2NumberOfSearches = {'flat':0, 'hill':0, 'forest':0 ,'cave':0}
# resultsRule2Cost = {'flat':0, 'hill':0, 'forest':0 ,'cave':0}
# resultsRule3NumberOfSearches = {'flat':0, 'hill':0, 'forest':0 ,'cave':0}
# resultsRule3Cost = {'flat':0, 'hill':0, 'forest':0 ,'cave':0}
# rule1NumberOfSearches= []
# rule1Cost = []
# rule2NumberOfSearches= []
# rule2Cost = []
# count = 0
# i = 0
# while i < 100:
#    target_x = np.random.randint(rowSize)
#    target_y = np.random.randint(rowSize)
#    originalMatrix, probabilityDistribution = Utility.matrixGenerator(rowSize,colSize)
#    print(i)
#    if map[originalMatrix[target_x][target_y]] < 25:
#       map[originalMatrix[target_x][target_y]]+=1
#       print(originalMatrix)
#       print("Rule 1")
#       rule1NumberOfSearches.append(movingTarget(originalMatrix,probabilityDistribution,probOfLandScapes,target_x,target_y,rowSize,colSize,solvedGrid,xr,xc,textMatrix,'Rule 1', landScapeTypes[originalMatrix[target_x][target_y]]).solve(resultsRule1NumberOfSearches,resultsRule1Cost).to_dict())
#       print("Rule 2")
#       rule2NumberOfSearches.append(movingTarget(originalMatrix,probabilityDistribution,probOfLandScapes,target_x,target_y,rowSize,colSize,solvedGrid,xr,xc,textMatrix,'Rule 2', landScapeTypes[originalMatrix[target_x][target_y]]).solve(resultsRule2NumberOfSearches,resultsRule2Cost).to_dict())
#       #rint("Rule 3")
#       #rule2NumberOfSearches.append(movingTarget(originalMatrix,probabilityDistribution,probOfLandScapes,target_x,target_y,rowSize,colSize,solvedGrid,xr,xc,textMatrix,'Rule 3', landScapeTypes[originalMatrix[target_x][target_y]]).solve(resultsRule3NumberOfSearches,resultsRule3Cost).to_dict())
#       i+=1
#       print("##########################################")
#    count +=1
#
# print("count:" ,count)
# print("map: ", map)
# print("Rule 1 result searches:" , resultsRule1NumberOfSearches)
# print("Rule 1 result cost:" , resultsRule1Cost)
# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# print("Rule 2 result searches:" ,resultsRule2NumberOfSearches)
# print("Rule 2 result cost:" , resultsRule2Cost)
# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# print("Rule 3 result searches:" ,resultsRule3NumberOfSearches)
# print("Rule 3 result cost:" , resultsRule3Cost)
# print("*************************")
# print("Rule 1 Array :" ,rule1NumberOfSearches)
# print("*****************************************")
# print("Rule 2 Array :" ,rule2NumberOfSearches)
#solvedGrid.getMouse()
#solvedGrid.close()
