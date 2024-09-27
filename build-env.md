# Build Environment Setup

This document describes the setup process for the development environment, including project configuration, third-party tool installation, and automatic update configuration and testing.

## Project Configuration

1. Application Name:
   - Open `src-tauri/tauri.conf.json` and update the `productName` field.
   - Update the `name` field in both `Cargo.toml` files (root and src-tauri).
   - Update the `AppName` in `installer.iss`.

2. Version Number:
   - Update the `version` field in both `Cargo.toml` files and `src-tauri/tauri.conf.json`.

3. Bundle Identifier:
   - Update the `identifier` field in `src-tauri/tauri.conf.json`.

4. Icons:
   - Replace `icon.png` in the project root with your own high-resolution icon (1024x1024 recommended).
   - Run `python generate_icons.py` to generate platform-specific icons.

## Third-Party Tool Installation

1. Rust:
   - Install from https://rustup.rs/

2. Tauri CLI:
   ```
   cargo install tauri-cli --version "^2.0.0-rc"
   ```

3. xmake:
   - Install from https://xmake.io/#/getting_started

4. Platform-specific tools:

   ### Windows
   - Visual Studio Build Tools 2019 or later
   - Inno Setup: https://jrsoftware.org/isdl.php

   ### macOS
   - Xcode 12 or later
   - Command Line Tools: `xcode-select --install`

   ### Linux
   - Install development packages:
     ```
     sudo apt install libwebkit2gtk-4.0-dev build-essential curl wget libssl-dev libgtk-3-dev libayatana-appindicator3-dev librsvg2-dev
     ```

   ### iOS (macOS only)
   - Xcode 12 or later
   - iOS SDK

   ### Android
   - Android Studio: https://developer.android.com/studio
   - Android SDK
   - Android NDK

5. Cargo plugins:
   ```
   cargo install cargo-deb cargo-rpm
   ```

## Building the Project

1. Clone the repository:
   ```
   git clone https://github.com/modasi/webview-ipc-app.git
   cd webview-ipc-app
   ```

2. Install dependencies:
   ```
   cargo build
   ```

3. Run the development version:
   ```
   cargo tauri dev
   ```

4. Build the release version:
   ```
   cargo tauri build
   ```

## Automatic Update Configuration

1. Generate a key pair for signing updates:
   ```
   tauri signer generate -w ~/.tauri/myapp.key
   ```

2. Update `src-tauri/tauri.conf.json`:
   - Set `tauri.updater.active` to `true`
   - Update `tauri.updater.endpoints` with your update server URL
   - Set `tauri.updater.pubkey` to the public key generated in step 1

3. Set up an update server:
   - Create a server to host your update files
   - Ensure it's accessible via HTTPS

## Testing Automatic Updates

1. Build your initial release:
   ```
   cargo tauri build
   ```

2. Increment the version number in `src-tauri/tauri.conf.json` and both `Cargo.toml` files

3. Create an update:
   ```
   python create_update.py
   ```

4. Upload the generated files in the `releases` directory to your update server

5. Run the initial release version of your app and check if it detects and installs the update

## Building Installers

Run the following command to build installers for your current platform:
    ```
    python build_installer.py
    ```

Note: Building for iOS and Android requires additional setup and may need manual intervention in Xcode or Android Studio.

## Troubleshooting

- If you encounter any issues with dependencies, try updating Rust and your cargo packages:
  ```
  rustup update
  cargo update
  ```

- For platform-specific issues, consult the Tauri documentation: https://tauri.app/v1/guides/

- Ensure all paths in scripts and configuration files match your project structure

Remember to test your build on all target platforms before distribution.