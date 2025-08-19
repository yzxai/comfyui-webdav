from .webdav_node import WebDAVUploadNode

NODE_CLASS_MAPPINGS = {
    "WebDAVUploadNode": WebDAVUploadNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "WebDAVUploadNode": "WebDAV Upload"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']