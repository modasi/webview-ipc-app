use tauri::Manager;
use url::Url;

pub async fn run_webview(socket_path: std::path::PathBuf) -> Result<(), Box<dyn std::error::Error>> {
    let context = tauri::generate_context!();
    tauri::Builder::default()
        .setup(|app| {
            let window = app.get_window("main").unwrap();
            let socket_path_clone = socket_path.clone();
            
            window.listen("ipc-message", move |event| {
                let socket_path = socket_path_clone.clone();
                tokio::spawn(async move {
                    let payload = event.payload().unwrap();
                    let response = crate::ipc::send_request(socket_path, payload.to_string()).await.unwrap();
                    window.emit("ipc-response", response).unwrap();
                });
            });
            
            Ok(())
        })
        .run(context)
        .expect("Error while running tauri application");

    Ok(())
}