

class AudioFile:

    def __init__(self, filename):

        if not filename.endswith(self.ext):
            raise Exception ('Formato Inválido!')
        self.filename = filename
    pass

class MP3File(AudioFile):

    ext = 'mp3'


f = MP3File('flamingos.wav')
