__title__ = "Hello BIM World!"
__author__ = "Eden Falaka"
__doc__ = """This is Hello World Button. Click on it to see what happens"""


# VARIABLES
uidoc = __revit__.ActiveUIDocument
# CUSTOM IMPORT
from Snippets._selection import get_selected_elements

if __name__ == '__main__':
    print(get_selected_elements(uidoc))