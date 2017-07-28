import serial, time

arduino = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(1) 

print "Iniciando..."
con = 1
arduino.flush()

while 1:
    if(con==1):
        dato_recibido=arduino.readline()
        time.sleep(1)
        print dato_recibido
        con=con+1
    time.sleep(1)
    if(con==2):
        var=str('enviando')
        arduino.write(var)
        time.sleep(2)


