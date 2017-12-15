import wave
import math
import binascii

NomFichier = 'la440.wav'
leSon = wave.open(NomFichier,'w') # instanciation de l'objet leSon

frequenceGauche = int(input("Choisissez la fréquence gauche ?"))
frequenceDroite = int(input("Choisissez la fréquence droite ?"))

nbCanal = 2   # stereo
nbOctet = 1    # taille d'un echantillon : 1 octet = 8 bits
fech = 44100   # frequence d'echantillonnage
niveau = 1
duree = 2
nbEchantillon = duree * fech
amplitude = 127.5 * niveau

parametres = (nbCanal, nbOctet, fech, nbEchantillon, 'NONE', 'not compressed')# tuple
leSon.setparams(parametres)    # creation de l'en-tete (44 octets)

print('Attendez un peu ;-) ...')
for i in range(nbEchantillon):
    valeurData = wave.struct.pack('B', int(128.0 + amplitude * math.sin( 2.0 * math.pi * frequenceGauche * i/fech)))
    valeurData2 = wave.struct.pack('B', int(128.0 + amplitude * math.sin( 2.0 * math.pi * frequenceDroite * i/fech)))
    leSon.writeframes(valeurData)
    leSon.writeframes(valeurData2)

leSon.close()
