import Pallet
import BlankStack
class Robot:
    def __init__(self):
        self.Xcoordinate = 0 #from frame pallet
        self.Ycoordinate = 0  # from frame pallet
        self.Zcoordinate = 0 # from frame pallet


    def layerScan(self,actualLayerIndex,Pallet,BlankStack,sensorValue,):
        #start from the end of the pallet looking for the current column
        current_column = (Pallet.columns - 1) - ((Pallet.width - self.Xcoordinate) // BlankStack.width) #retrieve the actual column where i'm suppose to be with x coordinate
        thereIsStackForHowMuchRows =(sensorValue - 100) // BlankStack.depth
        #Mark as false if the stack is not present
        for i in range(thereIsStackForHowMuchRows):
            Pallet.layers[actualLayerIndex][(Pallet.rows -1) -i ][current_column] = False