
# Table of contents
1.[BAP ROSdriven](#BAP ROSdriven)

1. [SBC Setup (Single Board Computer)](#SBCSetup)


- [Table of contents](#table-of-contents)
- [BAP ROSdriven](#bap-rosdriven)
    + [Installeren van ROS op externe computer](#installeren-van-ros-op-externe-computer)
    + [Installeren van afhankelijke ROS Packages](#installeren-van-afhankelijke-ros-packages)
    + [Installeren van TurtleBot3 Packages](#installeren-van-turtlebot3-packages)
    + [Geef aan met welk model gewerkt wordt](#geef-aan-met-welk-model-gewerkt-wordt)
    + [Netwerk configuratie](#netwerk-configuratie)
  * [SBC Setup (Single Board Computer) <a name="SBCSetup"></a>](#sbc-setup--single-board-computer---a-name--sbcsetup----a-)
    + [Voorbereiding](#voorbereiding)
    + [Download de Turtlebot3 SBC Image](#download-de-turtlebot3-sbc-image)
    + [Uitpakken van de image file](#uitpakken-van-de-image-file)
    + [Branden van de image file](#branden-van-de-image-file)
    + [Configuratie van het WIFI-Netwerk](#configuratie-van-het-wifi-netwerk)
    + [Opstarten van de Turtlebot](#opstarten-van-de-turtlebot)
    + [Configuratie van het ROS Netwerk](#configuratie-van-het-ros-netwerk)
    + [OpenCR Test](#opencr-test)
  * [Bringup](#bringup)
    + [Roscore](#roscore)
    + [Bringup TurtleBot3](#bringup-turtlebot3)
  * [Basis besturing](#basis-besturing)
    + [Model TurtleBot3 instellen](#model-turtlebot3-instellen)
    + [Besturing met toetsenbord](#besturing-met-toetsenbord)
    + [Besturing met een controller](#besturing-met-een-controller)
      - [PS3 controller](#ps3-controller)
      - [XBOX 360 controller](#xbox-360-controller)
      - [Wii controller](#wii-controller)
  * [SLAM](#slam)
    + [Starten van de SLAM node](#starten-van-de-slam-node)
    + [Besturing van de Turtlebot in SLAM](#besturing-van-de-turtlebot-in-slam)
  * [Navigatie](#navigatie)
    + [Navigatie starten](#navigatie-starten)
    + [Startpositie geven](#startpositie-geven)
    + [Navigeren naar een doel](#navigeren-naar-een-doel)
    + [Installeren van de Gazebo Packages](#installeren-van-de-gazebo-packages)
    + [Starten van de simulatieomgeving](#starten-van-de-simulatieomgeving)
    + [Maken van een Workspace en Package](#maken-van-een-workspace-en-package)
      - [Modules importeren](#modules-importeren)
      - [Initialiseren van de node](#initialiseren-van-de-node)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>







# BAP ROSdriven

##Computer instellen
### Installeren van ROS op externe computer
Open de terminal met **CRTL + ALT + T** en typ volgende commando's één voor één in.
```shell
sudo apt update
sudo apt upgrade
wget https://raw.githubusercontent.com/ROBOTIS-GIT/robotis_tools/master/install_ros_melodic.sh
chmod 755 ./install_ros_melodic.sh 
bash ./install_ros_melodic.sh
```
### Installeren van afhankelijke ROS Packages
```shell
sudo apt-get install ros-melodic-joy ros-melodic-teleop-twist-joy \
  ros-melodic-teleop-twist-keyboard ros-melodic-laser-proc \
  ros-melodic-rgbd-launch ros-melodic-depthimage-to-laserscan \
  ros-melodic-rosserial-arduino ros-melodic-rosserial-python \
  ros-melodic-rosserial-server ros-melodic-rosserial-client \
  ros-melodic-rosserial-msgs ros-melodic-amcl ros-melodic-map-server \
  ros-melodic-move-base ros-melodic-urdf ros-melodic-xacro \
  ros-melodic-compressed-image-transport ros-melodic-rqt* \
  ros-melodic-gmapping ros-melodic-navigation ros-melodic-interactive-markers
```
### Installeren van TurtleBot3 Packages
Installeer Turtlebot3 via Debian Packages
```shell
sudo apt-get install ros-melodic-dynamixel-sdk
sudo apt-get install ros-melodic-turtlebot3-msgs
sudo apt-get install ros-melodic-turtlebot3
```
### Geef aan met welk model gewerkt wordt
Hier wordt de naam van het type robot toegewezen aan de robot. 
Geef volgend commando in in de terminal.
Het bashrc bestand is een bestand die wordt gelezen wanneer een terminal sessie opstart.
```shell
echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
```
### Netwerk configuratie
Stap 1:
    Verbind de computer met een WIFI-Netwerk dat bij voorkeur werkt met DHCP-reservering zodat 
    de computer een vast ip-adres toegewezen krijgt door het netwerk en zoek het gekregen IP-adres van het apparaat met het volgende commando.
    Onthoud dit IP-adres.
```shell
ifconfig
```



![img_24.png](img_24.png)



Stap 2:
    Dit IP-adres wordt nu in bestand ingegeven dat wordt gebruikt bij het opstarten van de computer.
    Op deze manier zal ROS weten welke het ip-adres is van de ROS_MASTER_URI en de ROS_HOSTNAME.
    Het commando 'nano' laat toe het document eropvolgend aan te passen in een text editor in de terminal.
```shell
nano ~/.bashrc
```
Stap 3:
    Typ **CTRL + END** of **ALT + /** om de cursor naar het einde van de lijn te plaatsen.
    Pas het ip-adres aan zoals aangegeven op onderstaande afbeelding.

![img_28.png](img_28.png)

Sla hierna het document op met **CTRL + S** en sluit het document met **CTRL + X**.

Stap 4: Pas de aanpassingen toe in de huidige terminal met volgend commando.
```shell
Source ~/.bashrc
```
-----
-----

## SBC Setup (Single Board Computer) <a name="SBCSetup"></a>
In dit hoofdstuk zal de installatie gebeuren van de Turtlebot zelf.
Hierbij zal gebruik gemaakt worden van een Raspberry Pi. Dit gehele process zal even duren waardoor de Turtlebot 
best niet gevoed wordt door de batterij. De Turtlebot kan rechtstreek gevoed worden via het controllerbord. 
Om dit hoofdstuk uit te voeren zal een extern toetsenbord en muis nodig zijn. 
### Voorbereiding
Er wordt gebruik gemaakt van een SD-kaart. Zorg dat deze kan gelezen worden door uw computer
### Download de Turtlebot3 SBC Image
Aan de hand van de versie van de raspberry Pi en ROS zal er een bepaalde image file moeten gedownload worden.
Een image file is een bestand dat data bevat die nodig is om een systeem op te starten.



**Betekenis IMG file nakijken/navragen**



[Raspberry Pi 3B+ ROS Melodic image](https://www.robotis.com/service/download.php?no=2011)

[Raspberry Pi 4B (2GB of 4GB) ROS Melodic image](https://www.robotis.com/service/download.php?no=2065)

[Raspberry Pi 4B (2GB of 4GB) ROS Melodic image](https://www.robotis.com/service/download.php?no=1905)


### Uitpakken van de image file

Pak nu het gedownloade bestand uit en sla het op op de lokale schijf.

### Branden van de image file

Voor het branden van de image file moet er een programma gebruikt worden. 

[Raspberry Pi Imager](https://www.raspberrypi.org/software/) kan hiervoor gebruikt worden. 

Open het programma van zodra het geïnstalleerd is.

Voer volgende stappen uit:

![img_2.png](img_2.png)
![img_3.png](img_3.png)
![img_5.png](img_5.png)
![img_7.png](img_7.png)
![img_8.png](img_8.png)
![img_9.png](img_9.png)



### Configuratie van het WIFI-Netwerk

In deze stap wordt het wifi-netwerk geconfigureerd. In een bestand met de naam 50-cloud-init.yaml 
zal de naam van het gewenste netwerk, het WIFI_SSID, aangegeven worden met het daarbij horende wachtwoord.
Dit bestand zal het systeem gebruiken bij het opstarten om een verbinding te maken met het netwerk.

Open een terminal met **CTRL + ALT + T**.

Om dit bestand te bewerken moet men zich bevinden op de locatie waar het bestand zich bevindt.
Wanneer het commando om te bewerken ergens anders ingegeven wordt, 
zal er een nieuw bestand met die naam op die plaats gemaakt worden. Er zal dus een leeg bestand openen.

```shell
cd /media/$USER/writable/etc/netplan
sudo nano 50-cloud-init.yaml
```

Wanneer het bestand geopend is, zou er iets zoals onderstaande afbeelding moeten verschijnen. 
Hier moet WIFI_SSID en WIFI_PASSWORD vervangen worden door de naam van het wifi-netwerk en het bijhorende wachtwoord.
Opgelet, wanneer de inspringingen niet correct zijn, kan dit leiden tot problemen bij het verbinden met het netwerk.
Navigeren in het document gebeurt met de pijltjes. 

Sla hierna het document op met CTRL + S en sluit het document met CTRL + X.

![img_10.png](img_10.png)

### Opstarten van de Turtlebot

1. Connecteer de HDMI-kabel van het externe scherm met de HDMI-poort van de Raspberry Pi
2. Connecteer het toetsenbord met één van de USB-poorten
3. Voer de micro-sd kaart in 
4. Voorzie de Turtlebot van voeding via de 12V poort van het OpenCR bord 
5. Log in met volgende gegevens:
   (hou er rekening mee dat linux geen tekst weergeeft wanneer een wachtwoord getypt wordt)

           Gebruikersnaam: ubuntu
           Wachtwoord: turtlebot

Opgelet: Wanneer er gebruik gemaakt wordt van een extern scherm, aangesloten op de HDMI-poort, 
moet deze aangesloten zijn alvorens de TurtleBot aan te zetten. Wanneer de Raspberry Pi opstart en 
geen apparaat kan vinden zal hij deze poort uitschakelen. Deze zal pas weer werken wanneer TurtleBot opnieuw
zal opgestart worden.

### Configuratie van het ROS Netwerk

In deze stap wordt het ROS netwerk ingesteld. Op deze manier zal er vanaf de ingestelde computer kunnen gecommuniceerd
worden met de TurtleBot. Op deze manier kan de TurtleBot bestuurd en aangepast worden zonder 
extern scherm of toetsenbord. Alles zal vanop de computer gedaan worden via een ssh verbinding. 
Dit zal later nog duidelijk worden.

De volgende bewerkingen worden gemaakt op de Raspberry Pi, niet op de computer die alreeds ingesteld is. 

Stap 1: Controleer de netwerkverbinding en het gekregen IP-adres.
Ga pas naar stap 2 wanneer er een IP-adres verkregen is van het gewenste netwerk.
Geef de TurtleBot en Raspberry Pi minstens een minuut tijd om op te starten. De TurtleBot heeft wat tijd nodig 
om de netwerkverbinding op te starten. Wanneer er nog steeds geen verbinding met het netwerk wordt gemaakt, 
zou het kunnen dat er fout gemaakt is in de stap **Configuratie van het wifi-netwerk**.

Mogelijke fouten hierbij zijn:

1. WIFI_SSID niet correct ingevuld
2. WIFI_PASSWORD is niet correct ingevuld
3. Inspringingen zijn niet correct
4. Een spatie voor of na kan een fout veroorzaken
            
```shell
ifconfig
```
Op onderstaande afbeelding kan de locatie van het IP-adres gevonden worden.
![img_26.png](img_26.png)

Ook de TurtleBot heeft een .bashrc bestand. In dit bestand geven we de TurtleBot, wanneer deze opstart,
mee wie de ROS_MASTER_URI en ROS_HOSTNAME is.
Hier is de ROS_MASTER_URI de eerder geconfigureerde computer en de ROS_HOSTNAME de 
Raspberry Pi van de TurtleBot. 

Open en bewerk het .bashrc bestand met volgend commando: 

```shell
nano ~/.bashrc
```

Navigeer in het bestand naar onder en pas de IP-adressen van de ROS_MASTER_URI en ROS_HOSTNAME aan.

- Het IP-adres van ROS_MASTER_URI is het IP-adres van de ingestelde computer.

Vervang {IP_ADDRESS_OF_REMOTE_PC} door het IP-adres van de ingestelde computer.

- Het IP-adres van de ROS_HOSTNAME is het IP-adres van de Raspberry Pi.

Vervang {IP_ADDRESS_OF_RASPBERRY_PI_3} door het IP-adres van de Rasberry Pi.

![img_27.png](img_27.png)

Sla hierna het document op met **CTRL + S** en sluit het document met **CTRL + X**.

Pas de aanpassing toe met volgend commando:

```shell
source ~/.bashrc
```

----
----


##OpenCR setup (Open-source Control Module for ROS)

In dit hoofdstuk wordt de OpenCR geconfigureerd. OpenCR staat voor Open-source Control Module for ROS en is ontwikkeld
speciaal voor ROS om een compleet open-source hardware en software te voorzien. De ontwikkelomgeving voor OpenCR is 
opengesteld voor het brede publiek. Zowel studenten die met Arduino of scratch werken en experts die met meer 
traditionele software werken kunnen aan de slag met het OpenCR bord.

![img_16.png](img_16.png)

###OpenCR setup

Stap 1: Installeren van de benodigde packages op de Raspberry Pi om up te loaden naar de OpenCR
```shell
sudo dpkg --add-architecture armhf
sudo apt-get update
sudo apt-get install libc6:armhf
```
Stap 2: Meegeven van het model van de TurtleBot
```shell
export OPENCR_PORT=/dev/ttyACM0
export OPENCR_MODEL=burger
rm -rf ./opencr_update.tar.bz2
```
Stap3: Download de firmware en lader.
```shell
wget https://github.com/ROBOTIS-GIT/OpenCR-Binaries/raw/master/turtlebot3/ROS1/latest/opencr_update.tar.bz2 
tar -xvf opencr_update.tar.bz2 
```
Stap 4: Uploadde firmware van de Raspberry Pi naar de OpenCR
```shell
cd ./opencr_update
./update.sh $OPENCR_PORT $OPENCR_MODEL.opencr
```
Stap 5: Wanneer de upload succesvol is, zou de terminal er als volgt moeten uitzien:

![img_14.png](img_14.png)

Stap 6: Indien de upload niet succesvol is, kan er geüpload worden in de recovery mode.
Volf volgende stappen om de OpenCR in recovery mode te brengen. Wanneer de OpenCR in recovery mode is, 
zal de status led, knipperen.

- Hou de SW2 drukknop ingedrukt.
- Druk op de Reset knop.
- Laat de Reset knop los.
- Laat de SW2 drukknop los.

![img_17.png](img_17.png)

### OpenCR Test

De Robot kan getest worden van zodra deze volledig geassembleerd is.

- Voorzie de robot van voeding, een rode led zal branden.
- Plaats de robot op een vlakke ondergrond met een vierkante meter open ruimte.
- Wanneer de SW1 knop een aantal seconden ingedrukt wordt, zou de robot 30cm vooruit moeten rijden.
- Wanneer de SW2 knop een aantal seconden ingedrukt wordt, zou de robot 180° moeten roteren.

---
---

## Bringup

In het hoofdstuk Bringup maken we vanop afstand verbinding met de Turtlebot vanaf de computer. De turtlebot_bringup 
zal de nodige scripts starten om de basis functies van de TurtleBot te starten. 

### Roscore
Om verbinding te kunnen maken, moet er in een terminal roscore gestart worden. Roscore is een verzameling van nodes 
en programma's die noodzakelijk zijn om een ROS-systeem op te starten. 
Er moet een roscore actief zijn om verschillende nodes met elkaar te laten communiceren.

Roscore zal de volgende zaken opstarten:
- een ROS Master
- een ROS parameter server
- een rosout logging node

Wanneer een package gestart wordt met een roslaunch commando, zal er automatisch een roscore mee opstart worden.


Een roscore wordt gestart met volgend commando:

```shell
roscore
```
### Bringup TurtleBot3

Om vanop afstand verbinding te maken met de Raspberry Pi zal een ssh-verbinding opgestart worden. Een ssh-verbinding 
is een 'secure shell' en staat toe op een versleutelde manier op een andere computer of server in te loggen en 
vanop afstand commando's uit te voeren.

Open een nieuwe terminal met **CTRL + ALT + T** en maak verbinding met de Raspberry Pi via zijn IP-adres.
Het standaard wachtwoord van de TurtleBot3 is 'turtlebot'. Geef de TurtleBot3 genoeg tijd om op te starten. 
Het kan tot meer dan een minuut na opstarten duren vooraleer verbinding kan gemaakt worden.

```shell
ssh ubuntu@{IP_ADDRESS_OF_RASPBERRY_PI}
```
Wanneer verbinding gemaakt is met Raspberry Pi zal er dus een andere gebruikersnaam zichtbaar zijn in de terminal.
Als dit het geval is, kan het bringup commando ingegeven worden.
```shell
roslaunch turtlebot3_bringup turtlebot3_robot.launch
```
Indien alles correct verloopt, zou de terminal er als volgt moeten uitzien:
```shell
SUMMARY
 ========

 PARAMETERS
 * /rosdistro: melodic
 * /rosversion: 1.14.3
 * /turtlebot3_core/baud: 115200
 * /turtlebot3_core/port: /dev/ttyACM0
 * /turtlebot3_core/tf_prefix:
 * /turtlebot3_lds/frame_id: base_scan
 * /turtlebot3_lds/port: /dev/ttyUSB0

 NODES
 /
     turtlebot3_core (rosserial_python/serial_node.py)
     turtlebot3_diagnostics (turtlebot3_bringup/turtlebot3_diagnostics)
     turtlebot3_lds (hls_lfcd_lds_driver/hlds_laser_publisher)

 ROS_MASTER_URI=http://192.168.1.2:11311

 process[turtlebot3_core-1]: started with pid [14198]
 process[turtlebot3_lds-2]: started with pid [14199]
 process[turtlebot3_diagnostics-3]: started with pid [14200]
 [INFO] [1531306690.947198]: ROS Serial Python Node
 [INFO] [1531306691.000143]: Connecting to /dev/ttyACM0 at 115200 baud
 [INFO] [1531306693.522019]: Note: publish buffer size is 1024 bytes
 [INFO] [1531306693.525615]: Setup publisher on sensor_state [turtlebot3_msgs/SensorState]
 [INFO] [1531306693.544159]: Setup publisher on version_info [turtlebot3_msgs/VersionInfo]
 [INFO] [1531306693.620722]: Setup publisher on imu [sensor_msgs/Imu]
 [INFO] [1531306693.642319]: Setup publisher on cmd_vel_rc100 [geometry_msgs/Twist]
 [INFO] [1531306693.687786]: Setup publisher on odom [nav_msgs/Odometry]
 [INFO] [1531306693.706260]: Setup publisher on joint_states [sensor_msgs/JointState]
 [INFO] [1531306693.722754]: Setup publisher on battery_state [sensor_msgs/BatteryState]
 [INFO] [1531306693.759059]: Setup publisher on magnetic_field [sensor_msgs/MagneticField]
 [INFO] [1531306695.979057]: Setup publisher on /tf [tf/tfMessage]
 [INFO] [1531306696.007135]: Note: subscribe buffer size is 1024 bytes
 [INFO] [1531306696.009083]: Setup subscriber on cmd_vel [geometry_msgs/Twist]
 [INFO] [1531306696.040047]: Setup subscriber on sound [turtlebot3_msgs/Sound]
 [INFO] [1531306696.069571]: Setup subscriber on motor_power [std_msgs/Bool]
 [INFO] [1531306696.096364]: Setup subscriber on reset [std_msgs/Empty]
 [INFO] [1531306696.390979]: Setup TF on Odometry [odom]
 [INFO] [1531306696.394314]: Setup TF on IMU [imu_link]
 [INFO] [1531306696.397498]: Setup TF on MagneticField [mag_link]
 [INFO] [1531306696.400537]: Setup TF on JointState [base_link]
 [INFO] [1531306696.407813]: --------------------------
 [INFO] [1531306696.411412]: Connected to OpenCR board!
 [INFO] [1531306696.415140]: This core(v1.2.1) is compatible with TB3 Burger
 [INFO] [1531306696.418398]: --------------------------
 [INFO] [1531306696.421749]: Start Calibration of Gyro
 [INFO] [1531306698.953226]: Calibration End
```

---
---
## Basis besturing

Voor het besturen van de TurtleBot3 zijn er verschillende mogelijkheden.
De TurtleBot3 kan enerzijds met het toetsenbord van de computer bestuurd worden, anderzijds kan deze ook met een 
controller bestuurd worden. Er zijn verschillende packages beschikbaar afhankelijk van de soort controller die wenst
gebruikt te worden.

### Model TurtleBot3 instellen

Om ervoor te zorgen dat er niet telkens manueel moet meegegeven worden aan de TurtleBot3 welk model deze is, kan volgend
commando's gebruikt worden.

```shell
echo 'export TURTLEBOT3_MODEL=burger' >> ~/.bashrc
source ~/.bashrc
```

### Besturing met toetsenbord

Voor de besturing met het toetsenbord moeten geen extra packages gedownload worden.
Open een terminal met **CTRL + ALT + T** op de computer zelf, niet in de ssh-verbinding met de Raspberry Pi.

```shell
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```
Indien de node succesvol is gestart, zou de terminal er als volgt moeten uit zien.
```shell
Control Your Turtlebot3
Moving around
     w
 a   s   d
     x
w/x : increase/decrease linear velocity
a/d : increase/decrease angular velocity
space key, s : force stop
CTRL-C to quit
```

### Besturing met een controller
#### PS3 controller
Om de TurtleBot3 te besturen met een PS3 controller, moet de controller via bluetooth of met een USB-kabel verbonden
worden met de computer. 
Installeer daarna de juiste packages met onderstaand commando.
```shell
sudo apt-get install ros-melodic-joy ros-melodic-joystick-drivers ros-melodic-teleop-twist-joy
```
Indien de packages correct zijn geïnstalleerd, zou de TurtleBot3 met de PS3 controller bestuurbaar moeten zijn 
na het invoeren van volgend commando.

```shell
roslaunch teleop_twist_joy teleop.launch
```
#### XBOX 360 controller
Om de TurtleBot3 te besturen met een XBOX 360 controller, moet de controller via een draadloze adaptor of 
met een USB-kabel verbonden worden met de computer. 
Installeer daarna de juiste packages met onderstaand commando.
```shell
sudo apt-get install xboxdrv ros-melodic-joy ros-melodic-joystick-drivers ros-melodic-teleop-twist-joy
```
Indien de packages correct zijn geïnstalleerd, zou de TurtleBot3 met de XBOX 360 controller bestuurbaar moeten zijn 
na het invoeren van volgend commando.

```shell
sudo xboxdrv --silent
roslaunch teleop_twist_joy teleop.launch
```
#### Wii controller
Om de TurtleBot3 te besturen met een Wii controller, moet de controller via bluetooth verbonden zijn met de computer.
Installeer daarna de juiste packages met onderstaand commando.
```shell
sudo apt-get install ros-melodic-wiimote libbluetooth-dev libcwiid-dev
cd ~/catkin_ws/src
git clone https://github.com/ros-drivers/joystick_drivers.git  
cd ~/catkin_ws && catkin_make
```
Indien de packages correct zijn geïnstalleerd, zou de TurtleBot3 met de Wii controller bestuurbaar moeten zijn 
na het invoeren van volgende commando's.
```shell
rosrun wiimote wiimote_node
rosrun wiimote teleop_wiimote
```

---
---

## SLAM

SLAM staat voor Simultaneous Localization and Mapping is een techniek gebruikt om een kaart te maken van 
een willekeurige ruimte door gebruik te maken zijn eigen geschatte locatie. SLAM is een gekende functie van Turtlebot 
en zijn voorgangers. 
Voor SLAM zal de TurtlBot3 de LDS(Laser Distance Sensor) 

### Starten van de SLAM node

Stap 1:

Start roscore van op de computer
```shell
roscore
```

Stap 2:

Zorg dat de TurtleBot3 actief is door de bringup te activeren op de Raspberry Pi.

```shell
ssh ubuntu@{IP_ADDRESS_OF_RASPBERRY_PI}
roslaunch turtlebot3_bringup turtlebot3_robot.launch
```

Stap 3:
Open een nieuwe terminal en start de SLAM node. 
Rviz (ROS Visualization) zou moeten openen. 
Rviz is een krachtig 3D programma om te visualizeren wat de robot denkt dat er gebeurt.
```shell
roslaunch turtlebot3_slam turtlebot3_slam.launch
```
### Besturing van de Turtlebot in SLAM

In Rviz is nu zichtbaar wat de robot ziet. Door met de robot rond te rijden, kan er een groter gebied in kaart gebracht 
worden. De kaart wordt gemaakt gebaseerd op de odometrie, tf en scan van de robot. Terwijl de robot zich verplaatst
in de ruimte, zal dit op de kaart in Rviz ook weergegeven worden en zal de kaarten getekend worden.

Een uitgebreide uitleg over Rviz is te vinden ...................



**INVOEREN VAN SCREENSHOT VAN BASIS SLAM**



```shell
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

 Control Your TurtleBot3!
 ---------------------------
 Moving around:
        w
   a    s    d
        x

 w/x : increase/decrease linear velocity
 a/d : increase/decrease angular velocity
 space key, s : force stop

 CTRL-C to quit
```

###Opslaan van de kaart

Wanneer de volledige ruimte in kaart is gebracht, kan deze kaart opgeslagen en gebruikt worden in het volgende 
hoofdstuk Navigatie. Daar zal kunnen genavigeerd worden door de ruimte door hem een doel te geven.
Gebruik volgend commando op de kaart op te slaan. 'kaart' kan vervangen worden door een bestandsnaam naar keuze.

```shell
rosrun map_server map_saver -f ~/kaart
```
Dit commando zal twee soorten bestanden opslaan. Een .yaml en een .pgm bestand zullen opgeslagen worden op de 
thuislocatie ~/. Dit is kort voor /home/${username}. -f geeft een specifieke locatie aan waar de bestanden opgeslagen 
worden. 

---
---

## Navigatie

In het hoofdstuk navigatie kan de robot gevraagd worden naar een specifieke locatie te rijden.
Om dit te kunnen realiseren, is er een kaart nodig van de ruimte waarin de robot gaat rondrijden.
Deze kaart moet de grootste obstakels en muren bevatten zodat hij zich kan oriënteren op de kaart.
Hij zal al deze objecten en muren gebruiken om zijn locatie in de ruimte. 

### Navigatie starten

Stap 1:

Start roscore van op de computer indien deze nog niet actief is.

```shell
roscore
```

Stap 2:

Zorg dat de TurtleBot3 actief is door de bringup te activeren op de Raspberry Pi.

```shell
ssh ubuntu@{IP_ADDRESS_OF_RASPBERRY_PI}
roslaunch turtlebot3_bringup turtlebot3_robot.launch
```

Stap 3:

Start de navigatie met onderstaand commando.

```shell
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/kaart.yaml
```


### Startpositie geven

Rviz is reeds opgestart en toont de kaart, de robot en een groene puntenwolk. De groene punten geven de objecten
aan die de robot opmerkt op dat moment. De zwarte lijnen zijn de objecten die door SLAM gescand zijn.
Om deze twee kaarten gelijk te krijgen moeten we de robot een startlocatie en kijkrichting geven.
In Rviz start de robot steeds op positie (0,0). Dit is zelden de positie waar de robot zich effectief bevind.

Stap 1:

Door in Rviz op de groene pijl te klikken, kunnen we de robot een startlocatie en kijkrichting geven.
Klik nu op de locatie op de kaart waar de robot zich moet bevinden en sleep de pijl in de correcte kijkrichting.

![img_18.png](img_18.png)

Stap 2: 

Er worden veel groene kleine pijltjes weergegeven, dit zijn allemaal locaties waar de software denkt dat 
de robot zich zou kunnen bevinden. Hoe meer de robot beweegt, hoe minder groene pijltjes er zullen zijn
en hoe meer exact zijn locatie op de kaart zal zijn in vergelijking met zijn werkelijke positie in de ruimte.
Het bewegen van de robot kan met behulp van het toetsenbord, of met de controller.

Gebruik het juiste commando, afhankelijk van de gebruikte manier.

Indien het toetsenbord gebruikt word, kan onderstaand commando gebruikt worden in een nieuwe terminal.
```shell
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```
Stap 3: 

Beweeg de robot in alle richtingen zodat de software zijn locatie precies kan bepalen. De software zal 
de gemaakte kaarten gelijk proberen leggen met de observatie van de laserscan van de robot. Hoe meer deze beide 
kaarten overeenkomen, hoe meer exact de geschatte locatie zal zijn.

![img_20.png](img_20.png)



**INSERT EIGEN FOTO'S VAN ESTIMATED LOCATION**



Stap 4:

Wanneer de locatie gekend is, moet de tele-operatie gestopt worden. Gebruik hiervoor **CTRL + C** in de juiste terminal.
Dit moet zodat de robot niet van twee verschillende nodes input kan krijgen over wat hij moet doen.


### Navigeren naar een doel

De TurtleBot3 kan nu een doel gegeven worden naar waar deze kan navigeren. De robot zal een traject creëeren 
naar het doel, gebaseerd op de 'global path planner'. Wanneer er een object in op de route van de robot geplaatst wordt,
zal de robot gebruik maken van de 'local path planner' om dit object te vermijden.


Klik op de rode pijl in het menu van Rviz. Klik vervolgens op de plaats op de kaart naar waar de robot moet 
rijden en sleep in welke richting deze moet kijken wanneer de robot zijn doel bereikt heeft.

![img_21.png](img_21.png)



**INSERT EIGEN FOTO'S VAN NAVIGATIE**



![img_22.png](img_22.png)

---
---

##Gazebo simulatie

![img_23.png](img_23.png)

De TurtleBot3 kan ook geprogrammeerd en ontwikkeld worden in een virtuele simulatieomgeving. TurtleBot3 is namelijk 
beschikbaar in de 3D robot simulator Gazebo. De Gazebo simulatieomgeving maakt gebruik van ROS Gazebo Packages.

### Installeren van de Gazebo Packages

```shell
cd ~/catkin_ws/src/
git clone -b melodic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
cd ~/catkin_ws && catkin_make
```

### Starten van de simulatieomgeving

Gazebo kan gestart worden met een lege wereld, dit wil zeggen dat er geen enkele muur of object aanwezig is.
```shell
roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
```

Om een bestaande wereld te laden, moet het laatste deel van het commando vervangen worden door de gewenste map.

```shell
roslaunch turtlebot3_gazebo turtlebot3_world.launch
```
Er bestaand al verschillende werelden in Gazebo die kunnen gebruikt worden.

```shell
multi_map_merge.launch              
multi_turtlebot3.launch             
multi_turtlebot3_slam.launch        
turtlebot3_autorace_2020.launch     
turtlebot3_autorace.launch          
turtlebot3_autorace_mission.launch  
turtlebot3_empty_world.launch       
turtlebot3_gazebo_rviz.launch   
turtlebot3_house.launch
turtlebot3_simulation.launch
turtlebot3_stage_1.launch
turtlebot3_stage_2.launch
turtlebot3_stage_3.launch
turtlebot3_stage_4.launch
turtlebot3_world.launch
```

Ook hier kan de turtlebot in aangestuurd worden met het toetsenbord, kan SLAM in gebruikt worden en
kan er genavigeerd worden.






---
---













---
---

##Stap voor stap programmeren
In de vorige hoofdstukken is python kort verduidelijks, is ROS geinstalleerd, is de basis gelegd van het besturen van 
de TurtleBot aan de hand van bestaande packages en nodes. Nu de werking en het gebruik ervan gekend is, 
kan er zelf aan de slag gegaan worden. In dit hoofdstuk zullen er ROS workspaces en ROS packages gemaakt worden. 
Ook zullen er zelf nodes ontwikkeld worden en zal de Turtlebot door een eigen programma aangestuurd worden. 
Eerst zal een bericht gepublished worden door een node. Een andere node zal dit bericht subsriben en weergeven. 
Hierna zal een Rostopic uitgelezen worden die door de TurtleBot3 verstuurd worden. 
Daarna zal een Rostopic naar de TurtleBot3 verstuurd worden om zo uiteindelijk tot het eindresultaat te komen waarbij 
de Turtlebot3 zelf naar meerdere gekozen locaties na elkaar zal rijden, dit zal de SimpleGoal heten.

### Maken van een Workspace en Package

####ROS Workspace
De ROS packages worden bewaard in ROS workspaces. Packages kunnen gemaakt worden en geïnstalleerd worden.
Bij het ingeven van volgend commando, zal een workspace 'catkin_ws' aangemaakt worden met daarin een bestandsmap src.

```shell
mkdir -p ~/catkin_ws/src 
```
Ga hierna naar die bestandslocatie op de volgende manier. 

```shell
cd catkin_ws/src
```
Hier kan de workspace geïnitialiseerd worden. Dit gebeurt met volgend commando.

```shell
catkin_init_workspace
```
De volgende boodschap zou moeten verschijnen in de terminal

```shell
Creating symlink "/home/rosdriven1/catkin_ws/src/CMakeLists.txt"
```

Na het initialiseren van de workspace, moet deze gebuild worden.
Ga hiervoor naar de catkin_ws folder door een folder terug te keren.
Volgend commando gaat 1 map terug naar 'boven'.

```shell
cd ..
```
Typ hier het commando om de workspace te builden.

```shell
catkin_make
```

De terminal zou er min of meer als volgt moeten uitzien.

![img_29.png](img_29.png)

Er zijn hierna een aantal mappen toegevoeg aan de map catkin_ws.

![img_30.png](img_30.png)

In de src map worden de packages bewaard. ROS packages creëren alleen een uitvoerbaar bestand wanneer deze zich in
de src map bevindt.

De volgende stap is het toegankelijk en zichtbaar maken van deze packages in de workspace. 
Voer de volgende stappen hiervoor uit. 

Open een terminal en typ in de thuismap het volgende commando om het bashrc bestand te wijzigen.

```shell
gedit .bashrc
```
Voeg volgende lijn toe op het einde van het bestand. 

```shell
source ~/catkin_ws/devel/setup.bash
```
![img_31.png](img_31.png)

Wanneer het catkin_make commando uitgevoerd wordt, wordt elke package gebuild, deze built bestanden worden 
in de build map opgeslagen. Ook worden er uitvoerbare bestanden gemaakt. Deze bestanden worden in de devel map opgeslagen.
De devel map bevat dus de scripts die uitgevoerd kunnen worden. 

Hierna moeten de uitvoerbare bestanden nog geinstalleerd worden. Dit kan met het volgende commando in 
de terminal wanneer in de catkin_ws map.

```shell
catkin_make install
```

####ROS Package

Na het creëren van een ROS workspace, kan nu een ROS package gepaakt worden. In deze packages worden de nodes bewaard.
Het maken van een package gebeurt met het volgende commando.

```shell
catkin_create_pkg ros_package_name package_dependencies
```
Dit kan uitgevoerd worden in de src map van de workspace.
Voorbeeld:
```shell
catkin_create_pkg hello_world roscpp rospy std_msgs 
```

Met dit commando is dus een package gemaakt met de naam hello_world. 
Het package bevat de volgende zaken:

- CMakeLists.txt: Dit bestand bevat alle commando's om in het package de ROS broncode te bouwen en het 
uitvoerbaar bestand te maken.
- Package.xml: dit is een XML-bestand dat informatie bevat over het package.
- Src: de broncode van de ROS packages worden hierin bewaard. Voor python wordt in deze map nog een map scripts gemaakt.
- Include: Dit bestand bevat het package zijn header bestanden.

###Rospy

Rospy is de ROS client library voor Python. Client libraries zijn een verzameling van van code met functies
om ROS concepten toe te voegen. Door deze libraries toe te voegen bij het maken van een ROS-node zal dit tijdsbesparend
zijn voor het ontwikkelen van software.

In het begin van een ROS-node zal steeds de lijn 'import rospy' te vinden zijn. 

```python
import rospy
```
#### Modules importeren
Rospy bevat alle belangrijke ROS functies. 

Vervolgens zal een lijn code zoals hieronder vaak te vinden zijn. Hierin wordt een string message type geïmporteerd 
in python. 

```python
from std_msgs.msg import String
```

std_msgs.msg is de naam van het package en String is de message type die uit het package komt die zal worden gebruikt 
in de node.

#### Initialiseren van de node

Vervolgens zal de node moeten geïnitialiseerd worden. Dit gebeurd met de volgende lijn code in het python bestand.
Hier zal de naam van de node ingegeven worden, alsook een argument die ervoor zorg dat de node steeds uitgevoerd 
kan worden.

```python
rospy.init_node('naam_van_node', anonymous:True)
```

####ROS Message Definitie

Om een topic te publishen, moet er een ROS message definitie gemaakt worden. Op die manier kan er data uit
de ROS message gehaald worden.
Met onderstaande code kan men "string data voorbeeld" als data in de message String steken. 


```python
msg = String()
msg.data = "string data voorbeeld"
```


###Eerste nodes

Bij het maken van nodes in ROS is het kunnen publishen en subscriben bijna noodzakelijk.

####Structuur Publishen en Subscriben
De gedachtegang bij het Publishen gaat als volgt.
```python
publisher_voorbeeld= rospy.Publisher('topic_naam',message_type,queue_size)
```

Dit kan duidelijk uitgelegd worden bij het invullen van het voorbeeld.
```python
pub = rospy.Publisher('chatter', String, queue_size=10)
pub.publish(hello_str)
```
- pub: Dit is de message definitie de zelf gekozen wordt
- rospy.Publisher: Dit is de klasse die gebruikt wordt om iets te publishen
- 'chatter': Dit is de naam van het topic
- String: Dit is het type van het bericht, in dit geval tekst
- Queue_size: Dit is een waarde die gegeven wordt waar wordt naar gekeken als er meerdere zaken
tegelijk moeten worden verwerkt. 

De gedachtengang bij Subscriben loopt grotendeel gelijk.

```python
rospy.Subscriber('topic_naam', message_type, callback functie naam)
```
Met het volgend commando kan gesubscribed worden op het topic 'chatter' met als message_type String.
Wanneer er data binnengehaald wordt, zal de functie 'callback' getriggerd worden.
```python
rospy.Subscriber('chatter', String, callback)
```
De callback functie zal er als volgt uitzien. Dit zal later duidelijker worden in een werkend 
programma.

```python
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
```

####Talker

Wanneer het vorige geziene toegepast wordt, kan een node er als volgt uit zien. 
Deze node is een bestand in de scripts map in de package hello_world zoals eerder uitgelegd.

1. Workspace maken 
2. Package maken
3. Map scripts aanmaken in de Package
4. In de terminal 'touch talker.py' om een leeg bestand te maken
5. gedit talker.py om het bestand te bewerken
6. chmod +x talker.py om het bestand uitvoerbaar te maken


Talker.py
```python
#! /usr/bin/env python

# import

import rospy
from std_msgs.msg import String

def talker():

	rospy.init_node('talker', anonymous=True)
	pub = rospy.Publisher('chatter', String, queue_size=10)
	rate = rospy.Rate(10) #10hz

	while not rospy.is_shutdown():
		hello_str = "hello world %s" % rospy.get_time()
		rospy.loginfo(hello_str)
		pub.publish(hello_str)
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
```
Wat wordt er precies gedaan in de node?

- In onderstaande node kan gezien worden dat rospy en de Ros message module geïmporteerd worden.
- Er wordt een functie gemaakt met de naam talker

- Daarin wordt de node geïnitialiseerd en een nieuwe ROS publisher gemaakt.

- De rospy.Rate functie wordt gebruikt om exact aan 10hz de loop te laten publishen.

- Vervolgens wordt de loop gemaakt die zal werken wanneer rospy actief is.
- Er wordt in een variabele gemaakt met de naam hello_str, daarin wordt tekst gestoken en de tijd
op dat moment toegevoegd worden aan de variabele.

- De rospy.loginfo zal in de terminal de topic weergeven.

- Met pub.publish wordt de variabele hello_str gepublished.

- De rate functie wordt hier geactiveerd, hierdoor zal de node een bepaalde tijd 'slapen'

- Het laatste deel zal de functie talker activeren en zal eventuele fouten/exceptions opvangen.




####Listener

Om door een andere node te subscriben op het topic dat door de talker gepublished wordt, 
kan een node listener.py gemaakt worden.


Listener.py
```python
#! /usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def listener():

	rospy.init_node('listener', anonymous=True)

	rospy.Subscriber("chatter", String, callback)

	rospy.spin()

if __name__ == '__main__':
	listener()
```
Wat wordt er nu precies gedaan in deze node dat nieuw is ten opzichte van de talker node?

- Er wordt een callback functie aangemaakt die zal getriggerd worden en de data zal weergeven in de terminal.

- De listenerfunctie wordt aangemaakt waarin de node geïnitialiseerd wordt.

- Met rospy.Subscriber wordt de topic met de naam /chatter en message type String binnengehaald en naar de callbackfunctie
gestuurd.

- rospy.spin zorgt voor een oneindige loop.

- Het laatste deel voert de functie listener() uit.

####Uitvoeren van de nodes


Zoals eerder gezien kan deze ROS nodes nu uitgevoerd worden met het commando's.

Start de roscore
```shell
roscore
```
Start de talker node
```shell
rosrun hello_world talker.py
```
Start de listener node
```shell
rosrun  hello_world listener.py
```
De terminals zouden er op dat moment zo moeten uitzien.

![img_32.png](img_32.png)

###Subscriben van een rostopic

In het vorige deel werd door een zelfgemaakte node een topic gepublished en uitgelezen door 
een andere zelfgemaakte node. Nu kan deze kennis gebruikt worden om te subscriben op topics die door de TurtleBot3
gepublished worden.



Wanneer de verbinding met de TurtleBot3 tot stand is gebracht, zal met het commando 'rostopic list' een lijst kunnen
verkregen worden van topics die gepublished worden op dat moment. 

Om even op te frissen hoe deze verbinding tot stand wordt gebracht.
- Stap 1

![img_34.png](img_34.png)

In het voorbeeld wordt de batterijstatus van de Turtlebot3 opgevraagd. De TurtleBot3 published deze constant.
Indien meer informatie over een topic gewenst is, kan volgende commando gebruikt worden.

```shell
roptopic info /topic_naam
```

![img_35.png](img_35.png)

Hieruit kan het message_type gehaald worden om deze te importeren in de subscriber node.

De Subscriber node zou er als volgt kunnen uitzien. De structuur van de node is gelijklopend aan de vorige 
subscribernode.
Hier is de topic /battery_state en de message_type BatteryState.
Wanneer deze data binnenkomt, zal de functie callbackBatteryState opgeroepen worden.
In deze functie zal de date kunnen geprint worden in de terminal. 
In plaats van het volledige bericht te print met 'print(msg)' kan gekozen worden om maar een deel van het bericht te 
gebruiken. Het is mogelijk met 'rostopic echo /topic_naam' te zien hoe de topic is volledig uit ziet.
Wanneer nu 'print(msg.voltage)' gevraagd wordt, zal enkel dat deeltje geprint worden.

![img_36.png](img_36.png)

ListenerBattery.py
```python
#! /usr/bin/env python

import rospy
from sensor_msgs.msg import BatteryState

def callbackBatteryState(msg):
	print ("Header: ")
	print (msg.header)
	print ("Voltage: ")
	print (msg.voltage)

def main():

	rospy.init_node('ListenerBattery')

	rospy.Subscriber("battery_state", BatteryState, callbackBatteryState)

	rospy.spin()

if __name__ == '__main__':
	main()


```
De bovenstaande code zou een bericht zoals dit moeten weergeven. 
Zoals gevraagd wordt de header en de spanning weergegeven.

![img_33.png](img_33.png)


###Subscriben op de LDS
![img_37.png](img_37.png)

Om de Turtlebot3 uiteindelijk autonoom te laten rijden, moet de laser uitgelezen en geïnterpreteerd worden.
In onderstaand programma wordt door de main functie een node geïnitialiseerd en er wordt gesubscribed op het 
LaserScan topic waarna dit herhaald zal worden. 

De callbackfucntie zal getriggered worden en zal de gevraagde data weergeven in de terminal. 
Met 'len' voor een lijst met waarden in te zetten, zal python de hoeveelheid waarden afdrukken.
De LaserScan geeft 360 waarden weer, wat neer komt op 1 waarde per graad rondom zich aangezien hij 360° 
rondom zich kijkt. 
De header zal van het bericht bepaalde informatie bevatten zoals een tijdstip en frame_id.
De waarden die de laser weergeeft komen overeen met de afstand in meter van het middelpunt van de laser tot waar deze 
een object tegen komt. Indien er binnen de afstand van 3.5 meter niets staat, zal de LaserScan een inf of een
0.0 waarden geven. Hier moet zeker rekening mee gehouden worden.

ListenerLaserscan.py
```python
#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def callbackLaserScan(msg):
	print (len(msg.ranges)) #Dit zal het aantal waardes weergeven die de laser waarneemt.
	print (msg.header) #Dit zal de header van de Laserscan weergeven. 
    print (msg) #Dit zal telken alle waarden weergeven in de terminal. 

def main():

	rospy.init_node('ListenerLaserscan') #node initialiseren

	rospy.Subscriber("scan", LaserScan, callbackLaserScan) #subscriber aanmaken op de LaserScan met een callbackfucntie

	rospy.spin() #oneindige loop maken van deze node

if __name__ == '__main__':
	main()

```

###Uitlezen van een bepaalde hoek van de laserscan

Om het vorige programma nog wat uit te breiden, kan er bijvoorbeeld alleen een bepaalde hoeveelheid van deze waarden 
opgevraagd worden. Wanneer bijvoorbeeld alleen moet geweten zijn wat er zich voor de TurtleBot bevindt, doen de andere 
waarden er niet toe op dat moment. De 360 waarden worden automatisch in een soort lijst gestoken met de naam ranges.
De waarde 0 bevindt zich recht voor de TurtleBot3, de waarde 180 zal recht achter zich zijn. Wanneer dus de

Laserhoek.py
```python
import rospy
from sensor_msgs.msg import LaserScan

def laser_callback(msg):

    print("Nieuwe groep waarden")
    print (msg.ranges[0:20])
    
def main():    
    rospy.init_node('Laserhoek')
    laser_sub = rospy.Subscriber('scan', LaserScan, laser_callback)
    rospy.spin()

if __name__ == '__main__':
	main()
```
###Publishen van een topic

```python
#! /usr/bin/env python

# import

import rospy
from geometry_msgs.msg import Twist

def main():

        rospy.init_node("SpeedTest")	
        rate = rospy.Rate(10) #10hz
	move = Twist() #defining the way we can allocate de values
	move.linear.x = 0.1 #allocating the values in x direction - linear
	move.angular.z = 0 #allocating the values in z direction - angular
	pub = rospy.Publisher('cmd_vel', Twist , queue_size=1)


	#De waarden van de move.linear.x mogen niet hoger zijn dan 0,23



        while not rospy.is_shutdown():
                pub.publish(move)
                rate.sleep()

if __name__ == '__main__':
		main()
```

###Wall evading

```python
#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def laser_callback(msg):

	#Proces van het uitzoeken hoe de scan werkte

	#print msg #lezen van alle waarden van de LaserScan
	#print len(msg.ranges) #aantal waarden dat de laser uitstuurt
	#print msg.ranges[180] #waarde op plaats 180
	#print 'afstand achter robot ', msg.ranges[0]
	#afstand_voor = msg.ranges[0]
	#afstand_voor1 = msg.ranges[350]
	#afstand_voor2 = msg.ranges[10]
	#print (afstand_voor1,afstand_voor,afstand_voor2)

	minimum1 = min (msg.ranges[330:360])
	minimum2 = min (msg.ranges[0:30])
	minimum = min (minimum2,minimum1)

	print ("mimimum: ",minimum)
	if minimum < 0.3: #0.5 voor halve meter van de muur, 0.0 voor als de object te ver staat
		print ('stop')
		move.linear.x = 0	
		move.angular.z = 2
	else:
		move.angular.z = 0
		move.linear.x = 0.22
		

rospy.init_node('wall_evading')
laser_sub = rospy.Subscriber('scan', LaserScan, laser_callback) #uitlezen van de scan van LaserScan message
	
rate = rospy.Rate(100) #xxhz
move = Twist() #definieren van variabele om waarden toe te kunnen kennen
move.linear.x = 0.1 #toekennen waarden in x-richting - lineair
move.angular.z = 0 #toekennen waarden in z-richting - hoek
pub = rospy.Publisher('cmd_vel', Twist , queue_size=1) #versturen van bericht 'cmd-vel' in de Twist message


#creeeren van een loop waarin hij de snelheid uitstuurt
while not rospy.is_shutdown():
	pub.publish(move)
	rate.sleep()
else:
	move.angular.z = 0
	move.linear.x = 0
```

###Simple Goal

```python
#!/usr/bin/env python
# license removed for brevity

#hierbij kan een coordinaat ingeven word waarnaar gereden kan worden

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client():
    print ("test")
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = -4
    goal.target_pose.pose.position.y = 2
    goal.target_pose.pose.orientation.w = 5.0

    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()

if __name__ == '__main__':
    try:
        rospy.init_node('SimpleGoal')
        result = movebase_client()
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
```

###Multiple Goals

```python
#!/usr/bin/env python
# license removed for brevity

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

#lijst van mogelijke doelen waaruit de gebruiker kan kiezen
Kamer_1 = "Kamer 1"
Kamer_2 = "Kamer 2"
Kamer_3 = "Kamer 3"
Kamer_4 = "Kamer 4"
Kamer_5 = "Kamer 5"
Kamer_6 = "Kamer 6"
#andere variabelen declareren
path = []
GO = "GO"
x = "counter"
#creeeren van een loop om een traject te vragen aan de gebruiker
while x != GO:
    try:
        x = input("Geef Kamer_X in, GO voor te starten: ")
        path.append(x)
    except NameError:
        print ("Deze kamer bestaat niet, probeer opnieuw!")
    print(path) #controle

#functie om de doelen te verzenden
def movebase_client():
    index = 0
    while not rospy.is_shutdown():
        client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        client.wait_for_server()
        goal = traject(path[index])
        index += 1
        client.send_goal(goal)
        wait = client.wait_for_result()
        if len(path) == index:
            print ("All Goals Reached!")
            exit()

#locaties van de verschillende kamers op de kaart van Rviz
def traject(kamer):
    goal = MoveBaseGoal() #gebruik maken van bestaande message file in ROS
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    if kamer == Kamer_1:
        goal.target_pose.pose.position.x = 5
        goal.target_pose.pose.position.y = 2
        goal.target_pose.pose.orientation.w = 1.0

    if kamer == Kamer_2:
        goal.target_pose.pose.position.x = 6
        goal.target_pose.pose.position.y = -2
        goal.target_pose.pose.orientation.w = 1.0

    if kamer == Kamer_3:
        goal.target_pose.pose.position.x = 1
        goal.target_pose.pose.position.y = 3
        goal.target_pose.pose.orientation.w = 1.0

    if kamer == Kamer_4:
        goal.target_pose.pose.position.x = -3
        goal.target_pose.pose.position.y = 2
        goal.target_pose.pose.orientation.w = 1.0

    if kamer == Kamer_5:
        goal.target_pose.pose.position.x = -6
        goal.target_pose.pose.position.y = 3
        goal.target_pose.pose.orientation.w = 1.0

    if kamer == Kamer_6:
        goal.target_pose.pose.position.x = -7
        goal.target_pose.pose.position.y = -3
        goal.target_pose.pose.orientation.w = 1.0

    print(kamer, goal)
    return goal #resultaat van de functie 'traject'


if __name__ == '__main__':
    try:
        rospy.init_node('SimpleGoalV2') #maken van een nieuwe node
        result = movebase_client() #het resultaat van de functie in een veriabele steken
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
```



