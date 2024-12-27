import os
from pytube import YouTube, Playlist
from pydub import AudioSegment

def download_video(video_url, output_folder):
    yt = YouTube(video_url)
    print(f"Downloading: {yt.title}")
    audio_stream = yt.streams.filter(only_audio=True).first()
    out_file = audio_stream.download(output_path=output_folder)
    base, ext = os.path.splitext(out_file)
    mp3_file = f"{base}.mp3"

    AudioSegment.from_file(out_file).export(mp3_file, format="mp3")
    os.remove(out_file)  
    print(f"Downloaded and converted: {yt.title} -> {mp3_file}")

def download_playlist(playlist_url, output_folder):
    playlist = Playlist(playlist_url)
    print(f"Found playlist: {playlist.title}")
    print(f"Total videos: {len(playlist.video_urls)}")
    
    for video_url in playlist.video_urls:
        try:
            download_video(video_url, output_folder)
        except Exception as e:
            print(f"Error downloading {video_url}: {e}")

def main():
    print("YouTube to MP3 Downloader")
    choice = input("Do you want to download a (1) single video or (2) playlist? Enter 1 or 2: ")
    
    if choice == "1":
        video_url = input("Enter the YouTube video URL: ")
        output_folder = input("Enter the output folder path: ")
        os.makedirs(output_folder, exist_ok=True)
        download_video(video_url, output_folder)
    elif choice == "2":
        playlist_url = input("Enter the YouTube playlist URL: ")
        output_folder = input("Enter the output folder path: ")
        os.makedirs(output_folder, exist_ok=True)
        download_playlist(playlist_url, output_folder)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
