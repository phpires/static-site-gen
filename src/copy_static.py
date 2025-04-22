import os
import shutil

def copy_from_static_to_public():
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.mkdir("public")
    def copy_contents_from_dir(src, dest):
        src_dir_content = os.listdir(src)
        print(f"copying content: {src_dir_content}")
        dir_to_create = {}
        if len(src_dir_content) == 0:
            return
        for content in src_dir_content:
            src_path = os.path.join(src, content)
            dest_path = os.path.join(dest, content)
            if os.path.isfile(src_path):
                print(f"Copied {src_path} to {dest_path}")
                shutil.copy(src_path, dest_path)
            else:
                print(f"Created a new dir: {dest_path}")
                os.mkdir(dest_path)
                dir_to_create[src_path] = dest_path
        if dir_to_create:
            print(dir_to_create)
            for src in dir_to_create:
                copy_contents_from_dir(src, dir_to_create[src])
    return copy_contents_from_dir("static", "public")