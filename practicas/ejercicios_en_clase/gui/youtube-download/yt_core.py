from pytube import YouTube

CARPETA = "./"
RICK_VIDEO = 'https://www.youtube.com/watch?v=GtL1huin9EE'

class DurationError(Exception):
    pass

def duration_check(link):
    yt = YouTube(link)
    if yt.length > 600: # si el video dura mas de 10 segundos.
        # Se pone esta limitación para que no se descarguen archivos tan largos que pueden llegar a colgar el programa
        raise DurationError("Duration error! Video muy largo")
    return yt

def downloader(video, path='./'):
    try:
        video.download(path)
        print("Descargado!")
    except Exception as e:
        raise e

    
def download_video(link, path='./'):
    try:
        yt = duration_check(link)    
        tags = yt.streams.get_highest_resolution()
        d_video = yt.streams.get_by_itag(tags.itag)
        downloader(d_video, path)
    except Exception as e:
        raise e

def download_audio(link, path='./'):
    try:
        yt = duration_check(link)
        d_video=yt.streams.filter(only_audio=True).first()
        downloader(d_video, path)
    except Exception as e:
        raise e


if __name__ == '__main__':
    download_video(RICK_VIDEO, CARPETA)