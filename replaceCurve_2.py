#Replaces a curve shape on a rig, or a broken curve

import maya.cmds as mc
import maya.mel as mel

#UI 
if mc.window("newWin",exists = True):
    mc.deleteUI("newWin")

myWindow = mc.window("newWin", t="replace curve", w=300, h=100)
mainLayout = mc.columnLayout(adj = True)

mc.separator(height=10,style='in')

mc.rowColumnLayout(nc=2,cw=[(1,400),(2,100)],columnOffset=[(1,'left',5),(2,'left',5)])
sourceA = mc.textFieldGrp(l= "New Shape", editable = True)
mc.button(l="Set", c="setsource()")
replceB = mc.textFieldGrp(l= "Replace Shape", editable = True)
mc.button(l="Set", c="setReplace()")


mc.setParent(mainLayout)

mc.separator(height=10,style='none')

mc.button(l="Transform", c="changeShape()")

mc.separator(height=20,style='none')


mc.showWindow(myWindow)


#--------------------

#set the source curve
def setsource():
    setsource.source = mc.ls(selection = True, fl =True)[0]
    mc.textFieldGrp(sourceA,tx=str(setsource.source), edit=True)

#set destination curve
def setReplace():
    setReplace.replce = mc.ls(selection = True, fl =True)[0]
    mc.textFieldGrp(replceB,tx=str(setReplace.replce), edit=True)


def changeShape():
	#Match the transform 
	mc.matchTransform(setsource.source,setReplace.replce)

    #change the shape
	mc.connectAttr(setsource.source+'.worldSpace[0]',setReplace.replce+'.create')

	#clear history
	cmds.delete(setsource.source, constructionHistory = True)
	cmds.delete(setReplace.replce, constructionHistory = True)
	mc.makeIdentity(setReplace.replce, apply=True )






