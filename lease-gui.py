#import libraries
import pywaves as pw
from decimal import *
from Tkinter import *
import ttk 
import tkMessageBox
import webbrowser

def callback(leaseId):
    webbrowser.open_new(r"http://www.wavesgo.com/transactions.html?"+leaseId)

def dolease(myKey,myAmount):
	msg=ttk.Label(mainframe, text="Broadcasting lease...")
	msg.grid(columnspan=5, row=8, sticky=W)
	msg.pack()
	try:
		myAddress = pw.Address(privateKey = myKey.get())
	except:
		tkMessageBox.showwarning("Private key incorrect","This key doesn't seem valid. Make sure you are entering your private key.")
		msg.pack_forget()
		return 
	
	try:
		myAmount_send=int(Decimal(myAmount.get())*Decimal(100000000))
		leaseId = myAddress.lease(minerAddress, myAmount_send)
		#tkMessageBox.showwarning("About to send...",myAmount_send)
		msg.pack_forget()
		if leaseId:
			tkMessageBox.showinfo("Yeah!","Lease successful")
			successmsg="TX ID: "+str(leaseId)
			ttk.Label(mainframe, text=successmsg).grid(columnspan=5, row=8, sticky=W)
			
			ttk.Button(mainframe, text="See transaction in WavesGo", command= lambda: callback(leaseId)).grid(columnspan=5, row=9, sticky=W)
			
		else:	
			tkMessageBox.showwarning("Uh oh","Something went wrong :(")
			msg.pack_forget()			
	except:
		tkMessageBox.showwarning("Uh oh","Something went very wrong :((")
		msg.pack_forget()
		return 



#configure parameters
pw.setNode(node = 'http://node.wavesgo.com:6869', chain = 'mainnet')
minerAddress = pw.Address('3P2HNUd5VUPLMQkJmctTPEeeHumiPN2GkTb')


#UI Stuff
root = Tk()
root.title("WavesGo Leasing")

mainframe = ttk.Frame(root, padding="8 8 32 32")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

myKey = StringVar()
myAmount = StringVar()
leaseId = StringVar()

myKey = ttk.Entry(mainframe, width=46,textvariable = myKey)
myKey.grid(column=2,columnspan=2,row=5, sticky=(W, E))

myAmount_entry = ttk.Entry(mainframe, width=7, textvariable=myAmount)
myAmount_entry.grid(column=2, row=6, sticky=(W, E))

ttk.Label(mainframe, text="You can find your private key in the lite client inside the backup icon").grid(columnspan=4, row=1, sticky=W)
ttk.Label(mainframe, text="Your Private Key").grid(column=1, row=5, sticky=W)
ttk.Label(mainframe, text="Amount to lease").grid(column=1, row=6, sticky=E)
ttk.Label(mainframe, text="Waves").grid(column=3, row=6, sticky=W)

ttk.Button(mainframe, text="Lease", command= lambda: dolease(myKey,myAmount)).grid(column=2, row=7, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

myKey.focus()
root.bind('<Return>', lambda:dolease(myKey,myAmount))

root.mainloop()
