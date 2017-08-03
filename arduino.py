import serial, time, urllib2, json
from threading import Thread

def getCoinStats(coin):
    global data
    stats = json.load(urllib2.urlopen("https://api.coinmarketcap.com/v1/ticker/"+coin+"/?convert=USD"))
    price_usd = round(float(stats[0]['price_usd']), 2)
    perc_change = stats[0]['percent_change_24h']
    data = [price_usd,perc_change]

def updateStats(coin):
    while 1:
        getCoinStats(coin)
        time.sleep(180)

con = 1
data = []
display = "price"

arduino = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(1) 

print "Initializing..."
arduino.flush()

eth_refresh = Thread(target=updateStats, args=("ethereum",))
eth_refresh.daemon = True
eth_refresh.start()

while 1:
    if(con==1):
        dato_recibido=arduino.readline()
        time.sleep(1)
        print dato_recibido
        con=con+1
    time.sleep(1)
    if(con==2):
        if(display=="price"):
            var=str('Price: $') + str(data[0])
            display = "perc"
        else:
            var=str('Change: ') + str(data[1]) + str('%')
            display = "price"
        arduino.write(var)
        time.sleep(3)


