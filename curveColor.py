
import maya.cmds as mc

#Create the user interface

if mc.window("newWin",exists = True):
    mc.deleteUI("newWin")

myWindow = mc.window("newWin", t="Curve color", w=50, h=50)
mainLayout = mc.columnLayout(adj = True)

rColor = mc.textFieldGrp(l= "Red value", editable = True)
gColor = mc.textFieldGrp(l= "Green value", editable = True)
bColor = mc.textFieldGrp(l= "Blue value", editable = True)

mc.separator(height=10,style='none')
mc.button(l="Set", c="color()",annotation="set the colors, then select curves to run")

mc.separator(height=10,style='none')
mc.text( label='yellow 1,1,0 | green 0,1,0 | turq 0,1,1 | magenta 1,0,1' )
mc.separator(height=10,style='none')


mc.showWindow(myWindow)



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



def color():

    #Universally change colour of a control
    
    #To make a list from selections
    sel = cmds.ls(sl=True) #select curves

    if not sel:
        mc.confirmDialog( title='Notice', message='Please select curves to change color')
    else:
        r = mc.textFieldGrp(rColor, q=True,text=True) 
        g = mc.textFieldGrp(gColor, q=True,text=True) 
        b = mc.textFieldGrp(bColor, q=True,text=True) 

        if not r or not g or not b:
            mc.confirmDialog( title='Notice', message='Please set values for RGB')
        else:
            
            selected = mc.listRelatives(sel, s=True) #gets the shape of the curve
            #print (selected)
            for y in selected:
                #print(y)
                mc.setAttr(y+'.overrideEnabled',1)
                mc.setAttr(y+'.overrideRGBColors',1)
                mc.setAttr(y+'.overrideColorRGB',int(r),int(g),int(b)) #change the color
            mc.confirmDialog( title='Notice', message='Colors changed')





