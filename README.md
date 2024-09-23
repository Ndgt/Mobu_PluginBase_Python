# Mobu-PluginBase-Python
## 概要
独自のツール・スクリプトを起動するメニューをメニューバーに追加する。

  ![alt text](image-1.png)

以下の2つのフォルダを `C/Program Files/Autodesk/MotionBuilder <version>/bin//config/PythonStartup` ディレクトリに作成。独自のファイルをここに格納する。

- `Tools`   : FBToolListに登録されるツール
- `Scripts` : 単純なスクリプト

また、同ディレクトリに`PluginBase.py`を配置する。


<br>

## 規則
### ツール内
メインのファイルにて、以下の`ActivateTool()` 関数を定義する。

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


<br>

## 仕組み
### メニューバーへのアクセス
[pyfbsdk.FBGetmainWindow()](https://help.autodesk.com/cloudhelp/2025/ENU/MOBU-PYTHON-API-REF/namespacepyfbsdk.html#a168c7b3df16bd9358f8326cd57167134) はMotionBuilderのメインウィンドウのポインタを返す。<br>
メインウィンドウの子ウィジェットの一つが、上部のメニューバー。


```python
def getMenubar() -> QMenuBar:
    # get Main Window
    pMainW = FBGetMainWindow()
    if pMainW:
        #Convert pointer to any non-inappropriate type
        MainW = wrapInstance(pMainW, QMainWindow)
        menubar = MainW.menuWidget().children()[1]
        return menubar
```


### メニューの追加
`PluginBase.py`においてメニュー追加と実行するファイルの接続を設定する。

```python
mbar  = getMenubar()
tmenu = mbar.addMenu("Tools")
smenu = mbar.addMenu("Scripts")

# if tools
for tools_filepath in tools_dir.iterdir():
    if str(tools_filepath).endswith(".py"):
        module_name = tools_filepath.stem
        module = importlib.import_module(module_name)
        
        # add submenu and connect module
        t = tmenu.addAction(module_name)
        t.triggered.connect(module.ActivateTool)

# if scripts
for script_filepath in scripts_dir.iterdir():
    if str(script_filepath).endswith(".py"):
        s = smenu.addAction(script_filepath.stem)
        s.triggered.connect(lambda check=False, sp = str(script_filepath) : FBApplication().ExecuteScript(sp))

```
