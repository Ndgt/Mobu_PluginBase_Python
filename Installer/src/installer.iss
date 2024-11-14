[Setup]
AppName=Mobu_PluginBase_Python
AppVersion=1.0
DefaultDirName={pf}\Autodesk

// Installer Name
OutputBaseFilename=PluginBase_Setup

// Display install path check
DisableDirPage=no

// do not create uninstaller
Uninstallable=no


[Code]
var
  VersionSelected: string;

function ResetDefaultInstallPath: string;
begin
  if VersionSelected = 'MotionBuilder 2024' then
    Result := 'C:\Program Files\Autodesk\MotionBuilder 2024\bin\config\PythonStartup'
  else if VersionSelected = 'MotionBuilder 2023' then
    Result := 'C:\Program Files\Autodesk\MotionBuilder 2023\bin\config\PythonStartup'
  else
    Result := 'C:\Program Files\Autodesk\MotionBuilder 2025\bin\config\PythonStartup';
end;

// get event from dropdown list
procedure VersionComboBoxChange(Sender: TObject);
begin
  VersionSelected := TComboBox(Sender).Items[TComboBox(Sender).ItemIndex];
  WizardForm.DirEdit.Text := ResetDefaultInstallPath;
end;

// specify MotionBuilder Version
procedure InitializeWizard;
var
  Page: TWizardPage;
  VersionComboBox: TComboBox;
begin
  Page := CreateCustomPage(wpWelcome, 'Select version of MotionBuilder','');
  VersionComboBox := TComboBox.Create(Page);
  VersionComboBox.Parent := Page.Surface;
  VersionComboBox.Items.Add('select version');
  VersionComboBox.Items.Add('MotionBuilder 2025');
  VersionComboBox.Items.Add('MotionBuilder 2024');
  VersionComboBox.Items.Add('MotionBuilder 2023');
  VersionComboBox.ItemIndex := 0;  // default is 2025
  VersionComboBox.OnChange := @VersionComboBoxChange; 
end;



[Files]
Source: "../../src/*"; DestDir: "{app}"; Flags: recursesubdirs; Excludes: "__pycache__"

[Setup]
OutputDir="../"
