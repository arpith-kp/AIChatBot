from slack.bot_runner import logger
from slackbot.bot import listen_to

from dataflow.train_model import response


@listen_to('helper_bot(.*$)')
def help(message, hl):
    logger.debug("------------ Received user message ------------ %s", hl)
    response_to_user = response(hl)
    logger.debug("------------ Sending response to user ------------ %s\n", response_to_user)
    message.send(response_to_user)

x = 1