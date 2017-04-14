# LEASE WAVES TO THE WAVESGO POOL
# USES PYWAVES (WITH THANKS)
# ANY QUESTIONS: go@wavesgo.com
# www.wavesgo.com

#import libraries
import pywaves as pw
from decimal import *

#configure parameters
pw.setNode(node = 'http://node.wavesgo.com:6869', chain = 'mainnet')
minerAddress = pw.Address('3P2HNUd5VUPLMQkJmctTPEeeHumiPN2GkTb')

#ask for user private key
print("=-=-= WELCOME TO THE FANTASTIC, MAGNIFICENT, WAVESGO LEASING APP! =-=-=.\n") 
print("www.wavesgo.com\n\n") 
print("In order to lease, we need your Waves account private key.\n") 
print("You can get this from the Waves lite client, click on the backup icon (on the top right hand corner), copy your private key and paste it here.\n")
print("Oh, and don't worry - your private key is only used to sign the transaction locally, it won't be sent over the internet.\n\n")
while True:
	try:
		myKey = raw_input('Your private Key: ')
		myAddress = pw.Address(privateKey = myKey)
		if myKey:
			break
	except:
		print("\nThis key doesn't seem valid. Make sure you are entering your private key.\n")

#ask how much user wants to lease
while True:
	try:
		myAmount_raw=raw_input('How many Waves do you want to lease (minimum is 1 Wave): ')
		myAmount=int(Decimal(myAmount_raw)*Decimal(100000000))
		if myAmount:
			break
	except:
		print("\nThis amount if invalid!\n")
	


# lease Waves to miner Address and print response
try:
	leaseId = myAddress.lease(minerAddress, myAmount)
	if leaseId:
		print "\nCongratulations! You have leased ",myAmount_raw," waves"
		print "Transaction ID: ",leaseId
	else:
		print "Something went wrong... :-("
except:
	print "Something went wrong, sorry!"
