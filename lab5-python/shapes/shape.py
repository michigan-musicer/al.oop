class Shape:
    def __init__(self, name):
        self._name = name
    
    def get_shape_name(self):
        return self.name
    
    def get_shape_type(self):
        raise NotImplementedError()
    
    def get_perimeter(self):
        raise NotImplementedError()
    
    def get_area(self):
        raise NotImplementedError()
