# Copilot Studio Connecting to Azure AI Search

This Agent will provide user with answers to the questions grounded in documents that are stored in the Blob storage and indexed via Azure AI Search. AI Search assets have been created in part 02.

AI Search in Copilot Studio will work only if the index is vectorized. Therefore check it first and vectorize if necessary. 

![alt text](main/imgs_mcs/cs_vectorize_index.png)

![alt text](main/imgs_mcs/cs_vectorize_index2.png)

Create your agent in Copilot Studio as already done in previous exercise.

Enter the description and activate GenAI orchestration. Remove the flag `Allow the AI to use its own general knowledge`.

Add knowledge source to your agent and choose the AI Search.

![alt text](main/imgs_mcs/cs_add_azureAIsearch.png)

Choose `Create new connection` and enter the credentials to your AI Search ressource.

![alt text](main/imgs_mcs/CS_azureAIsearch_newconn.png)

Enter your AI Search credentials: 

![](main/imgs_mcs/CS_azureAIsearch_cred1.png)

![alt text](main/imgs_mcs/CS_azureAIsearch_cred2.png)

Enter a description for the knowledge source and check the indices.

![alt text](main/imgs_mcs/CS_azureAIsearch_descr.png)

If the inidex is vectorized, than it will work fine. If not - datasource will not be found. Choose the vectorized one.

![alt text](main/imgs_mcs/CS_azureAIsearch_index.png)

Save and finish. Now your agent is ready to be tested. Nothing more must be done as it looks for relevant answers in the AI Search.

![](main/imgs_mcs/CS_azureAIsearch_testpane.png)

Publish your agent to Teams or M365 Copilot if wanted.

