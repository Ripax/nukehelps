nuke.pluginAddPath("./py")
nuke.pluginAddPath("./icons")
nuke.pluginAddPath("./group")
nuke.pluginAddPath("./widget")
nuke.pluginAddPath(" ./gismos")
nuke.pluginAddPath("./KnobScripter")

#-------------------Add Format----------------------------------------------
__HTM_WorkingRes_Ana = '1920 1080 0 0 1920 1080 1.0 FullHD_Widescreen'
__HTM_WorkingRes_half = '960 399 0 0 960 399 1.0 HalfHD_Widescreen'


nuke.addFormat(__HTM_WorkingRes_Ana)
nuke.addFormat(__HTM_WorkingRes_half)


#------------------------end------------------------------------------------


#Knob Default----------------------------------------------------------
nuke.knobDefault('Root.format', __HTM_WorkingRes_Ana)
nuke.knobDefault('Root.fps', '24')