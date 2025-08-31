from core.game import Game
from core.menu import Menu, HighScoreView, GameOverView
from core.sound_manager import SoundManager

if __name__ == "__main__":
    jogo = Game()
    sound_manager = SoundManager()
    state = "menu"
    menu = Menu(jogo.screen)
    score = 0
    while True:
        if state == "menu":
            sound_manager.play_music()
            state = menu.run()
        elif state == "play":
            sound_manager.play_music()
            state, score = jogo.run(menu.difficulty)
        elif state == "highscore":
            state = HighScoreView(jogo.screen).run(menu.difficulty)
        elif state == "gameover":
            sound_manager.play_sound('gameover')
            state = GameOverView(jogo.screen, score).run(menu.difficulty)
        elif state == "quit":
            jogo.quit()