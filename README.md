# Pipecam
einfache Mikrofon Steuerung durch Gesten 

# Funktionen
- erkennt und verfolgt beide Hände
- ermittelt Gesten
- steuert das Mikrofon in Zoom
- leitet Bild weiter, sodass andere Anwendungen die Kamera benutzen können

# Installieren
1. [Python3](https://www.python.org/downloads/) installieren
2. Virtuelle Kamera
- Windows: [OBS](https://obsproject.com/download) installieren
- Linux: siehe [hier](#linux-virtuelle-kamera)
3. Projekt herunterladen
4. `python3 -m pip install -r requirements.txt` ausführen, um Abhängigkeiten zu installieren
5. `python3 main.py` ausführen

# Bestandteile
- [x] Handerkennung durch [mediapipe](https://mediapipe.dev)
- [x] Webcam mit [pyvirtualcam](https://github.com/letmaik/pyvirtualcam)
- [x] Mikrofon Steuerung durch [pyautoit](https://pypi.org/project/PyAutoIt/)

# Gesten
- An Geste (Beispielvideo)
![Gordon Ramsay swiping](https://c.tenor.com/XsEnfr0dKp4AAAAC/gordon-ramsey-swipe.gif)

- Aus Geste
    wie oben, nur von links nach rechts

- Merkel-Raute
<a title="Armin Linnartz, CC BY-SA 3.0 DE &lt;https://creativecommons.org/licenses/by-sa/3.0/de/deed.en&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Angela_Merkel_Juli_2010_-_3zu4.jpg"><img width="256" alt="Angela Merkel Juli 2010 - 3zu4" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Angela_Merkel_Juli_2010_-_3zu4.jpg/256px-Angela_Merkel_Juli_2010_-_3zu4.jpg"></a>

# Konfiguration
Werte in `config.py`
- Anzahl der Bilder, aus denen die Bewegung der Hände errechnet wird
    POS_TO_KEEP = 10

- Bewegung nötig für Mikro an/aus Geste
    GESTURE_TRESHOLD = 0.3

- Maximaler Abstand der Finger bei der Raute
    EXTRA_MAX_DISTANCE = 0.05

- Mediapipes Werte, benötigte Sicherheit der AI, um etwas als Hand zu erkennen
    MIN_DETECTION_CONFIDENCE = 0.5
    MIN_TRACKING_CONFIDENCE = 0.5

# Linux virtuelle Kamera
Ubuntu / Debian
```
sudo apt install v4l2loopback-dkms # Kernel modul installieren
# Config file erstellen, exclusive_caps muss mind. 8 Zahlen sein
sudo echo options v4l2loopback nr_devices=1 exclusive_caps=1,1,1,1,1,1,1,1 video_nr=2 card_label=NAME > /etc/modprobe.d/v4l2loopback.conf
sudo echo v4l2loopback > /etc/modules-load.d/v4l2loopback.conf # Autostart
sudo modprobe -r v4l2loopback && sudo modprobe v4l2loopback # (Neu-)Starten
```
