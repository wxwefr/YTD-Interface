import customtkinter as ctk
import yt_dlp as youtube_dl
import os
import sys
import subprocess
import tkinter.messagebox as messagebox  # Import tkinter's messagebox

# Set customtkinter appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def resource_path(relative_path):
    """Get absolute path to resource (for PyInstaller)."""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Setup download folder
if getattr(sys, 'frozen', False):
    base_folder = os.path.dirname(sys.executable)
else:
    base_folder = os.path.abspath(".")

downloads_folder = os.path.join(base_folder, "Downloads")
os.makedirs(downloads_folder, exist_ok=True)

def update_interface(event=None):
    format_choice = format_var.get()

    if format_choice == 'MP3':
        quality_label.pack_forget()
        quality_dropdown.pack_forget()
        bitrate_label.pack(pady=(10, 0))
        bitrate_dropdown.pack(pady=(5, 10))
    else:
        bitrate_label.pack_forget()
        bitrate_dropdown.pack_forget()
        quality_label.pack(pady=(10, 0))
        quality_dropdown.pack(pady=(5, 10))

def download_content():
    url = url_entry.get()
    format_choice = format_var.get()

    if not url:
        messagebox.showwarning(title="Input Error", message="Please enter a valid YouTube URL")
        return

    ffmpeg_path = resource_path('ffmpeg/bin')

    ydl_opts = {
        'ffmpeg_location': ffmpeg_path,
        'outtmpl': os.path.join(downloads_folder, '%(title)s.%(ext)s'),
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True
    }

    if format_choice == 'MP3':
        bitrate_choice = bitrate_var.get()
        ydl_opts['format'] = 'bestaudio/best'
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': bitrate_choice,
        }]
    else:
        quality_choice = quality_var.get()
        if quality_choice == '4K':
            ydl_opts['format'] = 'bestvideo[height>=2160]+bestaudio/best'
        elif quality_choice == '1080p':
            ydl_opts['format'] = 'bestvideo[height>=1080]+bestaudio/best'
        elif quality_choice == '720p':
            ydl_opts['format'] = 'bestvideo[height>=720]+bestaudio/best'

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo(title="Success", message="Download completed successfully!")
        subprocess.Popen(f'explorer "{downloads_folder}"')
    except Exception as e:
        messagebox.showerror(title="Error", message=f"An error occurred: {str(e)}")

# Build the UI
root = ctk.CTk()
root.title("YouTube Downloader")
root.geometry("460x500")

# Fonts
title_font = ctk.CTkFont(size=18, weight="bold")
text_font = ctk.CTkFont(size=14)

# Main Frame
frame = ctk.CTkFrame(root)
frame.pack(padx=20, pady=20, fill="both", expand=True)

# URL
url_label = ctk.CTkLabel(frame, text="Enter YouTube URL:", font=title_font)
url_label.pack(pady=(10, 5))

url_entry = ctk.CTkEntry(frame, width=400, font=text_font)
url_entry.pack(pady=(0, 10))

# Format selection
format_label = ctk.CTkLabel(frame, text="Select Format:", font=title_font)
format_label.pack(pady=(10, 5))

format_var = ctk.StringVar(value="MP4")
format_dropdown = ctk.CTkOptionMenu(frame, variable=format_var, values=["MP3", "MP4"], command=update_interface)
format_dropdown.pack(pady=(0, 10))

# Bitrate options
bitrate_label = ctk.CTkLabel(frame, text="Select Audio Bitrate (MP3):", font=title_font)
bitrate_var = ctk.StringVar(value="192")
bitrate_dropdown = ctk.CTkOptionMenu(frame, variable=bitrate_var, values=["128", "192", "256", "320"])

# Quality options
quality_label = ctk.CTkLabel(frame, text="Select Video Quality (MP4):", font=title_font)
quality_var = ctk.StringVar(value="1080p")
quality_dropdown = ctk.CTkOptionMenu(frame, variable=quality_var, values=["4K", "1080p", "720p"])

# Download Button
download_button = ctk.CTkButton(frame, text="Download", font=text_font, command=download_content, width=200)
download_button.pack(pady=30)

# Initialize UI
update_interface()

root.mainloop()
