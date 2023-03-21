import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

font_dirs = ['/usr/share/fonts', ]
font_files = font_manager.findSystemFonts(fontpaths=font_dirs)

for font_file in font_files:
    font_manager.fontManager.addfont(font_file)

# 列出所有可用字体
print(font_manager.fontManager.ttflist)

