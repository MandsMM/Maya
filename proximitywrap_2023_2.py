#Creates a proximity wrap on the source and target, also setting the parameters
#Creates a normal wrap

import maya.cmds as cmds
import maya.internal.nodes.proximitywrap.node_interface as node_interface

#the prox wrap---------------------------------------------

def createProximityWrap(source, target,smoothInf,smoothN):

    deformer = cmds.deformer(target, type='proximityWrap', name=target+ '_pWrap')[0]
    proximity_interface = node_interface.NodeInterface(deformer)
    shape = cmds.listRelatives(source,s=True)
    proximity_interface.addDrivers(shape[0])

    #set attributes
    cmds.setAttr(deformer + '.maxDrivers', 1)
    cmds.setAttr(deformer + '.smoothInfluences', smoothInf)
    cmds.setAttr(deformer + '.smoothNormals', smoothN)

    return deformer

createProximityWrap('Source_geo','Target_geo',5,3)


#the wrap---------------------------------------------

#target,source
cmds.select('Target_geo','Source_geo')
cmds.CreateWrap( )




