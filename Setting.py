class Settings:
    """一种用来保存游戏设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800  # pygame中，屏幕的原点在左上角，而按照右边的设置，屏幕的右下角将设为（1200,800）
        self.background_colour = (230, 230, 230)
        '''自机设置'''
        self.ship_limit = 1  # 生命值
        self.ship_speed_factor = 1.5
        '''子弹设置'''
        self.bullet_speed_factor = 1
        self.bullet_color = (60, 60, 60)
        self.bullet_width = 3
        self.bullet_height = 3
        self.bullet_maxnum = 10  # 子弹最大允许数量
        # 下面是debug专用子弹的设置
        self.bullet_debug_width = 1000
        '''敌机设置'''
        self.screen_reserve_space = 50  # 屏幕两侧以及顶端预留的宽度
        self.alien_reserve_space = 50  # 外星人与外星人之间预留的宽度
        self.alien_speed_factor = 0.25  # 外星人速度设置
        self.alien_line = 1  # 要创建的外星人行数
        '''过关后加速的比例'''
        self.speed_up_scale = 1.1

    def increase_speed(self):
        """提高游戏速度"""
        # self.ship_speed_factor *= self.speed_up_scale
        # self.bullet_speed_factor *= self.speed_up_scale
        self.alien_speed_factor *= self.speed_up_scale
