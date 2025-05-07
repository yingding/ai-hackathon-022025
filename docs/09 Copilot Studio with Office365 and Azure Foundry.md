# Copilot Studio with Office365 and Azure Foundry

## Option 1 - agent connecting to Outlook Calendar
This Agent will connect to user calendar or mailbox and call previously created connector with the information from the calendar event. You can also create a new agent.

You can use your previously created Joke telling agent.

Just go to the agent and add another action.

![alt text](main/imgs_mcs/cs_calendar1.png)

Add a `Get calendars (V2)` action. This action will get the calendar ID of the user.

![alt text](main/imgs_mcs/cs_calenddar2.png)

Confirm the connection or create a new one to Outlook and klick `Next`.

![alt text](main/imgs_mcs/cs_calendars3.png)

Enter descriptions and confirm with `Add action`. You don't need to fill out any other parameters.

![](main/imgs_mcs/cs_calendar4.png)

Reapeat the same procedure for the action `Get calendar view of events (V3)`

![alt text](main/imgs_mcs/cs_calendar5.png)

Now your actions will look something like this:

![](main/imgs_mcs/cs_calendar6.png)

That is all the configuration you have to do.

Create an event in your calendar with title `Elephants`

Go to the agent test pane and type the following prompt: `Tell me a joke from Deepseek about the event from my calendar today and use the title as topic for the joke.` 

The orchestrator will call all 3 actions in the right order to get the calendar, than the events title and finally call the endpoint.

![alt text](main/imgs_mcs/cs_calendar7.png)

![alt text](main/imgs_mcs/cs_calendar8.png)