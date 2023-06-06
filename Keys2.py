
#script to remove keys and zero out controls on selected

import maya.cmds as cmds

nscontrols=cmds.ls(sl=True)


cmds.cutKey(nscontrols, s=True,clear=False)

for each in nscontrols:
	print(each)
	keyable = cmds.listAttr(each, k=True, u= True)
	print(keyable)
	for key in keyable:
		defaults =cmds.attributeQuery(key,n=each,ld=True)
		for dv in defaults:
			cmds.setAttr(each+'.'+key,dv)
