## Agent in Azure AI Foundry

## What is an AI Agent?

Within Azure AI Foundry, an AI Agent acts as a "smart" microservice that can be used to answer questions (RAG), perform actions, or completely automate workflows. It achieves this by combining the power of generative AI models with tools that allow it to access and interact with real-world data sources
[[AI Agent Definition]](https://learn.microsoft.com/en-us/azure/ai-services/agents/overview#what-is-an-ai-agent).

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












## Reference

* AI Foundry Agents Overview: https://learn.microsoft.com/en-us/azure/ai-services/agents/overview
* AI Foundry Quickstart with AI Foundry from Azure Portal UI https://learn.microsoft.com/en-us/azure/ai-services/agents/quickstart?pivots=ai-foundry
*RBAC role for Azure AI Foundry portal https://learn.microsoft.com/en-us/azure/ai-studio/concepts/rbac-ai-studio

## Blogs
* DeepSeek R1 available on Azure AI Foundry and Github https://techcommunity.microsoft.com/discussions/marketplace-forum/deepseek-r1---now-available-on-azure-ai-foundry-and-github/4372176



