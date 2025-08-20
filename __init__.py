from .webdav_node import WebDAVUploadNode
from .privacy_protect_node import PrivacyProtectNode

NODE_CLASS_MAPPINGS = {
    "WebDAVUploadNode": WebDAVUploadNode,
    "PrivacyProtectNode": PrivacyProtectNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "WebDAVUploadNode": "WebDAV Upload",
    "PrivacyProtectNode": "Privacy Protect"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']