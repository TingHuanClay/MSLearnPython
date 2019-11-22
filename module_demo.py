import helpers

helpers.display("This is a sample message")

helpers.display("This is a warning message", True)

"""
You can import specific funciton from the module
Besides, if the method is the unique name, you can skip the modeule name
"""
from helpers import display
display("This is a sample message")
display("This is a warning message", True)