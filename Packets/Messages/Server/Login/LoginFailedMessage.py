from Utils.Writer import Writer
from Utils.Fingerprint import Fingerprint


class LoginFailedMessage(Writer):

    def __init__(self, client, player, msg):
        super().__init__(client)
        self.id = 20103
        self.player = player
        self.msg = msg

    def encode(self):
        self.writeInt(self.player.err_code) # error code
        self.writeString(Fingerprint.loadFinger_full("GameAssets/fingerprint.json")) # fingerprint
        
        self.writeString() # server hostname
        self.writeString(self.player.patchUrl) # patch hostname
        self.writeString(self.player.updateUrl) # update hostname
        self.writeString(self.msg) # message

        self.writeHexa('''00 00 00 00 00 FF FF FF FF 00 00 00 02''') # unknown

        self.writeString(self.player.patchUrl) # patch hostname
        self.writeString() # rackcdn hostname

        self.writeInt(0)
        self.writeInt(0) # time left ?

        self.writeString() # null
        self.writeString() # null

        self.writeHexa('''02 00 00 00 00 00 00 00 00 00''') # unknown



        # Error code list

        # 1  = Custom Message
        # 7  = Patch
        # 8  = Update Available
        # 9  = Failed to Connect
        # 10 = Maintenance
        # 11 = Banned
        # 13 = Acc Locked PopUp
        # 16 = Updating bs/Maintenance
        # 18 = Chinese Text?