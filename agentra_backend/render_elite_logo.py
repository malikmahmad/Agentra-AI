from PIL import Image, ImageDraw
import math

def render():
    size = 1024
    # Deep Dark Background
    img = Image.new('RGB', (size, size), '#0A0E1A')
    d = ImageDraw.Draw(img)
    
    center = (512, 512) # Centered icon
    cyan = '#00D4FF'
    emerald = '#00FF85'
    
    # Render the abstract neural sphere from the user's design (NO TEXT)
    
    # 1. Background Grid (Subtle)
    for i in range(0, size, 128):
        d.line([(i, 0), (i, size)], fill='#111F30', width=2)
        d.line([(0, i), (size, i)], fill='#111F30', width=2)
    
    # 2. Outer Orbit Rings
    d.ellipse([center[0]-380, center[1]-380, center[0]+380, center[1]+380], outline='#005577', width=2)
    d.ellipse([center[0]-320, center[1]-320, center[0]+320, center[1]+320], outline='#003355', width=1)
    
    # 3. Main Central Sphere
    d.ellipse([center[0]-220, center[1]-220, center[0]+220, center[1]+220], fill='#0D1B2E', outline=cyan, width=15)
    
    # 4. Neural Nodes
    nodes = []
    for i in range(8):
        angle = math.radians(i * 45)
        x = center[0] + 220 * math.cos(angle)
        y = center[1] + 220 * math.sin(angle)
        nodes.append((x,y))
        
    for node in nodes:
        d.line([center, node], fill='#005577', width=3)
        d.ellipse([node[0]-20, node[1]-20, node[0]+20, node[1]+20], fill=cyan)
        
    # 5. Inner Core
    d.ellipse([center[0]-80, center[1]-80, center[0]+80, center[1]+80], fill='#001830', outline=emerald, width=5)
    
    # Center Glow Node
    d.ellipse([center[0]-30, center[1]-30, center[0]+30, center[1]+30], fill=emerald)

    img.save('C:/Users/zubai/agentra/assets/icon.png')
    print("Elite icon rendered successfully.")

if __name__ == "__main__":
    render()
