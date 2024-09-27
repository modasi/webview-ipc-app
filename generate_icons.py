import os
from PIL import Image
import subprocess

def generate_icons(source_icon):
    if not os.path.exists(source_icon):
        print(f"Error: {source_icon} not found.")
        return

    os.makedirs("icons", exist_ok=True)

    with Image.open(source_icon) as img:
        generate_macos_icons(img)
        generate_windows_icons(img)
        generate_linux_icons(img)
        generate_ios_icons(img)
        generate_android_icons(img)

    print("Icons generated successfully.")

def generate_macos_icons(img):
    sizes = [16, 32, 64, 128, 256, 512, 1024]
    iconset_path = "icons/icon.iconset"
    os.makedirs(iconset_path, exist_ok=True)

    for size in sizes:
        icon_path = os.path.join(iconset_path, f"icon_{size}x{size}.png")
        img.resize((size, size), Image.LANCZOS).save(icon_path)
        if size <= 512:
            icon_path = os.path.join(iconset_path, f"icon_{size}x{size}@2x.png")
            img.resize((size*2, size*2), Image.LANCZOS).save(icon_path)

    subprocess.run(["iconutil", "-c", "icns", iconset_path])
    os.rename("icon.icns", "icons/icon.icns")

def generate_windows_icons(img):
    sizes = [16, 32, 48, 256]
    for size in sizes:
        img.resize((size, size), Image.LANCZOS).save(f"icons/icon_{size}x{size}.png")
    
    img.save("icons/icon.ico", format="ICO", sizes=[(size, size) for size in sizes])

def generate_linux_icons(img):
    sizes = [16, 22, 24, 32, 48, 64, 128, 256]
    for size in sizes:
        img.resize((size, size), Image.LANCZOS).save(f"icons/icon_{size}x{size}.png")

def generate_ios_icons(img):
    sizes = [20, 29, 40, 58, 60, 76, 80, 87, 120, 152, 167, 180, 1024]
    for size in sizes:
        img.resize((size, size), Image.LANCZOS).save(f"icons/icon_{size}x{size}.png")

def generate_android_icons(img):
    sizes = [36, 48, 72, 96, 144, 192]
    for size in sizes:
        img.resize((size, size), Image.LANCZOS).save(f"icons/icon_{size}x{size}.png")

if __name__ == "__main__":
    source_icon = "icon.png"
    generate_icons(source_icon)