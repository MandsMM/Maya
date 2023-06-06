#blendshape weight paint assistant, to paint half or copy and paste painting

import maya.cmds


#UI
if cmds.window("newWin",exists = True):
    cmds.deleteUI("newWin")

myWindow = cmds.window("newWin", t="Blendshape Paint Weight transfer", w=50, h=100)
mainLayout = cmds.columnLayout(adj = True)


cmds.separator(height=20,style='in')

cmds.button(l="Paint half", c="painthalf()")

cmds.separator(height=20,style='in')

cmds.button(l="Copy", c="copyWeight()",bgc=[0.207,0.440,0.440])


cmds.separator(height=10,style='in')

cmds.button(l="Paste", c="pasteWeight()",bgc=[0.332,0.471,0.471])




cmds.setParent(mainLayout)

cmds.separator(height=10,style='none')


cmds.showWindow(myWindow)


#-------------------------------------------------------------------------------------------------------------

#Paints half of the geometry blendshape based on the geo name - left or right
def painthalf():

    selectGeo = cmds.ls(sl=True)[0]
    history = cmds.listHistory( selectGeo )
    blendsh = cmds.ls( history, type = 'blendShape')[0]

    right_verts = []
    left_verts = []
    # get vertices
    verts = cmds.ls(selectGeo+".vtx[*]", fl=True)

    #check if mesh is left or right and remove weights

    if '_lf' in selectGeo:

        for vert in verts:
            if maya.cmds.pointPosition(vert, local=True)[0] < 0:
                right_verts.append(vert)


        for Rvert in right_verts:
            vertnum = Rvert[Rvert.index("[") + 1: Rvert.index("]")] #get the number in the string between []
            cmds.setAttr(blendsh+'.inputTarget[0].baseWeights['+str(vertnum)+']', 0)    
        print(selectGeo+' painted')
        print(blendsh+'.inputTarget[0].baseWeights['+str(vertnum)+']')

    if '_rt' in selectGeo:


        for vert in verts:
            if maya.cmds.pointPosition(vert, local=True)[0] > 0:
                left_verts.append(vert)    


        for Lvert in left_verts:
            vertnum = Lvert[Lvert.index("[") + 1: Lvert.index("]")] #get the number in the string between []
            cmds.setAttr(blendsh+'.inputTarget[0].baseWeights['+str(vertnum)+']', 0)
        print(selectGeo+' painted')

    cmds.dgdirty(allPlugs=True) #refresh viewport

#Copy blendshape weights
def copyWeight():


    selected = cmds.ls(sl=True)[0]

    verts = cmds.ls(selected+".vtx[*]", fl=True)
    longList = len(verts) -1

    #get the blendshape
    history = cmds.listHistory(selected)
    blendS = cmds.ls( history, type = 'blendShape')[0]

    copyWeight.weights = cmds.getAttr(blendS+'.inputTarget[0].baseWeights[0:'+str(longList)+']') #specifiying the verts because maya is being buggy
    copyWeight.identity = cmds.getAttr(blendS+'.inputTarget[0].baseWeights', multiIndices=True)

    print("copied")


#paste weights
def pasteWeight():


    selected = cmds.ls(sl=True)[0]
    history = cmds.listHistory(selected)
    blendS = cmds.ls( history, type = 'blendShape')[0]

    for num, value in enumerate(copyWeight.identity):
        vertnum =  str(value).replace("L", "")
        cmds.setAttr(blendS+'.inputTarget[0].baseWeights['+str(vertnum)+']', copyWeight.weights[num])

    print("pasted")





