# Deploy a Multi-Agent Semantic Kernel API Backend with Azure App Service

## Preparation on your local windows computer
1. Install a Python environment with Python 3.13 Version
2. Install VSCode
3. Install AZD tool on Windows

```powershell
winget search azd
winget install --id Microsoft.Azd
```
Restart the powershell terminal on windows to reload the PATH env variable.

4. Install git tool on Windows
```powershell
winget search git
winget install --id Microsoft.Git
```
Restart the powershell terminal on windows to reload the PATH env variable.

## Login to Tenant and Sub

```powershell
azd auth login --tenant-id <TENANT_ID>
azd auth login --check-status
# show login sub
azd config show
```
Note:
* You can find the **tenant id** from Azure Portal, MSFT Entra ID.

Reference:
* login tenant https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/reference#azd-auth-login
* config sub to use https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/azd-config#work-with-configuration-commands

## Clone Repository 
```powershell
cd <PATH of your choice>
git clone https://github.com/yingding/ai-hackathon-022025
```

## Open the code template
```powershell
cd <PATH of your choice>/ai-hackathon-022025

code .
```
This will automatical open VSCode editor

## Modify your env file
1. Copy the `<project root>/backend/app/.env.example` file to `<project root>/backend/app/.env` file

2. Fill out the `.env` file with your credential

```
AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="gpt-4o-2024-11-20"
AOAI_DEPLOYMENT_API_VERSION="2024-10-21"
AZURE_OPENAI_API_KEY="<your inference key for the gpt model>"
KEY_TOKEN="<your api bear token>" # must be longer than 7 tokens

# AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME="text-embedding-ada-002"
# AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

## Deploy
Run the following commands from a PowerShell on your local dev windows computer.

```powershell
# important to go to the sub dir "backend"
cd <project root path>/backend

# add azd support to the vs code proj root dir
azd env new dev

azd up
# select your sub for the right tenant
# select locaton East US 2
```

Then you will see the output from your powershell
```console
PS C:\Users\yingdingwang\Documents\VCS\events\ai-hackathon-022025> azd deploy web

Deploying services (azd deploy)

  (✓) Done: Deploying service web
  - Endpoint: https://web-xxxxxxxxxxx.azurewebsites.net/


SUCCESS: Your application was deployed to Azure in 15 minutes 44 seconds.
You can view the resources created under the resource group rg-dev-app-svc-uno in Azure Portal:
https://portal.azure.com/xxxxxxx
```

## Testing out the endpoint API
Testing the swagger api from:
```
https://web-xxxxxxxxxxx.azurewebsites.net/docs/
```
* Authenticate with your `KEY_TOKE` from the `.env` file

**Single Agent**:

Using the swagger UI for single agent API endpoint:
```json
{
  "message": "What are some innovative approaches to reduce plastic waste in urban environments?",
  "system_prompt": "You are a helpful assistant that provides concise and accurate information.",
  "temperature": 0.7,
  "available_plugins": [],
  "chat_history": []
}
```

**Multi Agent**:

Using the swagger UI for multi-agent API endpoint:
```json
{
  "message": "What are some innovative approaches to reduce plastic waste in urban environments?",
  "system_prompt": "You are a helpful assistant that provides concise and accurate information.",
  "temperature": 0.7,
  "available_plugins": [],
  "chat_history": [],
  "agent_configs": [],
  "max_iterations": 4
}
```

## Trouble shoot
### 1. Redeploy
In the backend subfolder
1. stop, ctrl + c
2. azd deploy web