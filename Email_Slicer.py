import pyautogui as pandey

email=pandey.prompt("Enter Your E-Mail").strip()
pos=email.find("@")
pandey.alert('Your Username Is "'+email[0:pos]+'" & Domain Is "'+email[pos+1:]+'"')