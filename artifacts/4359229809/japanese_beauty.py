#!/usr/bin/env python3
"""
生成日本美女插畫的 Python 腳本
使用 Pillow 库繪製日式風格的女性人物
"""

from PIL import Image, ImageDraw, ImageFilter
import numpy as np
import random

# 設定畫布大小
WIDTH, HEIGHT = 800, 1200
BACKGROUND_COLOR = (248, 244, 236)  # 溶紙色

# 顏色定義
COLORS = {
    'skin': (255, 218, 195),
    'skin_shadow': (240, 180, 150),
    'skin_highlight': (255, 235, 220),
    'hair': (25, 20, 30),
    'hair_highlight': (50, 45, 55),
    'eye': (40, 25, 15),
    'eye_iris': (120, 80, 50),
    'lip': (220, 100, 120),
    'kimono_red': (200, 40, 60),
    'kimono_red_shadow': (150, 20, 40),
    'kimono_red_highlight': (240, 80, 100),
    'kimono_black': (20, 15, 10),
    'obi_gold': (220, 180, 80),
    'obi_gold_highlight': (250, 220, 120),
    'obi_gold_shadow': (180, 140, 50),
    'sakura_pink': (255, 200, 220),
    'sakura_white': (255, 250, 250),
    'akizome_red': (180, 30, 50),
}

def create_image():
    """建立基礎畫布"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)
    return img, draw

def draw_sakura_branch(draw, img, x, y, length, angle, depth=3):
    """繪製櫻花樹枝"""
    if depth <= 0:
        return
    
    # 計算終點
    end_x = x + length * np.cos(np.radians(angle))
    end_y = y - length * np.sin(np.radians(angle))
    
    # 繪製樹枝
    branch_width = max(2, length // 20)
    draw.line([(int(x), int(y)), (int(end_x), int(end_y))], fill=(80, 50, 30), width=int(branch_width))
    
    # 在樹枝上繪製櫻花
    num_flowers = max(1, int(length // 40))
    for i in range(num_flowers):
        pos = i / num_flowers
        fx = x + length * pos * np.cos(np.radians(angle))
        fy = y - length * pos * np.sin(np.radians(angle))
        draw_sakura_flower(draw, int(fx), int(fy))
    
    # 遞迴繪製分支
    if depth > 1:
        new_length = length * 0.7
        draw_sakura_branch(draw, img, int(end_x), int(end_y), int(new_length), angle - 20, depth - 1)
        draw_sakura_branch(draw, img, int(end_x), int(end_y), int(new_length), angle + 20, depth - 1)

def draw_sakura_flower(draw, x, y):
    """繪製單朵櫻花"""
    petal_radius = random.randint(15, 25)
    center_radius = 8
    
    # 繪製花瓣 (5片)
    for i in range(5):
        angle = i * 72 + random.uniform(-5, 5)
        petal_x = x + petal_radius * np.cos(np.radians(angle))
        petal_y = y - petal_radius * np.sin(np.radians(angle))
        
        # 花瓣形狀
        petal_points = [
            (int(x + center_radius * np.cos(np.radians(angle))), 
             int(y - center_radius * np.sin(np.radians(angle)))),
            (int(petal_x + 10 * np.cos(np.radians(angle + 90))), 
             int(petal_y - 10 * np.sin(np.radians(angle + 90)))),
            (int(petal_x), int(petal_y)),
            (int(petal_x + 10 * np.cos(np.radians(angle - 90))), 
             int(petal_y - 10 * np.sin(np.radians(angle - 90))))
        ]
        
        # 顏色變化
        color = COLORS['sakura_pink'] if random.random() > 0.3 else COLORS['sakura_white']
        draw.polygon(petal_points, fill=color)
    
    # 繪製花蕊
    draw.ellipse([(int(x - center_radius), int(y - center_radius)), 
                  (int(x + center_radius), int(y + center_radius))], 
                 fill=(255, 240, 180))
    draw.ellipse([(int(x - center_radius//2), int(y - center_radius//2)), 
                  (int(x + center_radius//2), int(y + center_radius//2))], 
                 fill=(255, 220, 100))

def draw_petals_falling(draw, img):
    """繪製飄落的花瓣"""
    num_petals = 150
    for _ in range(num_petals):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        size = random.randint(5, 15)
        
        # 花瓣形狀
        points = []
        for i in range(5):
            angle = i * 72 + random.uniform(-10, 10)
            radius = size * random.uniform(0.7, 1.0)
            points.append((
                int(x + radius * np.cos(np.radians(angle))),
                int(y - radius * np.sin(np.radians(angle)))
            ))
        
        color = COLORS['sakura_pink'] if random.random() > 0.4 else COLORS['sakura_white']
        draw.polygon(points, fill=color)

def draw_character(draw, img):
    """繪製日本女性人物"""
    # 人物位置
    head_x = WIDTH // 2
    head_y = HEIGHT // 4
    head_radius = 120
    
    # 繪製頭部
    draw.ellipse([(int(head_x - head_radius), int(head_y - head_radius)),
                  (int(head_x + head_radius), int(head_y + head_radius))],
                 fill=COLORS['skin'])
    
    # 繪製頭髮 (黑色長髮)
    hair_points = [
        (int(head_x - head_radius - 10), int(head_y - head_radius + 20)),
        (int(head_x - head_radius - 20), int(head_y - head_radius - 30)),
        (int(head_x + head_radius + 20), int(head_y - head_radius - 30)),
        (int(head_x + head_radius + 10), int(head_y - head_radius + 20)),
        (int(head_x + head_radius + 10), int(head_y + head_radius - 30)),
        (int(head_x + head_radius - 20), int(head_y + head_radius + 100)),
        (int(head_x - head_radius - 20), int(head_y + head_radius + 100)),
        (int(head_x - head_radius - 10), int(head_y + head_radius - 30)),
    ]
    draw.polygon(hair_points, fill=COLORS['hair'])
    
    # 頭髮亮部
    highlight_points = [
        (int(head_x - head_radius + 10), int(head_y - head_radius + 30)),
        (int(head_x - head_radius + 30), int(head_y - head_radius - 10)),
        (int(head_x + head_radius - 30), int(head_y - head_radius - 10)),
        (int(head_x + head_radius - 10), int(head_y - head_radius + 30)),
        (int(head_x + head_radius - 20), int(head_y + head_radius - 50)),
        (int(head_x + head_radius - 40), int(head_y + head_radius + 50)),
        (int(head_x - head_radius + 40), int(head_y + head_radius + 50)),
        (int(head_x - head_radius + 20), int(head_y + head_radius - 50)),
    ]
    draw.polygon(highlight_points, fill=COLORS['hair_highlight'])
    
    # 繪製臉部細節
    draw_face(draw, head_x, head_y, head_radius)
    
    # 繪製身體和和服
    draw_kimono(draw, head_x, head_y, head_radius)

def draw_face(draw, head_x, head_y, head_radius):
    """繪製臉部細節"""
    # 額頭
    forehead_y = head_y - head_radius + 40
    draw.ellipse([(int(head_x - 60), int(forehead_y - 10)),
                  (int(head_x + 60), int(forehead_y + 30))],
                 fill=COLORS['skin_highlight'])
    
    # 臉頰
    draw.ellipse([(int(head_x - 80), int(head_y - 20)),
                  (int(head_x - 20), int(head_y + 40))],
                 fill=COLORS['skin_shadow'])
    draw.ellipse([(int(head_x + 20), int(head_y - 20)),
                  (int(head_x + 80), int(head_y + 40))],
                 fill=COLORS['skin_shadow'])
    
    # 眼睛
    eye_y = head_y - 15
    eye_width = 40
    eye_height = 20
    
    # 左眼
    left_eye_x = head_x - 35
    draw.ellipse([(int(left_eye_x - eye_width//2), int(eye_y - eye_height//2)),
                  (int(left_eye_x + eye_width//2), int(eye_y + eye_height//2))],
                 fill=COLORS['eye'])
    # 眼白
    draw.ellipse([(int(left_eye_x - eye_width//2 + 5), int(eye_y - eye_height//2 + 3)),
                  (int(left_eye_x + eye_width//2 - 5), int(eye_y + eye_height//2 - 3))],
                 fill=(255, 255, 255))
    # 瞳孔
    draw.ellipse([(int(left_eye_x - 5), int(eye_y - 2)),
                  (int(left_eye_x + 5), int(eye_y + 2))],
                 fill=COLORS['eye_iris'])
    
    # 右眼
    right_eye_x = head_x + 35
    draw.ellipse([(int(right_eye_x - eye_width//2), int(eye_y - eye_height//2)),
                  (int(right_eye_x + eye_width//2), int(eye_y + eye_height//2))],
                 fill=COLORS['eye'])
    draw.ellipse([(int(right_eye_x - eye_width//2 + 5), int(eye_y - eye_height//2 + 3)),
                  (int(right_eye_x + eye_width//2 - 5), int(eye_y + eye_height//2 - 3))],
                 fill=(255, 255, 255))
    draw.ellipse([(int(right_eye_x - 5), int(eye_y - 2)),
                  (int(right_eye_x + 5), int(eye_y + 2))],
                 fill=COLORS['eye_iris'])
    
    # 眉毛
    eyebrow_y = head_y - 35
    draw.line([(int(head_x - 50), int(eyebrow_y)), (int(head_x - 20), int(eyebrow_y - 5))],
              fill=COLORS['hair'], width=3)
    draw.line([(int(head_x + 20), int(eyebrow_y)), (int(head_x + 50), int(eyebrow_y - 5))],
              fill=COLORS['hair'], width=3)
    
    # 鼻子
    nose_points = [
        (int(head_x), int(head_y - 5)),
        (int(head_x - 8), int(head_y + 15)),
        (int(head_x + 8), int(head_y + 15))
    ]
    draw.polygon(nose_points, fill=COLORS['skin_shadow'])
    
    # 嘴巴
    mouth_y = head_y + 25
    draw.ellipse([(int(head_x - 20), int(mouth_y - 5)),
                  (int(head_x + 20), int(mouth_y + 10))],
                 fill=COLORS['lip'])
    # 嘴巴亮部
    draw.ellipse([(int(head_x - 15), int(mouth_y - 3)),
                  (int(head_x + 15), int(mouth_y + 5))],
                 fill=(255, 150, 180))

def draw_kimono(draw, head_x, head_y, head_radius):
    """繪製和服"""
    body_top = head_y + head_radius
    body_bottom = HEIGHT - 100
    
    # 和服主體 (紅色)
    kimono_points = [
        (int(head_x - 150), int(body_top)),
        (int(head_x - 200), int(body_top + 200)),
        (int(head_x - 180), int(body_bottom)),
        (int(head_x + 180), int(body_bottom)),
        (int(head_x + 200), int(body_top + 200)),
        (int(head_x + 150), int(body_top)),
        (int(head_x + 150), int(body_top + 100)),
        (int(head_x + 100), int(body_top + 150)),
        (int(head_x + 50), int(body_top + 100)),
        (int(head_x), int(body_top)),
    ]
    draw.polygon(kimono_points, fill=COLORS['kimono_red'])
    
    # 和服陰影
    shadow_points = [
        (int(head_x - 150), int(body_top)),
        (int(head_x - 180), int(body_top + 150)),
        (int(head_x - 170), int(body_bottom)),
        (int(head_x + 170), int(body_bottom)),
        (int(head_x + 180), int(body_top + 150)),
        (int(head_x + 150), int(body_top)),
        (int(head_x + 150), int(body_top + 80)),
        (int(head_x + 80), int(body_top + 120)),
        (int(head_x + 40), int(body_top + 80)),
        (int(head_x), int(body_top)),
    ]
    draw.polygon(shadow_points, fill=COLORS['kimono_red_shadow'])
    
    # 和服亮部
    highlight_points = [
        (int(head_x - 100), int(body_top + 50)),
        (int(head_x - 130), int(body_top + 150)),
        (int(head_x - 120), int(body_bottom - 200)),
        (int(head_x + 120), int(body_bottom - 200)),
        (int(head_x + 130), int(body_top + 150)),
        (int(head_x + 100), int(body_top + 50)),
        (int(head_x + 100), int(body_top + 80)),
        (int(head_x + 50), int(body_top + 100)),
        (int(head_x), int(body_top + 50)),
    ]
    draw.polygon(highlight_points, fill=COLORS['kimono_red_highlight'])
    
    # 袖子
    sleeve_left = [
        (int(head_x - 150), int(body_top)),
        (int(head_x - 250), int(body_top + 50)),
        (int(head_x - 220), int(body_top + 150)),
        (int(head_x - 180), int(body_top + 100)),
    ]
    draw.polygon(sleeve_left, fill=COLORS['kimono_red'])
    
    sleeve_right = [
        (int(head_x + 150), int(body_top)),
        (int(head_x + 250), int(body_top + 50)),
        (int(head_x + 220), int(body_top + 150)),
        (int(head_x + 180), int(body_top + 100)),
    ]
    draw.polygon(sleeve_right, fill=COLORS['kimono_red'])
    
    # 繪製腰帶 (obi)
    obi_y = body_top + 180
    obi_height = 80
    
    # 腰帶主體
    obi_points = [
        (int(head_x - 160), int(obi_y)),
        (int(head_x - 160), int(obi_y + obi_height)),
        (int(head_x + 160), int(obi_y + obi_height)),
        (int(head_x + 160), int(obi_y)),
    ]
    draw.polygon(obi_points, fill=COLORS['obi_gold'])
    
    # 腰帶陰影
    obi_shadow = [
        (int(head_x - 160), int(obi_y + 10)),
        (int(head_x - 160), int(obi_y + obi_height)),
        (int(head_x + 160), int(obi_y + obi_height)),
        (int(head_x + 160), int(obi_y + 10)),
    ]
    draw.polygon(obi_shadow, fill=COLORS['obi_gold_shadow'])
    
    # 腰帶亮部
    obi_highlight = [
        (int(head_x - 160), int(obi_y)),
        (int(head_x - 160), int(obi_y + 20)),
        (int(head_x + 160), int(obi_y + 20)),
        (int(head_x + 160), int(obi_y)),
    ]
    draw.polygon(obi_highlight, fill=COLORS['obi_gold_highlight'])
    
    # 腰帶結 (前面的結)
    obi_bow_x = head_x + 180
    obi_bow_y = obi_y + 20
    bow_points = [
        (int(obi_bow_x), int(obi_bow_y)),
        (int(obi_bow_x + 60), int(obi_bow_y + 30)),
        (int(obi_bow_x + 40), int(obi_bow_y + 60)),
        (int(obi_bow_x - 20), int(obi_bow_y + 40)),
    ]
    draw.polygon(bow_points, fill=COLORS['obi_gold'])
    
    # 腰帶上的紋樣
    draw_obi_pattern(draw, head_x, obi_y, obi_height)
    
    # 和服上的花紋
    draw_kimono_pattern(draw, head_x, body_top, body_bottom)

def draw_obi_pattern(draw, center_x, y, height):
    """繪製腰帶上的紋樣"""
    pattern_width = 140
    pattern_start = center_x - pattern_width // 2
    pattern_end = center_x + pattern_width // 2
    
    # 繪製傳統紋樣
    for i in range(5):
        x = pattern_start + i * 30
        draw.ellipse([(int(x - 8), int(y + height//2 - 8)),
                      (int(x + 8), int(y + height//2 + 8))],
                     fill=COLORS['obi_gold_highlight'])

def draw_kimono_pattern(draw, center_x, top, bottom):
    """繪製和服上的花紋"""
    # 在和服上繪製櫻花紋樣
    for i in range(8):
        angle = i * 45
        radius = 100 + random.randint(0, 50)
        px = center_x + radius * np.cos(np.radians(angle))
        py = top + 100 + radius * np.sin(np.radians(angle))
        
        if top < py < bottom - 100:
            draw_small_sakura(draw, int(px), int(py))

def draw_small_sakura(draw, x, y):
    """繪製小櫻花紋樣"""
    size = random.randint(8, 15)
    num_petals = 5
    
    for i in range(num_petals):
        angle = i * (360 / num_petals) + random.uniform(-5, 5)
        petal_x = x + size * np.cos(np.radians(angle))
        petal_y = y + size * np.sin(np.radians(angle))
        
        # 簡化花瓣
        draw.ellipse([(int(petal_x - 3), int(petal_y - 3)),
                      (int(petal_x + 3), int(petal_y + 3))],
                     fill=COLORS['sakura_pink'])
    
    draw.ellipse([(int(x - 2), int(y - 2)), (int(x + 2), int(y + 2))],
                 fill=(255, 240, 180))

def draw_kanzashi(draw, head_x, head_y):
    """繪製髮簪 (kanzashi)"""
    # 在頭髮上方繪製髮簪
    kanzashi_x = head_x + 80
    kanzashi_y = head_y - 120
    
    # 簪子主體
    draw.ellipse([(int(kanzashi_x - 5), int(kanzashi_y - 20)),
                  (int(kanzashi_x + 5), int(kanzashi_y + 20))],
                 fill=(200, 150, 50))
    
    # 簪子裝飾
    for i in range(3):
        decor_x = kanzashi_x + (i - 1) * 10
        draw.ellipse([(int(decor_x - 3), int(kanzashi_y - 25 - i * 5)),
                      (int(decor_x + 3), int(kanzashi_y - 20 - i * 5))],
                     fill=(255, 200, 80))

def add_soft_glow(img):
    """添加柔和光暈效果"""
    # 建立模糊層
    blurred = img.filter(ImageFilter.GaussianBlur(radius=10))
    
    # 將模糊層與原圖混合
    result = Image.blend(img, blurred, alpha=0.3)
    return result

def main():
    """主函數"""
    print("開始生成日本美女插畫...")
    
    # 建立畫布
    img, draw = create_image()
    
    # 繪製背景櫻花樹枝
    draw_sakura_branch(draw, img, WIDTH // 4, HEIGHT // 6, 200, -30, 3)
    draw_sakura_branch(draw, img, WIDTH * 3 // 4, HEIGHT // 6, 180, 30, 3)
    draw_sakura_branch(draw, img, WIDTH // 2, HEIGHT // 10, 150, 0, 2)
    
    # 繪製飄落的花瓣
    draw_petals_falling(draw, img)
    
    # 繪製人物
    draw_character(draw, img)
    
    # 繪製髮簪
    draw_kanzashi(draw, WIDTH // 2, HEIGHT // 4)
    
    # 添加光暈效果
    img = add_soft_glow(img)
    
    # 保存圖片
    output_path = "artifacts/4359229809/japanese_beauty.png"
    img.save(output_path)
    print(f"插畫已保存至 {output_path}")
    
    return img

if __name__ == "__main__":
    main()