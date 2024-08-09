import os
import json

path = os.path.dirname(os.path.realpath(__file__))

with open(f"{path}\\data.json", "r") as data:
    json_object = json.load(data)
    first_run = json_object["first_run"]

 
if first_run:
    with open(f"{path}\\data.json", "r+") as data:
            json_object = json.load(data)
            json_object["first_run"] = False
            data.seek(0)
            json.dump(json_object, data, indent=4)
            data.truncate()  
    if os.name == "nt":
        print("First run: Adding URI protocol to registry if running on ")

        import winreg

        location = winreg.HKEY_CURRENT_USER

        soft = winreg.OpenKeyEx(location, r"SOFTWARE\\Classes") 
        rootkey = winreg.CreateKey(soft, "drooler")

        winreg.SetValueEx(rootkey, "", 0, winreg.REG_SZ, "URL:drooler protocol") 
        winreg.SetValueEx(rootkey, "URL Protocol", 0, winreg.REG_SZ, "")

        if rootkey:
            winreg.CloseKey(rootkey)

        soft = winreg.OpenKeyEx(location, r"SOFTWARE\\Classes\\drooler") 
        shellkey = winreg.CreateKey(soft, "Shell")

        if shellkey:
            winreg.CloseKey(shellkey)

        soft = winreg.OpenKeyEx(location, r"SOFTWARE\\Classes\\drooler\\Shell") 
        openkey = winreg.CreateKey(soft, "Open")

        if openkey:
            winreg.CloseKey(openkey)

        soft = winreg.OpenKeyEx(location, r"SOFTWARE\\Classes\\drooler\\Shell\\Open") 
        commandkey = winreg.CreateKey(soft, "Command")

        winreg.SetValueEx(commandkey, "", 0, winreg.REG_SZ, f'"{path}\\drooler.bat"') 

        if commandkey:
            winreg.CloseKey(commandkey)

    else:
         print("First run: Not adding URI protocol as not running on Windows")
else:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print("Running")
    input()
