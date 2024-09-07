# -*- coding: utf-8 -*-

# IMPORTS
from Autodesk.Revit.DB import *

# VARIABLES
uidoc   = __revit__.ActiveUIDocument
doc     = __revit__.ActiveUIDocument.Document

# FUNCTIONS

# Get Selected Elements
def get_selected_elements(doc):
    """This function will return elements that are currently selected in Revit UI
    :params uidoc: uidoc where elements are selected
    return: list of selected elements
    """

    selected_elements = []

    for elem_id in uidoc.Selection.GetElementIds():
        elem = uidoc.Document.GetElement(elem_id)
        selected_elements.append(elem)

    return selected_elements


# Get Linked Models
def get_linked_docs(doc):
    """This function will return linked models, attached to our current Revit file
    :params doc: Current Document
    return: list of linked models in our current document
    """

    linked_docs = [
        link_instance.GetLinkDocument()
        for link_instance in FilteredElementCollector(doc).OfClass(RevitLinkInstance)
        if link_instance.GetLinkDocument()
    ]
    return linked_docs


# Get Project Basepoint Function
def get_base_point(linked_docs, pbp=False, sp=False):
    """This function will return which point to export
    :params pbp: bool param insert true/false whether you want Project basepoint to export
            sp: bool param insert true/false whether you want Survey point to export
    return: List of selected points"""

    # define empty values for pbp and sp
    project_base_point = None
    survey_point = None

    base_point = FilteredElementCollector(linked_docs).OfClass(BasePoint).WhereElementIsNotElementType().ToElements()
    for bp in base_point:
        if not bp.IsShared:
            project_base_point = bp
        else:
            survey_point = bp

    # Return Options
    if pbp and sp:
        return project_base_point, survey_point
    elif pbp:
        return project_base_point
    elif sp:
        return survey_point
    else:
        return None
