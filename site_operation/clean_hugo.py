import os
import shutil

# ======== CONFIG ========
# Path to your Hugo project
HUGO_DIR = "~/Dropbox/private_data/part_time/devops_blog/quantcodedenny.com/"

# Folders/files to remove
AUTO_GEN_ITEMS = [
    "content", # markdown files
    "docs/posts",
    "docs/tags",
    ".hugo_build.lock",
]

# ======== SCRIPT ========
def remove_auto_gen(hugo_dir):
    for item in AUTO_GEN_ITEMS:
        path = os.path.join(hugo_dir, item)
        if os.path.exists(path):
            if os.path.isdir(path):
                print(f"Removing directory: {path}")
                shutil.rmtree(path)
            else:
                print(f"Removing file: {path}")
                os.remove(path)
        else:
            print(f"Not found, skipping: {path}")

if __name__ == "__main__":
    remove_auto_gen(HUGO_DIR)
    print("Clean Hugo auto-generated files complete.")
