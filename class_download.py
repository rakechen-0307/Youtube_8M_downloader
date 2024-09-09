import os

## latin, funk, rock, EDM, pop, R&B, country, hip-hop
ytids = ["kJQP7kiw5Fk", "6Mgqbai3fKo", 
         "OPf0YbXqDm0", "gB4kaf9bVQE",
         "8sgycukafqQ", "r8OipmKFDeM",
         "qPTfXwPf_HM", "mt1mXwBLsSE",
         "o1sUaVJUeB0", "90xQdZ4WmLA",
         "7L06_HW_HcA", "o3IWTfcks4k",
         "MLhYghzNfII", "1vrEljMfXYo",
         "XbGs_qK2PQA", "H58vbez_m4E"]
video_dir = "./class_video"

os.mkdir(video_dir)
for i in range(len(ytids)):
    os.system("yt-dlp --extract-audio --audio-format mp3 {}".format(
        "https://www.youtube.com/watch?v=" + ytids[i]   
    ))