# Auxcast

Based on [this tutorial](https://dupontgu.medium.com/how-to-stream-your-record-player-throughout-your-home-for-cheap-fb044368a240) by Guy Dupont. Instead of using an app for casting however, I added a button to the Pi which uses Go-Chromecast to cast the stream to my chromecast-group, which contains both a Chromecast and a smartspeaker.

<h2>Hardware:</h2>

+ Any Rasberry Pi as i tested this on a very old 1B<br/>
+ A USB dac, The [Behringer UFO202](https://www.behringer.com/behringer/product?modelCode=P0A12) works well for turntables.

<h2>Software:</h2>

[Darkice](http://www.darkice.org/)<br/>
[Icecast2](https://icecast.org/)<br/>
[Go-chromecast](https://github.com/vishen/go-chromecast/blob/master/README.md)<br/>
[Auxcast](https://github.com/JanTijhof/Auxcast)


<h2>Instructions:</h2>
Start with setting up a Raspberry pi with Linux distro and network connection.

+ Wire up two momentary NO buttons. One from GPIO3 to GND (shutdown) and the other from GPIO4 to GND (cast button)

<h3>Set up the streaming software</h3>

Make sure the raspberry is up to date with: 
````
sudo apt-get update
sudo apt-get upgrade
````

No need for custom built packages as most tutorials instruct. Darkice 1.3 and higher have mp3 support built in.
Install Darkice and Icecast 2
````
sudo apt-get install icecast2 darkice
````
For now we can skip the Icecast configuration, as we will copy those settings in. If you'd rather configure everything yourself, it's possible to use [these](https://maker.pro/raspberry-pi/projects/how-to-build-an-internet-radio-station-with-raspberry-pi-darkice-and-icecast), or [these](https://circuitdigest.com/microcontroller-projects/raspberry-pi-internet-radio-and-streaming-station) instructions.
Both Darkice and Icecast configurations are included in this repo and can be cloned with:
````
git clone https://github.com/JanTijhof/Auxcast
sudo cp /Auxcast/darkice.cfg /etc/darkice.cfg
sudo cp /Auxcast/icecast.xml /etc/icecast2/icecast.xml
````

Add both to the startup script of your raspberry by opening rc.local
````
sudo nano /etc/rc.local
````
Add these lines
````
sudo nano icecast2&
sleep 5
sudo nano darkice -c /etc/darkice.cfg&
````

Now to finish our installing process, reboot the system. 
````
sudo reboot
````

Then get the IP address of your raspberry with
````
ifconfig
````

From any other device you should now be able to access your stream at port 8000 of this address.
for example 192.168.1.5:8000

<h3>Set up casting</h3>

Install Go ([instructions](https://linuxhint.com/2-methods-install-go-raspberry-pi/))
Then instal Go-chromecast

If everything is running wel, plug in your Aux source and test your setup.<br/>
replace "Muziek" with the Google casting device/group you're targeting and the IP with yours.
````
go-chromecast -n 'Muziek' load 'http://192.168.1.169:8000/turntable.mp3'
````

<h3>Scripts for buttons</h3>

When casting is working, install the script for the buttons by running the following SSH command:
````
git clone https://github.com/JanTijhof/Auxcast/

./Auxcast/scripts/install
````
That should be it! Enjoy your Music! 🎶
