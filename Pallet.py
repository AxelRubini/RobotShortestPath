from venv import create

import BlankStack
class Pallet :
    def __init__(self,width,depth,height,BlankStack):
        self.number_of_layers = None
        self.rows = None
        self.columns =None
        self.BlankStack = BlankStack
        self.layers = list()
        self.width = width
        self.depth = depth
        self.height = height
        self.create_pallet(self.BlankStack)



    def create_layer(self,BlankStack):

        self.columns = self.width // BlankStack.width
        self.rows = self.depth // BlankStack.depth
        layer = list()
        for i in range(self.rows):
            new_row = list()
            for j in range(self.columns):
                new_row.append(True)

            layer.append(new_row)

        return layer

    def create_pallet(self,BlankStack):
        self.number_of_layers = self.height // BlankStack.height

        for i in range(self.number_of_layers):
            self.layers.append(self.create_layer(BlankStack))




