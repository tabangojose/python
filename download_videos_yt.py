from pytube import YouTube

# URL del video de YouTube a descargar
url = 'https://www.youtube.com/watch?v=uKStJftNAAw'

# Crea un objeto YouTube
yt = YouTube(url)

# Descarga el video en la máxima resolución disponible
video = yt.streams.get_highest_resolution().download()

# Descarga los subtítulos en inglés
subtitles = yt.captions.get_by_language_code('en')
if subtitles:
    subtitles = subtitles.generate_srt_captions()
    with open(yt.title + '.en.srt', 'w') as f:
        f.write(subtitles)