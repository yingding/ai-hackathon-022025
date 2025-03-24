# Copilot Studio

## Create your agent in copilot studio

Call the browser in InPrivate mode and type the [[Copilot Studio]](https://copilotstudio.preview.microsoft.com)
Use the user credentials assigned to you to sign into the demo tenant. Set-Up the MFA if needed.
When you set up the MFA you can create a new user profile in browser so that you can log in again without having to enter the credentials.

In Copilot Studio, you can create a new agent by description. Assure that you have selected your own personal developer environment.

 ![](main/imgs_mcs/pic1.jpg)

 You can continue in the dialogue and enter decriptions or user "Skip to configure" button to use the configureation pane directly.
 Upon finishing, press "Create" to create your agent.
 
 ![](main/img_mcs/skip_to_configure.png)

 ![](main/imgs_mcs/create_agent.png)

After your agent is created, enable GenAI orchestration and disable the feature "Allow the AI to use its own general knowledge."

![](main/imgs_mcs/GenAI_Setting.png)

## Add an action to your agent

### Create a custom connector 
For your agent to connect to Azure Foundry endpoints, you need to create a custom connector.

Go to [[Power Automate]](https://make.preview.powerautomate.com)
You will have to switch on some menu points on the left side

![](main/imgs_mcs/PAmenu.png)

Choose "Discover all" and turn on the "Connections", "Connectors" and  "Custom Connectors"

![](main/imgs_mcs/PA_discover_pin.png)

Go to the menu point "custom connectors" and create a new one from blank. Enter a name "AI Joke Connector" or whatever you like.

 ![](main/imgs_mcs/PA_customcon.png)

After you did this, hit "Create connector"
 ![](main/imgs_mcs/PA_customcon_create1.png)

 Switch the button "Swagger editor" on and copy the swagger file into the editor.
 ![](main/imgs_mcs/PA_customcon_swagger.png)

 Here is the file:
 [swagger template](main/imgs_mcs/custom_connector_swagger_file_1.txt)
 
