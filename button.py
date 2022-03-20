import pygame.font


class Button:
    def __init__(self, screen, msg) -> object:
        """初始化按键属性
        :rtype: object
        """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        '''设置按键尺寸、颜色、文本颜色'''
        self.width = 200
        self.height = 50
        self.button_colour = (255, 255, 0)
        self.text_color = (255, 255, 255)  # 黑色
        self.font = pygame.font.SysFont(None, 48)  # font = 字体
        """创建按钮的rect对象，同时使其在屏幕居中"""
        self.rect = pygame.Rect(0, 0, self.width, self.height)  # 调用pygame中的Rect类创建该对象
        self.rect.center = self.screen_rect.center
        '''创建按钮标签'''
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将msg渲染为图像，然后在按钮上居中"""
        self.msg_image = self.font.render(msg, True, self.text_color,  # font_render将文本转为图像
                                          self.button_colour)         # 后面的True是抗锯齿
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """在屏幕上绘制按键"""
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)