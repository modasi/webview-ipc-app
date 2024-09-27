mod webview;
mod ipc;
mod web_server;

use std::path::PathBuf;
use tokio::net::UnixStream;
use tokio::io::{AsyncReadExt, AsyncWriteExt};

#[cfg(windows)]
use tokio_uds_windows::UnixStream;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let socket_path = PathBuf::from("/tmp/webview_ipc.sock");
    
    // Start the web server in a separate task
    tokio::spawn(web_server::start_web_server(socket_path.clone()));

    // Initialize and run the webview
    webview::run_webview(socket_path).await?;

    Ok(())
}