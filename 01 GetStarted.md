# Get started with Azure AI Foundry

@author: Yingding Wang\
@date: 10.02.2025\
@revision: 1

## Quickstart guide

In your Azure subscription:
1. Create an Azure AI Foundry hub
2. Create an Agent project

### Start AI Foundry from Azure Portal UI

Prerequisites
* An Azure subscription
* Your Azure Portal User have "Azure AI Developer" assigned

#### 1 Create a resource groups
* resource groups in the Azure portal search
* create
* "rg-ai-sandbox-<yourname>-uno"
* Region: East US
* Review + Create
* Create

#### 2 Create a AI Hub in Azure AI Foundry
Hub: Grouping container for projects. Provides security, connectivity, and compute management.

To create a Hub in Azure AI Foundry, follow these steps:

1. Go to Azure AI Foundry

2. Select + "Create v" -> Hub.

3. select resource group `rg-ai-sandbox-<yourname>-uno`

4. select Create new hub, 
    * Resource group: `rg-ai-sandbox-<yourname>-uno`
    * region: East US 2
    * Name: `ai-hub-demo-<yourname>-uno`
    * Connect AI Service -> Create new -> `aihubdemo<yourname>uno` -> save
    * next storage
    * storage -> Create new -> `aihubdemo<yourname>uno` -> LRS -> save
    * key valut -> Create new -> `aihubdemo<yourname>uno`
    -> review + create

**The following Azure resource will be created**:
|Resource | Type |
|:---| :---|
|ai-hub-demo-yingding-uno|Microsoft.MachineLearningServices/workspaces|
|aihubdemoywuno|Microsoft.CognitiveServices/accounts|
|aihubdemoywuno|Key vault|
|aihubdemoywuno|Storage account|

#### 3 Create a AI Project in Azure AI Foundry
Project: Collaborate, organize, and track work to build AI apps.

To create a Project in Azure AI Foundry, follow these steps:

1. Go to Azure AI Foundry

2. Select + "Create v" -> Project.

3. select resource group `rg-ai-sandbox-<yourname>-uno`, Enter a name for the project `ai-proj-demo-<yourname>-uno` 

4. select hub: `ai-hub-demo-<yourname>-uno`

5. review + create


**The following Azure resource will be created**:
|Resource | Type |
|:---| :---|
|ai-proj-demo-yw-uno|Microsoft.MachineLearningServices/workspaces|


#### 4 Go to the Azure AI Foundry Project
* In Azure portal, goto the Azure AI Foundry Project `ai-proj-demo-<yourname>-uno`  
* Overview
* Launch Studio

1. From your project overview, select Agents, located under Build and customize.

2. Select your Azure OpenAI service resource `aihubdemo<yourname>uno_aoai` -> click on `Let'S go`
![](imgs/agent_aoai_svc_resource.png)

3. Select a model deployment for the Agent to use.

4. Goto model catalog, search "DeepSeek"
![](imgs/model_catalog_deep_seek.png)

5. Click on "DeepSeek R1"
    * Deploy
    * Agree and Procceed
  ![](imgs/deepseek_deploy_1.png)

    * Customize 
    ![](imgs/deepseek_deploy_2.png)

    * Content filter: DefaultV2
    ![](imgs/deepseek_deploy_3.png)
    * Deploy


6. Play with "Deep Seek R1" via Playground

    * Models + endpints
    * DeepSeek R1
    * Open in playground
    ![](imgs/playground_deepseek_1.png)
   
    * chat with DeepSeek R1 
    * Type in the query "hi, who are you?"
    ![](imgs/playground_deepseek_2.png)
   

## (Optional) Update identity-based storage account access

Should you encounter the issue that you can not access the storage account for  the Azure AI Foundry Project. Please double check if the `storage account key accesss` of your AI hub storage account (`aihubdemo<your name>uno`) is deactivated by default.

1. double check whether the storage account's key access is deactivated
* Open your AI hub storage account through Azure Portal
* Open `Configuration` tab under `Settings` menu
* double check whether `Allow storage account key access` is disabled.



## can not access the promptflow

1. AI hub
Settings -> Properties -> Storage account access -> identity-based -> save

2. Disable shared key on storage account
storage account for AI Hub
* Settings - Configuration -> Allow storage account key access (disabled)
* IAM -> Add role assignment
* Choose the roles: 
-> Storage Blob Data Contributor
-> Storage File Data Privileged Contributor
to your current user.

Now you shall have access to the promptflow.

Assign user with
Storage Blob Data Contributor and Storage File Data Privileged Contributor roles

```
Important: When using identity-based authentication, "Storage Blob Data Contributor" and "Storage File Privileged Contributor" roles must be granted to individual users that need access on the storage account
```

Reason: The Storage access key has been disabled on the Storage account.
if your company has a policy to disable it, you will need to find another way.

Refer to this page for information on how to change the access to using Entra ID:

https://learn.microsoft.com/en-gb/azure/ai-studio/how-to/disable-local-auth?tabs=portal#update-an-existing-hub


* https://learn.microsoft.com/en-us/answers/questions/2114208/authentication-failed-when-creating-prompt-flow


## Reference

* AI Foundry Agents Overview: https://learn.microsoft.com/en-us/azure/ai-services/agents/overview
* AI Foundry Quickstart with AI Foundry from Azure Portal UI https://learn.microsoft.com/en-us/azure/ai-services/agents/quickstart?pivots=ai-foundry
*RBAC role for Azure AI Foundry portal https://learn.microsoft.com/en-us/azure/ai-studio/concepts/rbac-ai-studio

## Blogs
* DeepSeek R1 available on Azure AI Foundry and Github https://techcommunity.microsoft.com/discussions/marketplace-forum/deepseek-r1---now-available-on-azure-ai-foundry-and-github/4372176



