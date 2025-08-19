"""
WebDAV Node for ComfyUI
=======================

This module provides a custom node for ComfyUI that allows users to upload generated images 
directly to a WebDAV server without saving them to the local disk.
"""

import os
import io
import logging
from typing import Dict, Any, Tuple
import requests
from webdav4.client import Client
import numpy as np
from PIL import Image

# Set up logging
logger = logging.getLogger(__name__)

class WebDAVUploadNode:
    """
    A ComfyUI node that uploads images to a WebDAV server.
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Dict[str, Any]]:
        """
        Define the input types for the node.
        """
        return {
            "required": {
                "images": ("IMAGE",),
                "server_url": ("STRING", {
                    "default": "https://example.com/webdav/",
                    "multiline": False
                }),
                "username": ("STRING", {
                    "default": "",
                    "multiline": False
                }),
                "password": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "password": True
                }),
                "remote_path": ("STRING", {
                    "default": "/",
                    "multiline": False
                }),
            },
            "optional": {
                "skip_ssl_verify": ("BOOLEAN", {
                    "default": False
                })
            }
        }

    RETURN_TYPES = ("IMAGE", "STRING")
    RETURN_NAMES = ("images", "status")
    FUNCTION = "upload_images"
    CATEGORY = "image/postprocessing"
    OUTPUT_NODE = True

    def upload_images(self, images, server_url: str, username: str, password: str, 
                      remote_path: str, skip_ssl_verify: bool = False) -> Tuple[Any, str]:
        """
        Upload images to WebDAV server.
        
        Args:
            images: Input images from ComfyUI
            server_url: WebDAV server URL
            username: WebDAV username
            password: WebDAV password
            remote_path: Remote path on WebDAV server
            skip_ssl_verify: Whether to skip SSL verification
            
        Returns:
            Tuple of (images, status message)
        """
        # Validate inputs
        if not server_url:
            return (images, "Error: Server URL is required")
            
        if not username or not password:
            return (images, "Error: Username and password are required")
            
        # Set SSL verification
        if skip_ssl_verify:
            requests.packages.urllib3.disable_warnings()
            verify_ssl = False
        else:
            verify_ssl = True
            
        try:
            # Initialize WebDAV client
            client = Client(
                server_url,
                auth=(username, password),
                verify=verify_ssl
            )
            
            # Process each image
            status_messages = []
            for i, image in enumerate(images):
                # Convert ComfyUI image format to PIL Image
                pil_image = self.tensor_to_pil(image)
                
                # Generate filename
                filename = f"comfyui_image_{i+1}.png"
                remote_file_path = os.path.join(remote_path, filename).replace("\\", "/")
                
                # Upload image
                success = self.upload_single_image(client, pil_image, remote_file_path)
                if success:
                    status_messages.append(f"Uploaded {filename} successfully")
                else:
                    status_messages.append(f"Failed to upload {filename}")
                    
            return (images, "; ".join(status_messages))
            
        except Exception as e:
            logger.error(f"WebDAV upload error: {str(e)}")
            return (images, f"Error: {str(e)}")

    def tensor_to_pil(self, tensor_image) -> Image.Image:
        """
        Convert ComfyUI tensor image to PIL Image.
        
        Args:
            tensor_image: Image tensor from ComfyUI
            
        Returns:
            PIL Image object
        """
        # Convert tensor to numpy array
        image_array = tensor_image.cpu().numpy()
        
        # Convert from 0-1 float to 0-255 uint8
        image_array = (image_array * 255).astype(np.uint8)
        
        # Create PIL Image
        pil_image = Image.fromarray(image_array)
        return pil_image

    def upload_single_image(self, client: Client, pil_image: Image.Image, 
                           remote_path: str) -> bool:
        """
        Upload a single PIL image to WebDAV server.
        
        Args:
            client: WebDAV client
            pil_image: PIL Image to upload
            remote_path: Remote path for the image
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Convert PIL image to bytes
            img_byte_arr = io.BytesIO()
            pil_image.save(img_byte_arr, format='PNG')
            img_byte_arr.seek(0)
            
            # Upload to WebDAV
            client.upload_fileobj(img_byte_arr, remote_path)
            return True
            
        except Exception as e:
            logger.error(f"Failed to upload image to {remote_path}: {str(e)}")
            return False