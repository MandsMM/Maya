#Allows you to x-ray geometry and make it unselectable. Select the geo that needs an x-ray then run script. Select geo and run script again to make it visable again
from maya import cmds

selected = cmds.ls(sl=True)

for item in selected:
	cmds.setAttr(item+'.overrideEnabled', 1)
	on=cmds.displaySurface(item, q=True ,xRay=True)
	if on == [True]:
	    cmds.displaySurface(item, xRay=False)
	    cmds.setAttr(item+'.overrideDisplayType',0)
	else:
		cmds.displaySurface(item, xRay=True )
		cmds.setAttr(item+'.overrideDisplayType',2)


#------------------------------------------------------

#Allows you to x-ray geometry. Select the geo that needs an x-ray then run script. Select geo and run script again to make it visable again
from maya import cmds

selected = cmds.ls(sl=True)

for item in selected:
	on=cmds.displaySurface(item, q=True ,xRay=True)
	if on == [True]:
	    cmds.displaySurface(item, xRay=False)
	else:
		cmds.displaySurface(item, xRay=True )

#------------------------------------------------------

#Sets the selected geo as a template. Select geo and run script again to make it visable again
from maya import cmds

selected = cmds.ls(sl=True)

for item in selected:
    on = cmds.getAttr(item+'.template')
    if on == True:
        cmds.setAttr(item+'.template', 0)
    else:
        cmds.setAttr(item+'.template', 1)