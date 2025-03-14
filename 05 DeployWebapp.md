# (TODO)Deploy Webapp from Chat playground

TODO: write

1. create resource groups in US East2
2. create storage account, blob storage, container
3. Upload the file
4. connect the blobstorage over key with AI foundry storage data
5. Create Azure AI Search resource
6. Index from AI foundry storage data with Azure AI Search resource 

## registering the Microsoft.Web and Microsoft.OperationalInsights provider for your subscription
Microsoft.Web provider is required for services like App Services, Web Apps, Functions, and other related services.

1.	Login to Azure Portal

2.	Navigate to Subscriptions

3.	In Settings, Resource Providers	of your subscription

4.	Search for Microsoft.Web, Microsoft.OperationalInsights

5.	Select, click on the elipse and Register the Provider

6.	Verify Registration	Refresh the page and ensure that the status of Microsoft.Web is now "Registered".

## Web App
1. Settings -> Authenticaton 
2. Add identity provider

https://learn.microsoft.com/en-us/azure/ai-studio/tutorials/deploy-chat-web-app#configure-web-app-authentication

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
* Deploy enterpise webapp: https://learn.microsoft.com/en-us/azure/ai-studio/tutorials/deploy-chat-web-app
* Azure AI Search with Azure AI Foundry https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/04-Use-own-data.html
* Follow this link to add Microsoft Privider (You shall link your Microsoft User first) https://learn.microsoft.com/en-us/azure/app-service/scenario-secure-app-authentication-app-service?tabs=workforce-configuration#3-configure-authentication-and-authorization


## Issue
* Please verify that Microsoft.web provider is registered for the selected subscription.

