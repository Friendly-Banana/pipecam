# pipecam
einfache Mikrofon Steuerung durch Gesten 

# Funktionen
- erkennt beide Hände, rechte Hand hat Vorrang
- neue Virtualcam, um mit allen Anwendungen zu funktionieren

# Installieren
1. [Python](https://www.python.org/downloads/) installieren
2. Virtuelle Kamera installieren
- Windows: [OBS](https://obsproject.com/download) installieren
- Debian: `sudo apt install v4l2loopback-dkms && sudo modprobe v4l2loopback devices=1`
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
