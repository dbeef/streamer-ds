# streamer-ds
Capturing desktop and streaming it to NDS 

https://www.youtube.com/watch?v=WR8Y4Iro9t0
https://www.youtube.com/watch?v=ESSFMSbR2Kw
https://www.youtube.com/watch?v=Z8DLfSR5GKQ

How it works:

NDS opens port 8080, python script connects PC to it, then:
  python makes screenshot,
  resizes it to 256px or 128px (depends how smooth transmition you want - 256px takes ~ 0.6s on frame, 128px - ~0.3s)
  calls grit to make a 16 bit, lz77 compressed raw binary version
  sends image size to the NDS
  sends image
  receives ACK character from NDS
  repeat
  
How to make WIFI connection with NDS (it's not that obvious):
  
