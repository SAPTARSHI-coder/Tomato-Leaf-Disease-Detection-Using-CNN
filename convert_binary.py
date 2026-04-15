import os
import shutil

SOURCE_DIR = "dataset"
DEST_DIR = "dataset_binary"
HEALTHY_CLASS = "healthy"

for split in ["train", "test"]:
    os.makedirs(os.path.join(DEST_DIR, split, "healthy"), exist_ok=True)
    os.makedirs(os.path.join(DEST_DIR, split, "diseased"), exist_ok=True)

def process_split(split_name):
    source_path = os.path.join(SOURCE_DIR, split_name)

    if not os.path.exists(source_path):
        print(f"ERROR: {source_path} not found")
        return

    for category in os.listdir(source_path):
        category_path = os.path.join(source_path, category)

        if not os.path.isdir(category_path):
            continue

        if category.lower() == HEALTHY_CLASS:
            label = "healthy"
        else:
            label = "diseased"

        dest_path = os.path.join(DEST_DIR, split_name, label)

        for file in os.listdir(category_path):
            src_file = os.path.join(category_path, file)
            dst_file = os.path.join(dest_path, file)

            try:
                shutil.copy(src_file, dst_file)
            except Exception as e:
                print(f"Skipped {file}: {e}")

process_split("train")
process_split("test")

print("Binary dataset created successfully!")