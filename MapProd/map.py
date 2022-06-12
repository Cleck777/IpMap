
import fileinput
import folium
import webbrowser
import subprocess
import requests
#cenimport tkinter



##import scapy.all as scapy

class Map:
    
    
    def __init__(self, center, zoom_start):
        self.center = center
        self.zoom_start = zoom_start
    
    def showMap(self):
        #Create the map
        #tiles ="Stamen Toner"
        my_map = folium.Map(location = self.center, zoom_start = self.zoom_start)
	
        folium.CircleMarker(
            location= self.center,
            radius=50,
            popup= site + " Server",
            color="#9E9E9E",
            fill=True,
            fill_color="#9E9E9E",
        ).add_to(my_map)

        #Display the map
        my_map.save("map.html")
       
        
        webbrowser.open_new_tab("DIRECTORY")

    """def getIP(addr):g
        command = ['dig', '+short', "brockport.edu"]
        p = subprocess.Popen(command, stdout=subprocess.PIPE)
        text = p.stdout.read()
        text = text.decode("utf-8") 
        text= text.replace('"\\"n', "")
        print(text)
        return text"""

        
    def getAddr(str):
    #ip = '123.42.02.244'
    
        response = requests.get("http://ip-api.com/json/"+str).json()

        if response["status"] == 'fail':
            print("ERROR: INVALID IP QUITTING")
            quit()
        #print(response)
        latlong = [response["lat"], response['lon'], response["query"], response["isp"] ]
        return latlong
    
    #Define coordinates of where we want to center our map
print("""
                 ..ooo@@@XXX%%%xx..
                .oo@@XXX%x%xxx..     ` .
                .o@XX%%xx..               ` .
            o@X%..                  ..ooooooo
            .@X%x.                 ..o@@^^   ^^@@o
        .ooo@@@@@@ooo..      ..o@@^          @X%
        o@@^^^     ^^^@@@ooo.oo@@^             %
        xzI    -*--      ^^^o^^        --*-     %
        @@@o     ooooooo^@@^o^@X^@oooooo     .X%x
        I@@@@@@@@@XX%%xx  ( o@o )X%x@@@@@@@@@@X%x
        I@@@@XX%%xx  oo@@@@X% @@X%x   ^^^@@@@@@@X%x
        @X%xx     o@@@@@@@X% @@XX%%x  )    ^^@X%x
        ^   xx o@@@@@@@@Xx  ^ @XX%%x    xxx
                o@@^^^ooo I^^ I^o ooo   .  x
                oo @^ IX      I   ^X  @^ oo
                IX     U  .        V     IX
                V     .           .     V                                 
""")
print("        ██▓ ██▓███      ███▄ ▄███▓ ▄▄▄       ██▓███  ")
print("        ▓██▒▓██░  ██▒   ▓██▒▀█▀ ██▒▒████▄    ▓██░  ██▒")
print("        ▒██▒▓██░ ██▓▒   ▓██    ▓██░▒██  ▀█▄  ▓██░ ██▓▒")
print("        ░██░▒██▄█▓▒ ▒   ▒██    ▒██ ░██▄▄▄▄██ ▒██▄█▓▒ ▒")
print("        ░██░▒██▒ ░  ░   ▒██▒   ░██▒ ▓█   ▓██▒▒██▒ ░  ░")
print("         ░▓  ▒▓▒░ ░  ░   ░ ▒░   ░  ░ ▒▒   ▓▒█░▒▓▒░ ░  ░")
print("          ▒ ░░▒ ░        ░  ░      ░  ▒   ▒▒ ░░▒ ░     ")
print("          ▒ ░░░          ░      ░     ░   ▒   ░░       ")
print("          ░                     ░         ░  ░         ")
print("          ░                     ░         ░  ░         ")
print()
prompt = "ADRR INPUT >> "

#for line in fileinput.input(files =('Ip.txt', 'r')):
 
    #ipaddre = "69.53.224"

print(prompt);
loc2 = input();
loc = Map.getAddr(loc2);
    

coords = [loc[0], loc[1]]
 ##print(loc[2], loc[3], loc[4])
map = Map(center = coords, zoom_start = 13)
    #enter = coords, zoom_start = 1
site = loc[3];

print(loc[3], " FOUND AT ", loc[2])

print("WOULD YOU LIKE TO SHOW THE MAP? [yes/no]")
answer = input();
if answer == "yes":
    map.showMap()
elif answer == "no":
    print("QUITTING")
    quit()
else:
    print("WRONG INPUT QUITTING")
    quit()
