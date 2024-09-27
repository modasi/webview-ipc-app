# WebView IPC App

This is a cross-platform WebView application that demonstrates IPC communication between a WebView and a separate web server process.

## Features

- Cross-platform support (macOS, Linux, Windows, iOS, Android)
- WebView with custom protocol handling
- IPC communication using Unix domain sockets
- Built using Rust and Tauri
- Automatic updates
- Installer creation for all platforms

## System Requirements

### macOS
- macOS 10.15 (Catalina) or later
- Supports both x64 and ARM64 architectures

### Linux
- Major distributions with kernel version 4.4 or later
- x64 architecture only

### Windows
- Windows 10 version 1803 or later
- Supports both x64 and ARM64 architectures

### iOS
- iOS 13 or later

### Android
- Android 8.0 (API level 26) or later

## Getting Started

Please refer to the [build-env.md](build-env.md) file for detailed instructions on setting up the development environment, building the project, and creating installers.

## License

[MIT License](LICENSE)