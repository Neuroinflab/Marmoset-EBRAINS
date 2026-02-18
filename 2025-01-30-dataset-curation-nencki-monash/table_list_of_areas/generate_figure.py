#!/usr/bin/env python
# encoding: utf-8

import numpy as np
import pandas as pd

# Spreadsheet with the definitions of the cortical areas:
C_AREAS_FILE = "areas.xlsx"
areas = pd.read_excel(C_AREAS_FILE)
C_OUTPUT_FILENAME = "areas_.svg"

svg_begin = """<?xml version="1.0"?>
 <svg xmlns="http://www.w3.org/2000/svg"
      xmlns:xlink="http://www.w3.org/1999/xlink"
      width="680px" height="945px">
 """
svg_end = """</svg>"""

index_form = """<text x="%d" y="%d" style="fill:rgb(0,0,0);" font-family="Arial, Helvetica, sans-serif" font-size="8pt">(%s)</text>"""
rect_form = """<rect width="22" height="9" x="%d" y="%d" style="fill:rgb(%d, %d, %d);stroke-width:0.75px;stroke:rgb(0, 0, 0)" />"""
abbrev_form = """<text x="%d" y="%d" style="fill:rgb(0,0,0);" font-family="Arial, Helvetica, sans-serif" font-size="8pt">%s</text>"""
fullname_form = """<text x="%d" y="%d" style="fill:rgb(0,0,0);" font-family="Arial, Helvetica, sans-serif" font-size="8pt">%s</text>"""

def index(x, y, text):
    return index_form % (x, y, text)

def colorbox(x, y, xxx_todo_changeme):
    (r, g, b) = xxx_todo_changeme
    return rect_form % (x, y, r, g, b)

def abbrev(x, y, text):
    return abbrev_form % (x, y, text)

def fullname(x, y, text):
    return abbrev_form % (x, y, text)


fh = open(C_OUTPUT_FILENAME, "w")

fh.write(svg_begin)

i = 0
for idx, row in areas.iterrows():
    if row.is_leaf_node:

        i+=1

        y, x, area_index = (i+1) * 12 -2, -30, row.id
        fh.write(index(x, y, str(area_index)) + "\n")

        y, x, r, g, b = i * 12, 0, row.color_r, row.color_g, row.color_b
        fh.write(colorbox(x, y, (r, g, b)) + "\n")

        y, x =  (i+1) * 12 - 2, 31
        fh.write(abbrev(x, y, str(row.abbrev)) + "\n")

        y, x =  (i+1) * 12 - 2, 88
        fh.write(fullname(x, y, row.display_name) + "\n")

fh.write(svg_end)

fh.close()
