# -*- coding: utf-8 -*-

# IMPORTS
from Autodesk.Revit.DB import *

# VARIABLES
app = __revit__.Application

#FUNCTIONS
def convert_internal_to_m(length):
    """Function to convert internal units to meters.
    :param length: length in internal Revit units
    :return: length in Metets, roundeed to 2nd digit"""
    rvt_year = int(app.VersionNumber)

    # RVT < 2022
    if rvt_year < 2022:
        return UnitUtils.Convert(length,
                                 DisplayUnitType.DUT_DECIMAL_FEET,
                                 DisplayUnitType.DUT_METERS) # Change to any other unit if needed...
    # RVT >= 2022
    else:
        return UnitUtils.ConvertFromInternalUnits(length, UnitTypeId.Meters)