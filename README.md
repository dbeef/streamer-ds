# streamer-ds
Capturing desktop and streaming it to NDS 

<p align="center">
<img src="https://github.com/dbeef/streamer-ds/blob/master/readme/cropped_128.gif" alt="128px streaming"
 width="240" height="340">
<img src="https://github.com/dbeef/streamer-ds/blob/master/readme/cropped_256.gif" alt="256px streaming"
 width="240" height="340">


<ul>
<li>https://www.youtube.com/watch?v=ESSFMSbR2Kw</li>
<li>https://www.youtube.com/watch?v=Z8DLfSR5GKQ</li>
</ul>

<h2 align="center">Dependencies</h2>
<ul>
 <li>linux</li>
<li>DevkitPro, easiest way to download it is through pacman: https://devkitpro.org/wiki/Getting_Started</li>
</ul>


<h2 align="center">Usage</h2>

<ul>
 
 <li> create hotspot on your laptop </li>
 <li> run .nds file on your NDS </li>
 <li> connect to your hotspot on your NDS via the .nds file </li>
 <li> run the python script: desktop_client.py </li> 
 
 
</ul>


<h2 align="center">How it works</h2>

<ul>
<li>NDS opens port 8080, python script connects PC to it, then:</li>
  <ul>
    <li> python makes screenshot,</li>  
    <li> resizes it to 256px or 128px (depends how smooth transmition you want - 256px takes ~ 0.6s on frame, 128px - ~0.3s)</li>  
    <li> calls grit to make a 16 bit, lz77 compressed raw binary version</li>  
    <li> sends image size to the NDS</li>  
    <li> sends image</li>  
    <li> receives ACK character from NDS</li>  
    <li> repeat</li>  
    </ul>
</ul>

<h2 align="center">How to make WIFI hotspot that NDS can connect (it's not that obvious):</h2>

<ul>
<li>in Ubuntu open "Network Connections" and click "add new"</li>
<li>go to the "Wi-Fi security" - NDS supports only WEP security (so remember, it's dangerous to beacon that poorly secured network all the time, use this hotspot only when playing with your NDS) - select "WEP 40/128 bit key (Hex or ASCII)" </li>
 <li> select some random 5 character (only digits) password </li>
 <li> in "Wi-Fi" tab select "Mode" to "Hotspot" </li>
 <li> save it </li>
 <li> open "Network" </li>
 <li> click "Connect to to a hidden network" </li>
 <li> select network that you've just created (by default its name will be "hotspot")
 <li> you're done, if you were previously connected with another network via wifi you'll be disconnected</li>
 <li> now you can connect to this network through your NDS </li>
</ul>

<h2 align="center">Performance:</h2>
<p> Well... as it's only sending lz77 compressed bitmaps through the network, you won't be suprised that for a 2004 portable console that much of bytes will be a shock therapy. On average it's somewhere between 10-20 kB per 256px frame and 5-10 per 128px frame. Every frame must be decompressed on NDS (it has a dedicated hardware for that so it's not that bad in this task) and that's the thing that takes most of the time (around 2/3 of frame time). I tried sending non-compressed bitmaps but it took around 80kB per each and it took even more time (this time the WiFi capabilities of the NDS were the bottleneck). </p>

<p align="center"> <a href="https://raw.githubusercontent.com/dbeef/streamer-ds/master/readme/all_parameters_500.png"> Click to see details</a>
<img src="https://github.com/dbeef/streamer-ds/blob/master/readme/all_parameters_500.png" alt="Efficiency"
 width="2500" height="200">

<h2 align="center">FAQ</h2>

<ul>
<li>Can I control my desktop through this app?</li>
 <ul>
<li> You could do it, I even created one version that you can access on this video:</li>
<li>https://www.youtube.com/watch?v=WR8Y4Iro9t0</li>
<li> ...but it's almost no use because I can't utilize multiple threads on NDS so capturing input will occure every frame - that means it will happen every ~0.3 second - so it's basically garbage.</li>
<li> If you're interested only in capturing key input (without the video part), I created another program:</li>
 <li>https://github.com/dbeef/controller-ds</li> 
 </ul>
 </ul>
