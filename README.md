# Mobu-PluginBase-Python
Set the standard of arranging original Python Tools/Scripts

<br>

## Concepts
- Show up plugins in the tab menu from original distribution directory

    ![alt text](image-1.png)

    set two directory in `Users/<username>/Documents/MB/<version>/config/PythonStartup` folder

    - `Tools`   : Python Tools registered in FBTools
    - `Scripts` : Python Scripts which can be used as module
<br>

## Rules
### In the Scripts
- define `main()` to execute all functions in the module
- script name will be displayed in the menu 


### In the Tools
- In the main file, define `ActivateTool()` function below  

    ```python
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

- main script name will be displayed in the menu

<br>

## Mechanism to Add Tool
### Get Access to Main window
[pyfbsdk.FBGetmainWindow()](https://help.autodesk.com/cloudhelp/2025/ENU/MOBU-PYTHON-API-REF/namespacepyfbsdk.html#a168c7b3df16bd9358f8326cd57167134) can return the MotionBuilder main window.<br>
Searching its children widgets and find TabMenu : QtWidgets.QMenu.

```python
def getMainWindow() -> QtWidgets.QWidget:
    ptr = FBGetMainWindow()
    if ptr is not None:
        # convert the pointer to QWidget instance
        return wrapInstance(ptr, QtWidgets.QWidget)


# search and return TabMenu Widget 
def getTabMenu(win : QtWidgets.QWidget) -> QtWidgets.QMenu:
    if win is not None:
        # Search TabMenu Widget
        for child in win.children():
            if not str(type(child)).find("QtWidgets.QWidget") == -1:
                for childwidget in child.children():
                    if not str(type(childwidget)).find("QtWidgets.QMenuBar") == -1:
                        return childwidget

getTabMenu(getMainWindow())
```


<br>

### Add TabMenu
In the `PluginBase.py`, module name will be extracted from Tools/Scripts path  

```python
tabmenu = <TabMenu instance : QtWidgets.QMenu>
tmenu = tabmenu.addMenu("Tools")
smenu = tabmenu.addMenu("Scripts")

# if Tools
for file in os.listdir(<toolpath>):
    if file.endswith(".py"):
        module_name = file[:-3]
        module = importlib.import_module(module_name)
        
        # add submenu and connect module
        t = tmenu.addAction(module_name)
        t.triggered.connect(module.ActivateTool)

# if Scripts
for file in os.listdir(<scriptpath>):
    if file.endswith(".py"):
        module_name = file[:-3]
        module = importlib.import_module(module_name)

        # add submenu and connect module
        s = smenu.addAction(module_name)
        s.triggered.connect(module.main)
```

<br>