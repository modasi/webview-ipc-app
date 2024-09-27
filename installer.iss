; Inno Setup Script for webview-ipc-app

[Setup]
AppName=WebView IPC App
AppVersion=1.0
DefaultDirName={pf}\WebView IPC App
DefaultGroupName=WebView IPC App
OutputDir=.
OutputBaseFilename=WebViewIPCAppSetup

[Files]
Source: "src-tauri\target\release\webview-ipc-app.exe"; DestDir: "{app}"

[Icons]
Name: "{group}\WebView IPC App"; Filename: "{app}\webview-ipc-app.exe"
Name: "{commondesktop}\WebView IPC App"; Filename: "{app}\webview-ipc-app.exe"

[Run]
Filename: "{app}\webview-ipc-app.exe"; Description: "Launch WebView IPC App"; Flags: postinstall nowait