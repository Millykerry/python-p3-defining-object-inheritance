from vehicle import Vehicle

class Car(Vehicle):
    """Child class that inherits from Vehicle"""
    
    def go(self):
        """Overwrites the inherited go() method with car-specific behavior"""
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"