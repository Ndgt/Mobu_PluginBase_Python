# Mobu-PyPluginArrange
Set the standard of arranging original Python Sripts/Tools
<br>

## Concepts
**Show up plugins in the tab menu from original distribution firectory**


## Rules
### Scritps
- define `main()` to execute all functions in the module


### Tools
- define

```
def ActivateTool():
    # define the Tool name 
    toolName = "<tool name>"

    # check the Tool already created
    if toolName in FBToolList:
        ShowToolByName(toolName)
    
    else:
        tool = WigTool(toolName)
        FBAddTool(tool)
        ShowToolByName(toolName)
```