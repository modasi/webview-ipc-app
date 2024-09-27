import os
import json
import hashlib
import subprocess
from datetime import datetime

def create_update(version, notes):
    if not version.startswith('v'):
        version = f'v{version}'

    with open('src-tauri/tauri.conf.json', 'r') as f:
        config = json.load(f)

    config['package']['version'] = version[1:]
    
    with open('src-tauri/tauri.conf.json', 'w') as f:
        json.dump(config, f, indent=2)

    subprocess.run(['cargo', 'tauri', 'build'], check=True)

    update_info = {
        "version": version,
        "notes": notes,
        "pub_date": datetime.utcnow().isoformat() + "Z",
        "platforms": {
            "darwin-x86_64": {"signature": "", "url": ""},
            "darwin-aarch64": {"signature": "", "url": ""},
            "linux-x86_64": {"signature": "", "url": ""},
            "windows-x86_64": {"signature": "", "url": ""}
        }
    }

    for platform in update_info['platforms'].keys():
        if platform.startswith('darwin'):
            ext = 'app.tar.gz'
        elif platform.startswith('linux'):
            ext = 'AppImage.tar.gz'
        else:  # Windows
            ext = 'msi.zip'
        
        bundle_path = f'src-tauri/target/release/bundle/{platform}/{config["package"]["productName"]}.{ext}'
        
        if os.path.exists(bundle_path):
            with open(bundle_path, 'rb') as f:
                data = f.read()
            signature = subprocess.run(['tauri', 'signer', 'sign', '-d', data], 
                                       capture_output=True, text=True).stdout.strip()
            
            update_info['platforms'][platform]['signature'] = signature
            update_info['platforms'][platform]['url'] = f"https://releases.myapp.com/{platform}/{config['package']['productName']}-{version}.{ext}"

            os.makedirs(f'releases/{platform}', exist_ok=True)
            os.rename(bundle_path, f'releases/{platform}/{config["package"]["productName"]}-{version}.{ext}')

    with open(f'releases/{version}.json', 'w') as f:
        json.dump(update_info, f, indent=2)

    print(f"Update {version} created successfully!")

if __name__ == "__main__":
    version = input("Enter the new version number (e.g., 1.0.1): ")
    notes = input("Enter the update notes: ")
    create_update(version, notes)