import os
import shutil

def copy_from_static_to_public(src,dest):
    
    if not os.path.exists(dest):
        print(f"Creating new dir: {dest}")
        os.mkdir(dest)

    src_dir_content = os.listdir(src)
    print(f"copying content: {src_dir_content}")
    for content in src_dir_content:
        src_path = os.path.join(src, content)
        dest_path = os.path.join(dest, content)
        if os.path.isfile(src_path):
            print(f"Copied {src_path} to {dest_path}")
            shutil.copy(src_path, dest_path)
        else:
            copy_from_static_to_public(src_path, dest_path)
