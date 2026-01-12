import random

## Creates a Roulette Wheel object for a European Roulette Wheel with 37
## slots: 0 (green) and 1-36 (red/black)

class Slot:
    
    ## Will never be seen by user and only used to populate a wheel object.
    ## Just need a Constructor, accessors, and a __str__ method.
    
    def __init__(self, number):
        assert isinstance(number, int)  # Require number to be an int
        assert number >= 0 and number <= 36 # Requie it bein correct range
        
        self.number = number
        
        ## Assuming we have a valid number, assign color according to the rules
        ## of a roulette table.  Can be looked up online.
        ##
        ## You don't need to worry about this part - it just assigns the colors
        ## to the numbers
        
        if number == 0:
            self.color = 'Green'
        elif number >= 29:
            if number % 2 == 0:
                self.color = 'Red'
            else:
                self.color = 'Black'
        elif number >= 19:
            if number % 2 == 0:
                self.color = 'Black'
            else:
                self.color = 'Red'
        elif number >= 11:
            if number % 2 == 0:
                self.color = 'Red'
            else:
                self.color = 'Black'
        else:
            if number % 2 == 0:
                self.color = 'Black'
            else:
                self.color = 'Red'               

    ## Accessors
    def get_color(self):
        return self.color    
    def get_number(self):
        return self.number
    
    def __str__(self):
        return self.color + ' ' + str(self.number)


class RouletteWheel:
    def __init__(self):
        self.slots = []
        for k in range(37):
            self.slots.append(Slot(k))
        ## Ball does not star in a slot, so current slot isset to None to 
        ## begin with.  Need to use the spin method to get a result
        self.current_slot = None

    ## Spin the wheel - ball will fall in a random slot.
    def spin(self):
        self.current_slot = random.choice(self.slots)
    
    ## Accessor to find the current slot.  It returns a slot object.
    def get_slot(self):
        return self.current_slot
    
    