import tkinter as tk
from tkinter import ttk, filedialog
from pytube import YouTube
# import threading


def url_tag():
    # Get URL of video from text`s field
    video_url = url_entry.get()

    try:
        video_url = YouTube(video_url)
        # Get resolution from list
        selected_resolution = resolution_combobox.get()
        # Using method get_by_resolution() with selected resolution
        stream = video_url.streams.get_by_resolution(selected_resolution)

        if audio.get():
            stream = video_url.streams.filter(only_audio=True).first()

        # Opening dialogue window for choice folder to save file
        save_path = filedialog.askdirectory()
        if save_path:
            stream.download(save_path)
            status_label.config(text='Media was download successful!')
    except Exception as e:
        status_label.config(text='Huston we have a problem: ' + str(e))

    # Creating a thread for  downloading the video
    # download_thread = threading.Thread(target=download)
    # download_thread.start()


def past_text(event=None):
    """This function  is realize opportunity past of text in URL-field"""
    clipboard_text = root.clipboard_get()
    url_entry.delete(0, tk.END)
    url_entry.insert(0, clipboard_text)


# Creating GUI
root = tk.Tk()
root.title('YouTube Downloader')

# Defining window size
window_width = 400
window_height = 200

# Getting screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculating x and y coordinates for the Tk root window
x = (screen_width/2) - (window_width/2)
y = (screen_height/2) - (window_height/2)

# Setting the window to appear in the center of the screen
root.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))

# Creating text field for URL
url_label = tk.Label(root, text='Entry URL:')
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Creating menu for choice of resolution video
resolutions = ["720p", "480p", "360p"]  # List of available resolution
resolution_combobox = ttk.Combobox(root, values=resolutions, state='readonly')
resolution_combobox.current(0)  # Set default variant
resolution_combobox.pack()

# Checkbox for choice only audio file
audio = tk.BooleanVar()
audio_check = tk.Checkbutton(root, text='Download audio (mp3)', variable=audio)
audio_check.pack()

# Button for download video
download_button = tk.Button(root, text='Download', command=url_tag)
download_button.pack()

# Label for status of download
status_label = tk.Label(root, text='')
status_label.pack()

# Progress bar
progress = ttk.Progressbar(root, orient='horizontal', mode='indeterminate')
progress.pack()

# Add function for paste text from clipboard to URL-field
# url_entry.bind('<Control-v>', lambda event: url_entry.event_generate('<Paste>'))
root.bind('<Control-V>', past_text)

# Run main cycle
root.mainloop()
