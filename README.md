#  YTD-Interface (MP3/MP4)

A simple, dark-themed YouTube downloader with a modern UI using `customtkinter`, `yt_dlp`, and `ffmpeg`.

Download YouTube videos as **MP4** (video) or **MP3** (audio only) with customizable quality or bitrate, and a user-friendly interface.

---

##  Features

-  Download YouTube videos in **MP3** or **MP4**
-  Select audio bitrate for MP3: `128`, `192`, `256`, `320`
-  Choose video quality for MP4: `720p`, `1080p`, `4K`
-  Auto-opens downloads folder after completion
-  Dark-mode GUI built with `customtkinter`

---

## Requirements

- Python 3.10 or newer
- `ffmpeg` binary (included in packaged EXE)
- Python packages:
  ```bash
  pip install yt-dlp customtkinter

## Run the Script (Developer Mode)
#Clone or download the repo.

#Download ffmpeg static build and place ffmpeg.exe in ffmpeg/bin/

Run the script:
`python main.py`

YouTubeDownloader/
│
├── main.py
├── icon.ico                # (optional) app icon
├── ffmpeg/
│   └── bin/
│       └── ffmpeg.exe      # required


## Build EXE (Windows)
Use PyInstaller to convert to a standalone .exe:

# 1. Install PyInstaller
`pip install pyinstaller`

# 2. Build the app

pyinstaller --noconsole --onefile ^ --add-data "ffmpeg;ffmpeg" ^ --icon=icon.ico ^ main.py // FFMpeg/bin/ then the exes must be in the same directory

After building, your EXE will be in the dist/ folder.

## Distribute
Distribute the EXE alone, or zip the contents of the dist/ folder and share.

No Python installation needed by the user.

## Customization
To rename the app, rename main.py and update the PyInstaller command

You can adjust default quality/bitrate in the code

## Troubleshooting
Problem	Solution
GUI doesn't open	Make sure --noconsole was used

ffmpeg not found	Ensure ffmpeg/bin/ffmpeg.exe exists and is included via --add-data

Downloads fail	Validate the YouTube URL and internet connection

If anymore issues arrive make a request on my github or message me on discord 

wxwefr or blight.dev
