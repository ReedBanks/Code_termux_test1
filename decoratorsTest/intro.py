# allows to increase the functionality of functions,classes without having to create sub-classes
"""
The @-notation is syntactic sugar that is equivalent to the following:
    my_function =   super_secret_function(my_function)
"""

def enable(func):
    """
    allow bulb to turn on
    """
    return func
    
def disable(func):
    """
    prevent bulb from turning on
    """
    return None
    
@enable    
def bulb_on():
    return "The bulb is on."
    
    
print(bulb_on())    