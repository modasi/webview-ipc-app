use std::path::PathBuf;
use tokio::net::UnixStream;
use tokio::io::{AsyncReadExt, AsyncWriteExt};

#[cfg(windows)]
use tokio_uds_windows::UnixStream;

pub async fn send_request(socket_path: PathBuf, request: String) -> Result<String, Box<dyn std::error::Error>> {
    let mut stream = UnixStream::connect(socket_path).await?;
    stream.write_all(request.as_bytes()).await?;

    let mut response = String::new();
    stream.read_to_string(&mut response).await?;

    Ok(response)
}