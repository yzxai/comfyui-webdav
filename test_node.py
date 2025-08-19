#!/usr/bin/env python3
"""
Test script for ComfyUI WebDAV Node
"""

import sys
import os

# Add the current directory to the path so we can import the node
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_node_import():
    """Test that the node can be imported successfully."""
    try:
        import __init__
        print("✅ Node imported successfully")
        
        # Check that the node mappings are defined
        if hasattr(__init__, 'NODE_CLASS_MAPPINGS'):
            print("✅ NODE_CLASS_MAPPINGS found")
            print("Available nodes:", list(__init__.NODE_CLASS_MAPPINGS.keys()))
        else:
            print("❌ NODE_CLASS_MAPPINGS not found")
            
        if hasattr(__init__, 'NODE_DISPLAY_NAME_MAPPINGS'):
            print("✅ NODE_DISPLAY_NAME_MAPPINGS found")
            print("Node display names:", dict(__init__.NODE_DISPLAY_NAME_MAPPINGS))
        else:
            print("❌ NODE_DISPLAY_NAME_MAPPINGS not found")
            
        return True
    except Exception as e:
        print(f"❌ Error importing node: {e}")
        return False

def test_node_initialization():
    """Test that the node class can be initialized."""
    try:
        from nodes.webdav_node import WebDAVUploadNode
        
        # Test INPUT_TYPES
        input_types = WebDAVUploadNode.INPUT_TYPES()
        print("✅ INPUT_TYPES method works")
        print("Required inputs:", list(input_types.get('required', {}).keys()))
        print("Optional inputs:", list(input_types.get('optional', {}).keys()))
        
        # Test class attributes
        print("Return types:", WebDAVUploadNode.RETURN_TYPES)
        print("Return names:", WebDAVUploadNode.RETURN_NAMES)
        print("Function name:", WebDAVUploadNode.FUNCTION)
        print("Category:", WebDAVUploadNode.CATEGORY)
        
        return True
    except Exception as e:
        print(f"❌ Error initializing node: {e}")
        return False

if __name__ == "__main__":
    print("Testing ComfyUI WebDAV Node...")
    print("=" * 40)
    
    success = True
    success &= test_node_import()
    print()
    success &= test_node_initialization()
    
    print("=" * 40)
    if success:
        print("🎉 All tests passed!")
    else:
        print("💥 Some tests failed!")
        sys.exit(1)