# Mobu-PluginBase-Python
Set the standard of arranging original Python Tools/Scripts
<br>

## Concepts
- Show up plugins in the tab menu from original distribution directory

![alt text](image-1.png)
<br>

- set two directory in `Users/<username>/MB/<version>/config/PythonStartup`
    - `Tools`   : Python Tools registered in FBTools
    - `Scripts` : Python Scripts which can be used as module

<br>

## Rules
### Scritps
- define `main()` to execute all functions in the module


### Tools
- In the main file, define `ActivateTool()` function below  

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