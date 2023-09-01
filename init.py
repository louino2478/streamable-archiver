print("INIT START")
import shutil

#check if config file exists and copy default config file if not
if not os.path.exists("/config/config.json"):
    print("config file not found, creating it")
    shutil.copyfile("config.sample.json", "/config/config.json")

#check if DB file exists and create it if not
if not os.path.exists("/config/DB.txt"):
    print("DB file not found, creating it")
    f = open("/config/DB.txt","w")
    f.close()

#upgrade config file if needed
#add enabletelegram to config file if not present
print("checking config file...")
with open('/config/config.json', 'r') as f:
    config = json.load(f)
try:
    enabletelegram = config['enabletelegram']
    if enabletelegram == True or enabletelegram == False:
        print("config file OK")
except:
    print("config file is depressed, upgrading it")
    config['enabletelegram'] = True
    with open('/config/config.json', 'w') as f:
        json.dump(config, f, indent=4)



print("INIT END")