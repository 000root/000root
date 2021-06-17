'''配置文件'''
import os


'''屏幕大小'''
SCREENSIZE = (1200, 800)
'''游戏素材'''
BGMPATH = os.path.join(os.getcwd(), 'resources/audios/bgm.wav')
HEROPICPATH = os.path.join(os.getcwd(), 'resources/images/hero.png')
'''FPS'''
FPS = 20
'''块大小'''
BLOCKSIZE = 20#15
MAZESIZE = (20, 35) # num_rows * num_cols(35,50)
BORDERSIZE = (25, 50) # 25 * 2 + 50 * 15 = 800, 50 * 2 + 35 * 15 = 625