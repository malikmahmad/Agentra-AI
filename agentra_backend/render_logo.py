from PIL import Image, ImageDraw, ImageFont
import math

def render():
    size = 1024
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    
    # 1. Background (Rounded Rect)
    bg_color = (8, 14, 26, 255) # #080E1A
    d.rounded_rectangle([0, 0, size, size], radius=220, fill=bg_color)
    
    # 2. Subtle Grid
    grid_color = (0, 212, 255, 10) # #00D4FF with low opacity
    for i in range(0, size, 128):
        d.line([(i, 0), (i, size)], fill=grid_color, width=2)
        d.line([(0, i), (size, i)], fill=grid_color, width=2)

    # 3. Outer Orbit Rings (Simplified for PIL)
    center = (512, 430)
    cyan = (0, 212, 255, 150)
    
    # Render rings using ellipses with different rotations would be complex in PIL
    # We will draw 3 stylized circular orbits instead
    d.ellipse([center[0]-340, center[1]-130, center[0]+340, center[1]+130], outline=cyan, width=3)
    d.ellipse([center[0]-320, center[1]-200, center[0]+320, center[1]+200], outline=cyan, width=2)
    
    # 4. Main Central Sphere
    sphere_color = (10, 30, 53, 255)
    d.ellipse([center[0]-180, center[1]-180, center[0]+180, center[1]+180], fill=sphere_color, outline=(0, 212, 255, 100), width=4)
    
    # 5. Neural Nodes & Connections
    node_color = (0, 212, 255, 255)
    nodes = [
        (center[0], center[1]-180), # Top
        (center[0], center[1]+180), # Bottom
        (center[0]-180, center[1]), # Left
        (center[0]+180, center[1]), # Right
        (center[0]+128, center[1]-128),
        (center[0]-128, center[1]-128),
        (center[0]+128, center[1]+128),
        (center[0]-128, center[1]+128),
    ]
    
    for node in nodes:
        d.line([center, node], fill=(0, 212, 255, 50), width=2)
        d.ellipse([node[0]-15, node[1]-15, node[0]+15, node[1]+15], fill=node_color)

    # 6. Core Glow and 'A'
    d.ellipse([center[0]-55, center[1]-55, center[0]+55, center[1]+55], fill=(0, 24, 48, 255), outline=node_color, width=3)
    
    # Attempt to use a bold font, fallback to default if not found
    try:
        font_a = ImageFont.truetype("arialbd.ttf", 70)
        font_name = ImageFont.truetype("arialbd.ttf", 90)
        font_tag = ImageFont.truetype("arial.ttf", 25)
    except:
        font_a = ImageFont.load_default(size=70)
        font_name = ImageFont.load_default(size=90)
        font_tag = ImageFont.load_default(size=25)

    d.text((center[0], center[1]), "A", fill=node_color, anchor="mm", font=font_a)

    # 7. Bottom Branding
    d.line([(162, 660), (862, 660)], fill=(0, 212, 255, 60), width=3)
    d.text((512, 740), "AGENTRA", fill="white", anchor="mm", font=font_name)
    d.text((512, 800), "AI AGENT SYSTEM", fill=node_color, anchor="mm", font=font_tag)

    # 8. Corner Accents
    acc = (0, 212, 255, 80)
    # TL
    d.line([(80, 80), (140, 80)], fill=acc, width=5)
    d.line([(80, 80), (80, 140)], fill=acc, width=5)
    # TR
    d.line([(944, 80), (884, 80)], fill=acc, width=5)
    d.line([(944, 80), (944, 140)], fill=acc, width=5)
    # BL
    d.line([(80, 944), (140, 944)], fill=acc, width=5)
    d.line([(80, 944), (80, 884)], fill=acc, width=5)
    # BR
    d.line([(944, 944), (884, 944)], fill=acc, width=5)
    d.line([(944, 944), (944, 884)], fill=acc, width=5)

    img.save('C:/Users/zubai/agentra/assets/icon.png')
    print("Logo rendered successfully to assets/icon.png")

if __name__ == "__main__":
    render()
