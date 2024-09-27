set_project("webview-ipc-app")
set_version("0.1.0")

add_rules("mode.debug", "mode.release")

if is_plat("macosx") then
    add_frameworks("WebKit")
elseif is_plat("windows") then
    add_syslinks("user32", "gdi32", "shell32")
elseif is_plat("linux") then
    add_deps("gtk+-3.0", "webkit2gtk-4.0")
end

target("webview-ipc-app")
    set_kind("binary")
    add_files("src/*.rs")
    add_files("src-tauri/src/*.rs")
    set_targetdir("target")

    if is_mode("debug") then
        set_symbols("debug")
        set_optimize("none")
    elseif is_mode("release") then
        set_symbols("hidden")
        set_optimize("fastest")
        set_strip("all")
    end