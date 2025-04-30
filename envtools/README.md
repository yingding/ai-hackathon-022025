# Introduction
Use Powershell 7x to run the cmds to create python venv with pip.
Use Anaconda Powershell Prompt to run the cmds to create python venv with conda.

## Create a windows native python venv using pip
To create a native windows venv on windows 11,
1. use windows store to install the python version first before calling this powershell script

2. Open Powershell and copy the following snippet to create a python venv 
```powershell
# the current project directory path C:\Users\<windows_user>\Documents\VCS\<project_name>
# change it accordingly to your path
$PROJ_DIR="$env:USERPROFILE\Documents\azurecode\ai-hackathon-022025";
cd "$PROJ_DIR";

$VERSION="3.13";
$ENV_NAME="agents";
$ENV_SURFIX="winpip";
$PM="pip";
$ENV_DIR="$env:USERPROFILE\Documents\";
.\envtools\create_env.ps1 -VERSION $VERSION -ENV_NAME $ENV_NAME -ENV_SURFIX $ENV_SURFIX -PM $PM -WORK_DIR $ENV_DIR;
```

Note:
*  this script will also install the notebook kernel for the python environment automatically.

## Install packages (general)
```powershell
$VERSION="3.13";
$ENV_NAME="agents";
$ENV_SURFIX="winpip";

$ENV_FULL_NAME = "$ENV_NAME$VERSION$ENV_SURFIX";
# with the closing "\"
$ENV_DIR="$env:USERPROFILE\Documents\";

# absolute path of requirements.txt to install for the python venv
$PROJ_DIR="$env:USERPROFILE\Documents\azurecode\ai-hackathon-022025";
$SubProj="backend\app" 
$PackageFile="$PROJ_DIR\$SubProj\requirements.txt";

& "$ENV_DIR$ENV_FULL_NAME\Scripts\Activate.ps1";
Invoke-Expression "(Get-Command python).Source";

& "python" -m pip install --upgrade pip;
& "python" -m pip install -r $PackageFile --no-cache-dir;

deactivate
```