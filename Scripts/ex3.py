import subprocess as sp

sp.call(["ffmpeg",
         "-stream_loop", "-1",
         "-i", "./videos/alan.mp4",
         "-deinterlace",
         "-vcodec", "libx264",
         "-pix_fmt", "yuv420p",
         "-preset", "medium", "-r", "30",
         "-g", "60", "-b:v", "2500k",
         "-acodec", "libmp3lame",
         "-ar", "44100",
         "-threads", "6",
         "-qscale", "3",
         "-b:a", "712000",
         "-bufsize", "512k",
         "-f", "flv",
         "rtmp://a.rtmp.youtube.com/live2/ggk1-jg93-kbqj-acgj-1hjq"])
