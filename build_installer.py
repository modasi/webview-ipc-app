import os
import platform
import subprocess
import shutil

def run_command(command):
    subprocess.run(command, check=True, shell=True)

def build_macos():
    print("Building macOS installer...")
    run_command("cargo tauri build")
    app_name = "webview-ipc-app"
    
    # Create .pkg installer
    run_command(f"pkgbuild --root src-tauri/target/release/bundle/macos/{app_name}.app --identifier com.example.{app_name} --version 1.0 --install-location /Applications {app_name}.pkg")

def build_windows():
    print("Building Windows installer...")
    run_command("cargo tauri build")
    
    # Use Inno Setup to create installer
    run_command("iscc installer.iss")

def build_linux():
    print("Building Linux installer...")
    run_command("cargo tauri build")
    run_command("cargo deb")  # Create .deb package
    run_command("cargo rpm")  # Create .rpm package

def build_ios():
    print("Building iOS package...")
    run_command("cargo tauri ios build")
    # Generate .ipa file
    run_command("xcodebuild -exportArchive -archivePath src-tauri/gen/ios/build/MyApp.xcarchive -exportOptionsPlist exportOptions.plist -exportPath .")

def build_android():
    print("Building Android package...")
    run_command("cargo tauri android build")
    # APK file should be generated in src-tauri/gen/android/app/build/outputs/apk/

def main():
    system = platform.system().lower()
    if system == "darwin":
        build_macos()
        build_ios()  # Only build iOS package on macOS
    elif system == "windows":
        build_windows()
    elif system == "linux":
        build_linux()
    else:
        print(f"Unsupported operating system: {system}")
    
    # Build Android package on all platforms
    build_android()

if __name__ == "__main__":
    main()