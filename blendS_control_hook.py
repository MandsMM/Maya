#hookup blendshapes with same name as control


mycontrol='nurbsCircle1'
mesh = 'body_geo'
controlAtt= cmds.listAttr( control )


#Get the blendShape
history = cmds.listHistory(mesh)
blendS = cmds.ls( history, type='blendShape')

#Get the blend Shape Names
cmds.select(blendS)
blendSnames = cmds.listAttr( blendS[0] + '.w' , m=True )


for number, items in enumerate(blendSnames):
	if items in controlAtt:
		ctrAttrIndex = controlAtt.index(items)
		cmds.connectAttr(control+'.'+controlAtt[ctrAttrIndex], blendS[0]+'.'+items)






