# Deploy as Azure App Service

1. Install Azure Cli, Azure App Service VScode extension

```powershell
az webapp list-runtimes --os linux | grep PYTHON
```

output
```console
  "PYTHON:3.13",
  "PYTHON:3.12",
  "PYTHON:3.11",
  "PYTHON:3.10",
  "PYTHON:3.9",
  "PYTHON:3.8",
```
Reference:
* https://learn.microsoft.com/en-us/azure/app-service/configure-language-python

2. Need "Azure Tools" extension pack
```

```

Reference:
* https://learn.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=fastapi%2Cwindows%2Cvscode-aztools%2Cazure-cli-deploy%2Cdeploy-instructions-azportal%2Cterminal-bash%2Cdeploy-instructions-zip-azcli

In the Azure Tools extension for VS Code:
1. Find the RESOURCES section and select your subscription.
2. Select + (Create Resource...)

![](https://learn.microsoft.com/en-us/azure/app-service/media/quickstart-python/create-app-service-visual-studio-code-2-240-px.png)

3. Python 3.13, Pricing B1

## Install azd
```powershell
winget search azd
winget install --id Microsoft.Azd
```
Restart the powershell terminal on windows to reload the PATH env variable.

## Login to tenant and sub
```powershell
azd auth login --tenant-id <TENANT_ID>
azd auth login --check-status
# show login sub
azd config show
```
You can find the tenant id from Azure Portal, MSFT Entra ID.

Reference:
* login tenant https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/reference#azd-auth-login
* config sub to use https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/azd-config#work-with-configuration-commands


```powershell
cd <project root path>/backend
# open vscode
code .

# add azd spport to the vs code proj root dir
azd env new dev

azd up
# select your sub for the right tenant
# select locaton East US 2

```

B1 monthly approx. 13 USD App Service Plan, 100 minutes/day 1vCPU, 1.75 GB Memory


## AZD environment variable
* https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/environment-variables-faq

## redeploy+
In the backend subfolder
1. stop, ctrl + c
2. azd deploy web


```console
PS C:\Users\yingdingwang\Documents\VCS\events\ai-hackathon-022025> azd deploy web

Deploying services (azd deploy)

  (✓) Done: Deploying service web
  - Endpoint: https://web-xxxxxxxxxxx.azurewebsites.net/


SUCCESS: Your application was deployed to Azure in 15 minutes 44 seconds.
You can view the resources created under the resource group rg-dev-app-svc-uno in Azure Portal:
https://portal.azure.com/xxxxxxx
```

## deploy python azure app service
* https://youtu.be/lwNzb5pRn08

auto deploy with app.py


used 
python3 app.py

in app service, settings, configuration, startup command


```
azd env list
azd env refresh

```