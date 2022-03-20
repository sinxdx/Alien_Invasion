
class GameStats:
    """用于储存游戏数据"""
    def __init__(self, setting):
        """初始化统计信息"""
        self.setting = setting
        self.ship_left = self.setting.ship_limit
        self.game_active = False  # 当该值为False后，游戏结束

    def reset_stats(self):
        self.ship_left = self.setting
