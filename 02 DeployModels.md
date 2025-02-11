# Deploy models in Azure AI Foundry
## Deploy "text-embedding-ada-002" for AI Search

1. Login to the Azure AI Foundry portal https://ai.azure.com

2. In your project, in the navigation pane on the left, under `My assets`, select the `Models + endpoints` page.

3. Create a new deployment of the `text-embedding-ada-002` model with the following settings by selecting Customize in the `Deploy model` dropdown `Deploy base model` wizard:

* Deployment name: `text-embedding-ada-002`
* Deployment type: Standard
* Customize
    * Model version: Select the default version
    * Connected AI resource: Select the resource created previously `aihubdemo<yourname>uno_aoai`
    * Tokens per Minute Rate Limit (thousands): 40K
    * Content filter: DefaultV2
    * Enable dynamic quota: Disabled
* Deploy


![](imgs/deploy_text_embedding_model_1.png)

Reference:
* https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/04-Use-own-data.html
