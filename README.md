# Pipecam
einfache Mikrofon Steuerung durch Gesten 

# Funktionen
- erkennt beide Hände, rechte Hand hat Vorrang
- neue Virtualcam, um mit allen Anwendungen zu funktionieren

# Installieren
1. [Python](https://www.python.org/downloads/) installieren
2. Virtuelle Kamera installieren
- Windows: [OBS](https://obsproject.com/download) installieren
- Linux: siehe [hier](#linux-virtuelle-kamera)
3. Projekt runterladen
4. `python3 -m pip install -r requirements.txt` ausführen, um Abhängigkeiten zu installieren
5. `python3 main.py` ausführen

# Bestandteile
- [x] Handerkennung durch [mediapipe](https://mediapipe.dev)
- [ ] Webcam mit [pyvirtualcam](https://github.com/letmaik/pyvirtualcam) für Zoom
- [ ] Mikrofon Steuerung mit Zoom SDK

# Gesten
An Geste (Beispielvideo)

![Gordon Ramsay swiping](https://c.tenor.com/XsEnfr0dKp4AAAAC/gordon-ramsey-swipe.gif)

Aus Geste
wie oben, nur von links nach rechts

# Linux virtuelle Kamera
```
sudo apt install v4l2loopback-dkms # Kernel modul installieren
sudo echo options v4l2loopback nr_devices=1 exclusive_caps=1,1,1,1,1,1,1,1 video_nr=2 card_label=NAME > /etc/modprobe.d/v4l2loopback.conf 
# Config file erstellen, exclusive_caps muss mind. 8 Zahlen sein
sudo echo v4l2loopback > /etc/modules-load.d/v4l2loopback.conf # Autostart
sudo modprobe -r v4l2loopback && sudo modprobe v4l2loopback # (Neu-)Starten
```
