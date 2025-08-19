# ComfyUI WebDAV Node

This project provides a custom node for ComfyUI that allows users to upload generated images directly to a WebDAV server without saving them to the local disk.

## Features
- Upload images directly to WebDAV server
- Customizable server configuration (URL, username, password, remote path)
- SSL certificate validation options
- Image preview functionality

## Installation

1. Clone this repository to your ComfyUI `custom_nodes` directory:
   ```
   cd ComfyUI/custom_nodes
   git clone <repository-url> comfyui-webdav
   ```

2. Install the required dependencies:
   ```
   pip install -r comfyui-webdav/requirements.txt
   ```

3. Restart ComfyUI

## Usage

1. Add the "WebDAV Upload" node to your workflow
2. Connect the output of an image generation node to the "images" input of the WebDAV node
3. Configure the WebDAV server settings:
   - Server URL: Your WebDAV server URL (e.g., https://example.com/webdav/)
   - Username: Your WebDAV username
   - Password: Your WebDAV password
   - Remote Path: The directory on the WebDAV server where files should be uploaded
   - Skip SSL Verify: Check this if you're using a self-signed certificate

4. Run your workflow

## Configuration Options

- **Server URL**: The full URL to your WebDAV server
- **Username**: Your WebDAV account username
- **Password**: Your WebDAV account password
- **Remote Path**: The directory path on the WebDAV server where images will be uploaded
- **Skip SSL Verify**: When checked, SSL certificate validation will be skipped (useful for self-signed certificates)

## How It Works

The WebDAV Upload node takes generated images from ComfyUI, converts them to PNG format in memory, and uploads them directly to your WebDAV server without saving them to the local disk. This is especially useful for:
- Privacy: Images never touch your local storage
- Automation: Direct upload to cloud storage
- Workflow: Seamless integration with WebDAV-based workflows

## Requirements

- ComfyUI
- Python 3.7+
- webdav4 library
- requests library
- Pillow library

## Troubleshooting

If you encounter issues:
1. Verify your WebDAV server URL, username, and password
2. Check that your WebDAV server is accessible
3. If using a self-signed certificate, enable "Skip SSL Verify"
4. Check ComfyUI logs for detailed error messages

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.