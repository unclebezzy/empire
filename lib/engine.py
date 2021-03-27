# Imports
import threading
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

class Engine(object):
    """ Central chat engine
    
    Methods:
        __init__() - Initialize the engine
        create_bot() - Create a new ChatterBot
    """
    
    def __init__(self):
        """ Initialize the engine
        
        Arguments:
            None
        """
        
        # Set default values
        self.bots = {}
        
    def create_bot(self, bot_name):
        """ Create a new ChatterBot
        
        Arguments:
            bot_name - string - The name of the new bot
        """
        
        # Create a new bot and a trainer for it
        bot = ChatBot(bot_name)
        trainer = ListTrainer(bot)
        
        # Append to self.bots
        self.bots[bot_name] = {
            "bot": bot,
            "trainer": trainer
        }
        
    def train_bot(self, bot_name, training_data):
        """ Train a chatbot
        
        Arguments:
            bot_name - string - The bot to train
            training_data - list - The data to train the bot with
        """
        
        # Train the bot
        self.bots[bot_name]["trainer"].train(training_data)
        
    def get_response(self, bot_name, input_data):