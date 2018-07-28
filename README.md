# streamer-ds
Capturing desktop and streaming it to NDS 

<p align="center">
<img src="https://github.com/dbeef/streamer-ds/blob/master/readme/cropped_128.gif" alt="128px streaming"
 width="240" height="340">
<img src="https://github.com/dbeef/streamer-ds/blob/master/readme/cropped_256.gif" alt="256px streaming"
 width="240" height="340">


<ul>
<li>https://www.youtube.com/watch?v=WR8Y4Iro9t0</li>
<li>https://www.youtube.com/watch?v=ESSFMSbR2Kw</li>
<li>https://www.youtube.com/watch?v=Z8DLfSR5GKQ</li>
</ul>

<h2 align="center">Dependencies</h2>
<ul>
 <li>linux</li>
<li>DevkitPro, easiest way to download it is through pacman: https://devkitpro.org/wiki/Getting_Started</li>
</ul>

<h2 align="center">How it works:</h2>

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

<h2 align="center">How to make WIFI connection with NDS (it's not that obvious):</h2>
  

  
