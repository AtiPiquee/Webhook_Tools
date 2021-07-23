# importation de tout les modules utilisés et des fonction de modules 

import requests, os, platform, time, json
from dhooks import Webhook, Embed, File
from colorama import Fore, init


init() # initialise colorama 

# fonction de clear de la console selon l'os 

def clear():
	if platform.system() == "Windows":
		os.system("cls")
	elif platform.system() == "Linux":
		os.system("clear")

# fonction qui demande le webhook au début du programme 

def webhook():
	clear()
	global webhook_link
	webhook_link = input(Fore.GREEN + "\nEnter the webhook link $: ")
	clear()
	
# fonction de départ contenant le titre et le choix a faire 

def start():
	clear()
	current_webhook()
	print(Fore.YELLOW + """
                __    __                __      __              __    
 _      _____  / /_  / /_  ____  ____  / /__   / /_____  ____  / /____
| | /| / / _ \/ __ \/ __ \/ __ \/ __ \/ //_/  / __/ __ \/ __ \/ / ___/
| |/ |/ /  __/ /_/ / / / / /_/ / /_/ / ,<    / /_/ /_/ / /_/ / (__  )
|__/|__/\___/_.___/_/ /_/\____/\____/_/|_|   \__/\____/\____/_/____/ 
                                                                      

		""")
	print(Fore.LIGHTRED_EX + """[1] Message		[2] Embed\n\n[3] Spam Message	[4] Get Webhook Infos\n\n[5] Send files	        [6] Modify the webhook\n\n[7] Change webhook	[8] Nuke\n\n[9] Credits\n """)
	global choice 
	choice = int(input(Fore.RED + "           		$: "))
	global webhook_link

webhook() # appel de la fonction webhook()
os.system("title Webhook Tools") # change le nom de la fenêtre pour "Webhook Tools"

# fonction principale relative au différents choix possibles 

def main():
	start()
	if choice == 1:
		Message()
	elif choice == 2:
		Embed()
	elif choice == 3:
		Spam()
	elif choice == 4:
		Infos()
	elif choice == 5:
		Files_Sending()
	elif choice == 6:
		Webhook_Modification()
	elif choice == 7:
		Change_Webhook()
	elif choice == 8:
		Nuke()
	elif choice == 9:
		Credits()
	elif choice != [1,2,3,4,5,6,7,8,9]:
		print(Fore.RED + "Error !")
		input("")
		main()
	

# fonction affichant le lien du webhook en utilisation et son nom

def current_webhook():
	r = requests.get(webhook_link).json()
	print(Fore.LIGHTRED_EX + "Current Webhook : " + webhook_link + "\n" + Fore.YELLOW + "name : " + r['name'] + "\n")


# fonction pour envoyer un message 

def Message():
	clear()
	current_webhook()
	hook = Webhook(webhook_link)
	message = input(Fore.LIGHTYELLOW_EX + "Your message : ")
	hook.send(message)
	print(Fore.LIGHTGREEN_EX + "\nYour message has been sended !")
	input("")
	clear()
	main()

# fonction permetant de spam un message 

def Spam():
	clear()
	current_webhook()
	hook = Webhook(webhook_link)
	message = input(Fore.LIGHTYELLOW_EX + "Enter the message that you want to spam : ")
	messages_number = int(input("Enter the number of messages to spam : "))
	sended_message = 0
	for i in range(messages_number):
		hook.send(message)
		sended_message += 1
		print("\n" + Fore.WHITE + "[", Fore.RED + time.strftime('%H:%M:%S', time.localtime()) + Fore.WHITE, "]" + Fore.LIGHTYELLOW_EX, str(sended_message) + " messages sended !")

	print(Fore.GREEN + "\nAll of the messages has been sended !")
	input("")
	main()

# fonction pour envoyer un embed

def Embed_Sending():
	clear()
	current_webhook()
	global hook
	hook = Webhook(webhook_link)

	embed = Embed(
		description=input("Description : "),
    	color=input("Color (in HEX) : "),
    	timestamp='now'  # sets the timestamp to current time
    	)

	image1 = input("Enter the direct first image link : ")
	image2 = input("Enter the direct second image link : ")


	embed.set_author(name=input("Author name : "), icon_url=image1)
	embed.add_field(name=input("First field title : "), value=input("First field text : "))
	embed.add_field(name=input("Second field title : "), value=input("Second field text : "))
	embed.set_footer(text=input("Footer text : "), icon_url=image1)

	embed.set_thumbnail(image1)
	embed.set_image(image2)

	hook.send(embed=embed)

	print("embed sended !")
	input("")
	main()

# fonction d'affichage des infos du webhook

def Infos():
	clear()
	current_webhook()
	r = requests.get(webhook_link).text
	r = json.loads(r)
	print(Fore.YELLOW + "Id : " + Fore.LIGHTYELLOW_EX + r['id'])
	print(Fore.YELLOW + "Name : " + Fore.LIGHTYELLOW_EX + r['name'])
	print(Fore.YELLOW + "Avatar : " + Fore.LIGHTYELLOW_EX + str(r['avatar']))
	print(Fore.YELLOW + "Channel ID : " + Fore.LIGHTYELLOW_EX + r['channel_id'])
	print(Fore.YELLOW + "Guild ID : " + Fore.LIGHTYELLOW_EX + r['guild_id'])
	print(Fore.YELLOW + "Application ID : " + Fore.LIGHTYELLOW_EX + str(r['application_id']))
	print(Fore.YELLOW + "Token : " + Fore.LIGHTYELLOW_EX + r['token'])
	input("")
	main()

# fonction d'envoi de fichier par un webhook

def Files_Sending():
	clear()
	current_webhook()
	hook = Webhook(webhook_link)
	
	file = File(input(Fore.LIGHTYELLOW_EX + "File path : "), name=input("File name (if you don't want change file name press enter, if you want change the name precise the extention) : "))
	hook.send(input("Message (if you don't want send message press enter): "), file=file)
	print(Fore.GREEN + "\nyour file has been sended !")
	input("")
	main()

# fonction de modification du nom et de l'avatar du webhook

def Webhook_Modification():
	clear()
	current_webhook()
	hook = Webhook(webhook_link)

	with open(input(Fore.LIGHTYELLOW_EX + "Avatar | Image path :"), 'rb') as f:
		img = f.read() 
	
	hook.modify(name=input("Name | Enter the new name : "), avatar=img)
	print(Fore.GREEN + "\nWebhook succesfuly modifyed !")
	input("")
	main()

# fonction permettant de changer de webhook

def Change_Webhook():
	clear()
	current_webhook()
	global webhook_link
	webhook_link = input(Fore.GREEN + "\nEnter the new webhook link $: ")
	print("\n Webhook succesfuly changed !")
	input("")
	clear()
	main()

# fonction de suppression du webhook

def Nuke():
	clear()
	current_webhook()
	hook = Webhook(webhook_link)
	r = requests.get(webhook_link).json()

	choice = input(Fore.RED + "Are you sure you really want to delete the webhook ? [Y/N] : ")

	if choice == "Y":
		print(Fore.LIGHTRED_EX + "The webhook " + r['name'] + " will be deleted.")
		input("")
		hook.delete()
		print(Fore.GREEN + "The webhook is successfuly deleted !")
	elif choice == "y":
		print(Fore.LIGHTRED_EX + "The webhook " + r['name'] + " will be deleted.")
		input("")
		hook.delete()
		print(Fore.GREEN + "The webhook is successfuly deleted !")
	elif choice == "N":
		print(Fore.LIGHTGREEN_EX + "The webhook will not be deleted")
	elif choice == "n":
		print(Fore.LIGHTGREEN_EX + "The webhook will not be deleted")

# fonction qui affiche les crédits du tool

def Credits():
	clear()
	print(Fore.YELLOW + "Credits :\n")
	print(Fore.LIGHTBLUE_EX + "Dev by : " + Fore.LIGHTYELLOW_EX + "AtiPique_#1900")
	print(Fore.LIGHTBLUE_EX + "\nThanks for the help from : " + Fore.LIGHTYELLOW_EX + "GuyEdit#0990")
	input("")
	main()

# fonction de lancement du programme

if __name__ == "__main__":
	main()



