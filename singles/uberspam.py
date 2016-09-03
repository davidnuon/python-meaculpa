import Skype4Py 

skype = Skype4Py.Skype() 
skype.Attach() 

for n in range(90) :
    skype.CreateChatWith('westly.ward').SendMessage('grrrrr') 