import os
import shutil
import random

SOURCE_DIR = "C:/Users/Asus/Desktop/New folder (4)/train"             # your extracted dataset
DEST_DIR = "dataset"             

TRAIN_DIR = os.path.join(DEST_DIR, "train")
TEST_DIR = os.path.join(DEST_DIR, "test")

split_ratio = 0.7  # 70% train, 30% test


os.makedirs(TRAIN_DIR, exist_ok=True)
os.makedirs(TEST_DIR, exist_ok=True)

for category in os.listdir(SOURCE_DIR):
    category_path = os.path.join(SOURCE_DIR, category)

    if not os.path.isdir(category_path):
        continue

    images = os.listdir(category_path)
    random.shuffle(images)

    split_index = int(len(images) * split_ratio)

    train_images = images[:split_index]
    test_images = images[split_index:]

    train_cat_dir = os.path.join(TRAIN_DIR, category)
    test_cat_dir = os.path.join(TEST_DIR, category)

    os.makedirs(train_cat_dir, exist_ok=True)
    os.makedirs(test_cat_dir, exist_ok=True)

    # Copy train images
    for img in train_images:
        src = os.path.join(category_path, img)
        dst = os.path.join(train_cat_dir, img)
        shutil.copy2(src, dst)

    # Copy test images
    for img in test_images:
        src = os.path.join(category_path, img)
        dst = os.path.join(test_cat_dir, img)
        shutil.copy2(src, dst)

print("✅ Dataset split completed (70% train / 30% test)")