from pytube import YouTube

CARPETA = "./"

def download_video(link):
    try:
        yt = YouTube(link)
        tags = yt.streams.get_highest_resolution()
        d_video = yt.streams.get_by_itag(tags.itag)
        d_video.download(CARPETA)
        print("Descargado!")
    except Exception as e:
        raise e

def download_audio(link):
    try:
        d_video=yt.streams.filter(only_audio=True).first()
        d_video.download(CARPETA)
        print("Descargado!")
    except Exception as e:
        raise e


if __name__ == '__main__':
    rick_video = 'https://www.youtube.com/watch?v=mCdA4bJAGGk'
    download_video(rick_video)