from pytube import Playlist, YouTube
import os
import sys

def download_progress(stream, chunk, bytes_remaining):
    # Calculate the percentage of the downloaded file
    bytes_downloaded = stream.filesize - bytes_remaining
    progress = (bytes_downloaded / stream.filesize) * 100
    sys.stdout.write(f"\rDownloading... {progress:.1f}%")
    sys.stdout.flush()

def download_video(url, save_path='./'):
    try:
        playlist = Playlist(url)
        print(f"Playlist Title: {playlist.title}")
        
        for video_url in playlist.video_urls:
            yt = YouTube(video_url)
            video = yt.streams.filter(res="720p").first()

            # Get the file size of the video
            file_size = video.filesize / (1024 * 1024) # Convert bytes to MB
            print(f"File size: {file_size:.2f} MB")

            # Prompt the user to start the download
            #input("Press Enter to start the download... (Press Esc to cancel)")

            # Start downloading the video
            video.download(save_path)
            print("\nDownload completed successfully!")
    except KeyboardInterrupt:
        print("\nDownload aborted.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

# Prompting the user to input the URL
playlist_url = input("Enter the YouTube playlist URL: ")
download_video(playlist_url, save_path='./')
