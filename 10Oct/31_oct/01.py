class Vote:
    def __init__(self,name,vid,voted_for):
        self.name = name
        self._v_id = vid
        self.__voted_for = voted_for

    @property
    def get_v_id(self):
        return str(self._v_id)[-3::]
    
    @get_v_id.setter
    def set_v_id(self,new_id):
        self._v_id = new_id

vid1 = Vote('Jahnvi',123456,'Toe')
vid2 = Vote('Shrushti',123456,'Rose')
vid3 = Vote('Sujal',123456,'Bike')
