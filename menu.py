'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++
	HTMLDigger
	Created By Anupam Biswas
	contact Me :anupam-b@mpcfilm.com
+++++++++++++++++++++++++++++++++++++++++++++++++++++++'''
import os
import nuke
import Label_new
import ShotDrop
import setReferenceFrame
import link_hub
import connectCamera
import labelAutobackdrop
import KnobScripter



toolBar= nuke.toolbar('Nodes')
p = toolBar.addMenu('HTMLDIGGER', icon= 'HTMLDigger.png')
t = p.addMenu('Python', icon= 'HTMLDigger_python.png')
f = p.addMenu('Group', icon= 'grunge-group.png')


#shortcut for keylight
p.addCommand('Keyer/Keylight', 'nuke.createNode("Keylight")', 'ctrl+k', icon = 'Keylight.png')
p.addCommand('Python/setRefframe', 'setReferenceFrame.setRefframe()', 'z')
p.addCommand("copy node and keep inputs", "link_hub.copyKeepInputs(nuke.selectedNode())", "Alt+c")
p.addCommand("link", "link_hub.linkTools()","Ctrl+l")



 #KnobDefault

nuke.knobDefault("Read.label", 'Frame_Range\n[value first] - [value last]')
nuke.knobDefault("Premult.channels", "all")
nuke.knobDefault("Merge2.label", "BBox: [value bbox]")
nuke.knobDefault('Shuffle.label', '[value in]')


#adding Python Script------------------------------------------------------------------------------------------------------------

t.addCommand("Label_new", "Label_new.func_tion()", "n", icon= "Bridge-icon.png")

t.addCommand('Inputprocess', 'nuke.createNode("Saturation", "saturation 4");_useAsInputProcess()', ';', icon= 'ip.png')


'''__author__ = anupam-b
__version__ = 1.06'''




m=nuke.menu('Nuke')
n=m.addMenu('myTools',icon="grunge-group.png")
n.addCommand("python/DropFile", "dropRead()", "shift+d")
n.addCommand("python/shotDrop", "ShotDrop.shotDrop()", "shift+v")
n.addCommand("H_Group/H_dot", "nuke.createNode('H_Dot.nk')", ",")
n.addCommand("H_Group/Switch", "nuke.createNode('switch.nk')")
n.addCommand("H_Group/ContactSheet", "nuke.createNode('ContactSheet.nk')")

n.addCommand("python/connectCam", "connectCamera.connectCamera()", icon= "Camera.png", index=0)
#n.addCommand("python/HBackdrop", "autoBackdrop.autoBackdrop()", "ctrl+b", icon= "Backdrop.png", index=1)



toolbar = nuke.menu("Nodes")

def dropRead():
	node = nuke.selectedNode()
	file = node["file"].value()
	nuke.delete(node)
	nuke.tcl("drop", file)

'''
def dropTCL():
	Path = "//cosmossrv03/Leo_Da_Vinci/POST_PRODUCTION/06_Render_Output/LDV_EP_001/"
	P = nuke.getInput("path", "SH_001")
	nuke.tcl("drop", Path + P)
'''

 #KnobDefault

nuke.knobDefault("Read.label", 'Frame_Range\n[value first] - [value last]')
nuke.knobDefault("Premult.channels", "all")
nuke.knobDefault("Merge2.label", "BBox: [value bbox]")
nuke.knobDefault('Shuffle.label', '[value in]')
