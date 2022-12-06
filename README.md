# P3_SCAV

## Exercise 1
### Statement
Create a script which it will invoke FFMPEG to create a HLS transport stream container with one
video you already have. No DRM needed. 

If you’re one of the cool guys/girls or do you want to learn, try to inherit from old exercises you’ve delivered with super().
### Comments

The script can be found at the `Scripts` folder as `ex1.py`. It should be executed from the general folder `P3_SCAV` with the command `python3 Scripts/ex1.py`.

I have note implemented the inheritance part.
## Exercise 2
### Statement
Download the bento4 tools and use them to create a MPD video file with any encryption you want. You’ll need to fragment, encrypt and dash the file.
Feel free if you want to try to decrypt, or open from a player… whatever you do, just explain your way into this. If not, just create a script that will do

### Comments
I could not do this exercise because I had problems installing Bento4.
## Exercise 3
### Statement
Create a script to livestream with ffmpeg (any protocol you want) and open it from mobile or any other device in the same network.
### Comments
The script can be found at the `Scripts` folder as `ex3.py`. It has been executed from the general folder `P3_SCAV` with the command `python3 Scripts/ex3.py`. If you change the link and key should work for you too.

To create the streaming I requested YouTube the option to stream on my channel. After waiting 24h I could generate an streaming. From here I could get the RTMP link and the needed key to connect from ffmpeg.

![alt text](https://github.com/juliatogr/P3_SCAV/blob/main/screenshots/ex3/live_config_youtube.PNG?raw=true)

Afterwards, I executed the script and I saw an output at the terminal like this:

![alt text](https://github.com/juliatogr/P3_SCAV/blob/main/screenshots/ex3/terminal_output.PNG?raw=true)

Finally, I could reproduce the stream on my cellphone.

![Alt Text](https://github.com/juliatogr/P3_SCAV/main/screenshots/ex3/Screen_Recording_YouTube.gif?raw=true)

## Exercise 4
### Statement
Connect to your favorite streaming show (doesn’t matter the platform). Open developer tools, check network and click ‘play’ to watch the video.
Please document with screenshots and try to identify if it’s HLS or DASH, which browser where you using… try to ffmpeg a chunk or the master and
tell us the encoding in case you were able to.
### Comments

I connected to a streaming of KaiCenat on Twitch from Microsoft Edge navigator. Then, I pressed F12 to init the DevTools and got the next result.

![alt text](https://github.com/juliatogr/P3_SCAV/blob/main/screenshots/ex4/DevTools.png?raw=true)

On the URL I can see how they are using HLS.

Afterwards, I ffmpeg the link of the streaming and got the next output.

![alt text](https://github.com/juliatogr/P3_SCAV/blob/main/screenshots/ex4/ffmpeg_master.PNG?raw=true)

Here I see that the encoder is `Lavf57.71.100`.
## Util links

- *HLS Packaging using FFmpeg – Easy Step-by-Step Tutorial* https://ottverse.com/hls-packaging-using-ffmpeg-live-vod/

- *Live Stream to YouTube using FFMPEG & Looping the video* https://www.youtube.com/watch?v=7jWgyJgGKf8
