# -*- coding: utf-8 -*-
import ezdxf
drawingname=
blockrefs = modelspace.query(’INSERT[name=="Part12"]’) # get all INSERT entities with entity.dxf.name == "Part12"
entity = blockrefs[0] # process first entity found
for attrib in entity:
if attrib.dxf.tag == "diameter": # identify attribute by tag
attrib.dxf.text = "17mm" # change attribute content