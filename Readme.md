[![Gif](https://github.com/arpith-kp/BotUsageDemo/blob/master/BotUsa.gif)]

Simple demo on how to use chatbot for IT helpdesk service using machine learning.

--------------------------------------------------------------------------------
Some features of this bot 
* Bot can understand and use contextual information throughout conversations will interact in a way that’s easier, quicker, and more naturally helpful for people
* NLP engine can also detect the sentiment of an interaction to help steer the flow of the conversation
* Store conversation in memory which can then be is used to do Supervised or Unsupervised learning

--------------------------------------------------------------------------------
* On the right is Slack bot, on the left you see data used to generate response and in bottom you can log message when the bot runs.
--------------------------------------------------------------------------------

- To start demo, let's see how it responds to greetings 

    - helper_bot How are you.

- To show how bot uses it's previous knowledge(Unsupervised Learning) when new request received 

	- helper_bot What time are you open until (This is new input that bot have never seen)

- To show how bot preseves Context when you having conversation just like with human

    - helper_bot How many rooms are available
    - helper_bot ok book one today please(Here Context is about Conference rooms)

- To show how bot uses sentiment analysis to determine whether a piece of writing is positive, negative or neutral and use that with conversation flow
	- helper_bot Sweet


