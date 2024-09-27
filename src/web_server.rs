use tokio::net::UnixListener;
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use std::path::PathBuf;

#[cfg(windows)]
use tokio_uds_windows::UnixListener;

pub async fn start_web_server(socket_path: PathBuf) -> Result<(), Box<dyn std::error::Error>> {
    let listener = UnixListener::bind(&socket_path)?;

    loop {
        let (mut stream, _) = listener.accept().await?;
        tokio::spawn(async move {
            let mut buffer = [0; 1024];
            let n = stream.read(&mut buffer).await.unwrap();
            let request = String::from_utf8_lossy(&buffer[..n]);

            let response = handle_request(&request);

            stream.write_all(response.as_bytes()).await.unwrap();
        });
    }
}

fn handle_request(request: &str) -> String {
    format!("Processed request: {}", request)
}