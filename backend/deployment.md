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

