import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        # загружаем все wav файлы из папки sample_tracks
        self.music_folder = "music/sample_tracks"
        self.playlist = [f for f in os.listdir(self.music_folder) if f.endswith(".wav")]
        self.current = 0
        self.is_playing = False

    def play(self):
        if self.playlist:
            track_path = os.path.join(self.music_folder, self.playlist[self.current])
            pygame.mixer.music.load(track_path)
            pygame.mixer.music.play()
            self.is_playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        if self.playlist:
            self.current = (self.current + 1) % len(self.playlist)
            self.play()

    def prev_track(self):
        if self.playlist:
            self.current = (self.current - 1) % len(self.playlist)
            self.play()

    def get_current_track_name(self):
        if self.playlist:
            return self.playlist[self.current]
        return "No tracks"