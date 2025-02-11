# Single Agent Workflow

Building a single agent workflow with Promptflow, the endpoint can later be used in Copilot Studio.

In the Chat playground
- use promptflow to create a single agent workflow deployment

1. In Model Playground GPT-4o:
* Click on `PromptFlow` 
to generate a promptflow template.
![](imgs/generate_promptflow_playground.png)
* Enter name: `report search`



2. In the PromptFlow View:
* Click on `Start Compute Session`
![](imgs/testing_prompt_flow_run.png)

3. Update the library
* Open requirements.txt, edit with the following:
```txt
langdetect==1.0.9
promptflow-vectordb[azure]==0.2.16
promptflow==1.17.2
azureml-rag==0.2.38
```
* Save and install
![](imgs/update_and_install_promptflow_lib_search_agent.png)


3. Test Singe Agent workflow with `chat`:
![](imgs/test_chat_promptflow.png)

4. Deploy Single Agent workflow with `Deploy`:
* Click on `Deploy`
* Endpoint name: `ai-search-demo-<your name>-no`
* Virtual machine: `Standard_D2as_v4`
![](imgs/deploy_search_single_agent_promptflow.png)
* Review + Create
* Create




Reference:
* reate a generative AI app that uses your own data https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/04-Use-own-data.html