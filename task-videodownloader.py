from pytube import YouTube

def download_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        video.download()
        print("Downloading video... Done!")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    video_url = input("Enter the video URL: ")
    download_video(video_url)

if __name__ == "__main__":
    main()
