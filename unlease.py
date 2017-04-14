# UN-LEASE WAVES
# USES PYWAVES (WITH THANKS)
# ANY QUESTIONS: go@wavesgo.com
# www.wavesgo.com

#import libraries
import pywaves as pw

#configure parameters
pw.setNode(node = 'http://node.wavesgo.com:6869', chain = 'mainnet')

#ask for user private key
print("=-=-= WELCOME TO THE FANTASTIC, MAGNIFICENT, WAVESGO UNLEASING APP! =-=-=.\n") 
print("www.wavesgo.com\n\n") 
print("To cancel a lease we will need your lease transaction ID and your private key.\n") 
print("You can get your private key from the Waves lite client, click on the backup icon (on the top right hand corner), copy your private key and paste it here.\n")
print("You can get your lease transaction ID from wavesgo.com.\n\n")
while True:
	try:
		myKey = raw_input('Your private Key: ')
		myAddress = pw.Address(privateKey = myKey)
		if myKey:
			break
	except:
		print("\nThis key doesn't seem valid. Make sure you are entering your private key.\n")

#ask for transaction ID
while True:
	try:
		myTX_raw=raw_input('Please enter the lease transaction ID: ')		
		if myTX_raw:
			break
	except:
		print("\nThis transaction ID is invalid!\n")
	


# un-lease Waves to miner Address and print response
try:
	myAddress.leaseCancel(myTX_raw)
	print "Lease cancelled "
except Exception, e:
	print "Something went wrong, sorry!\n\n"+str(e)
