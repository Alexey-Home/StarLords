class Stats():
    """отслеживание статиски"""

    def __init__(self):
        """иниицилизирует статистику"""
        self.reset_stats()
        self.run_game = True
        with open("highscore.txt", "r") as f:
            self.high_score = int(f.readline())


    def reset_stats(self):
        """статистика, изменяющаяся во врмея игры"""
        self.guns_left = 2
        self.score = 0