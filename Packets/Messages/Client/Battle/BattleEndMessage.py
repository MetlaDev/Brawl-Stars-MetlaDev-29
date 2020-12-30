from Packets.Messages.Server.Battle.BattleResultMessage import BattleResultMessage
from Packets.Messages.Server.Battle.BattleResult2Message import BattleResult2Message

from Utils.Reader import BSMessageReader


class BattleEndMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.BattleResult = self.read_Vint()
        self.read_Vint()
        self.player.Rank = self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()

        self.player.Team = self.read_Vint() #red or blue

        self.read_Vint()
        
        self.read_string() #Your Name

        self.read_Vint()
        self.Bot1 = self.read_Vint() #bot brawler
        self.read_Vint()
        self.read_Vint() #red or blue
        self.read_Vint()

        self.Bot1N = self.read_string()

        self.read_Vint()
        self.Bot2 = self.read_Vint() #bot brawler
        self.read_Vint()
        self.read_Vint() #red or blue
        self.read_Vint()

        self.Bot2N = self.read_string()

        self.read_Vint()
        self.Bot3 = self.read_Vint() #bot brawler
        self.read_Vint()
        self.read_Vint() #red or blue
        self.read_Vint()

        self.Bot3N = self.read_string()

        self.read_Vint()
        self.Bot4 = self.read_Vint() #bot brawler
        self.read_Vint()
        self.read_Vint() #red or blue
        self.read_Vint()

        self.Bot4N = self.read_string()

        self.read_Vint()
        self.Bot5 = self.read_Vint() #bot brawler
        self.read_Vint()
        self.read_Vint() #red or blue
        self.read_Vint()

        self.Bot5N = self.read_string()

    def process(self):
    	if self.player.Rank != 0:
    		BattleResultMessage(self.client, self.player).send()
    	else:
    		if self.player.Team == 0:
    			self.player.Bot1N = self.Bot1N
    			self.player.Bot2N = self.Bot2N
    			self.player.Bot3N = self.Bot3N
    			self.player.Bot4N = self.Bot4N
    			self.player.Bot5N = self.Bot5N

    			self.player.Bot1 = self.Bot1
    			self.player.Bot2 = self.Bot2
    			self.player.Bot3 = self.Bot3
    			self.player.Bot4 = self.Bot4
    			self.player.Bot5 = self.Bot5

    			BattleResult2Message(self.client, self.player).send()
    		else:
    			self.player.Bot1N = self.Bot4N
    			self.player.Bot2N = self.Bot5N
    			self.player.Bot3N = self.Bot3N
    			self.player.Bot4N = self.Bot1N
    			self.player.Bot5N = self.Bot2N
                
    			self.player.Bot1 = self.Bot4
    			self.player.Bot2 = self.Bot5
    			self.player.Bot3 = self.Bot3
    			self.player.Bot4 = self.Bot1
    			self.player.Bot5 = self.Bot2
    			BattleResult2Message(self.client, self.player).send()
