# Mobu-PluginBase-Python
Set the standard of arranging original Python Sripts/Tools
<br>

## Concepts
Show up plugins in the tab menu from original distribution directory
<br>


## Rules
### Scritps
- define `main()` to execute all functions in the module


### Tools
- define `ActivateTool()` function in the main file

    ```
    def ActivateTool():
        # define the Tool name 
        toolName = "<tool name>"

        # check the Tool already created
        if toolName in FBToolList:
            ShowToolByName(toolName)
    
        else:
            # declare tool
            tool = <Original Tool Class declare>
            FBAddTool(tool)
            ShowToolByName(toolName)
    ```