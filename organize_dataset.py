"""
Organize Tomato Dataset into Diseased and Healthy categories
"""
import os
import shutil
from pathlib import Path
import json
from collections import defaultdict

def organize_tomato_dataset():
    """
    Organize the tomato dataset by disease/non-disease classification
    """
    source_dir = "dataset/train/tomato dataset"
    base_dir = "dataset/train"
    
    # Define disease categories
    diseases = {
        'Leaf_Mold': 'diseased',
        'Septoria_leaf_spot': 'diseased',
        'Spider_mites': 'diseased',
        'Target_Spot': 'diseased',
        'Tomato_mosaic_virus': 'diseased',
        'Tomato_Early_blight': 'diseased',
        'Tomato_Late_blight': 'diseased',
        'Tomato_Yellow_Leaf_Curl_Virus': 'diseased',
        'Tomato_Bacterial_Spot': 'diseased'
    }
    
    # Create new directory structure
    new_train_dir = "dataset/train"
    new_test_dir = "dataset/test"
    
    for base_path in [new_train_dir, new_test_dir]:
        os.makedirs(os.path.join(base_path, "healthy"), exist_ok=True)
        os.makedirs(os.path.join(base_path, "diseased"), exist_ok=True)
    
    print("=" * 60)
    print("🚀 ORGANIZING TOMATO DATASET")
    print("=" * 60)
    
    # If source directory doesn't exist, skip this
    if not os.path.exists(source_dir):
        print(f"\n⚠️  Source directory not found: {source_dir}")
        return
    
    # Get all files
    files = os.listdir(source_dir)
    print(f"\nTotal files found: {len(files)}")
    
    disease_count = defaultdict(int)
    healthy_count = 0
    
    # Process each file
    for idx, filename in enumerate(files):
        source_path = os.path.join(source_dir, filename)
        
        # Skip if not file
        if not os.path.isfile(source_path):
            continue
        
        # Determine if diseased or healthy based on filename
        is_diseased = False
        detected_disease = "unknown"
        
        for disease_key in diseases.keys():
            if disease_key in filename:
                is_diseased = True
                detected_disease = disease_key
                disease_count[disease_key] += 1
                break
        
        # If not detected as disease, must be healthy
        if not is_diseased:
            healthy_count += 1
            detected_disease = "healthy"
        
        # Split: 80% train, 20% test
        if idx % 5 == 0:  # 20% for test
            dest_dir = "diseased" if is_diseased else "healthy"
            dest_path = os.path.join(new_test_dir, dest_dir, filename)
        else:  # 80% for train
            dest_dir = "diseased" if is_diseased else "healthy"
            dest_path = os.path.join(new_train_dir, dest_dir, filename)
        
        # Copy file
        try:
            shutil.copy2(source_path, dest_path)
        except Exception as e:
            print(f"Error copying {filename}: {e}")
        
        if (idx + 1) % 50 == 0:
            print(f"  Processed: {idx + 1}/{len(files)} files...")
    
    # Print summary
    print("\n" + "=" * 60)
    print("📊 ORGANIZATION SUMMARY")
    print("=" * 60)
    
    print(f"\n✓ Healthy images: {healthy_count}")
    print(f"✓ Diseased images: {len(files) - healthy_count}")
    
    print(f"\n📋 Disease Breakdown:")
    total_diseases = 0
    for disease, count in sorted(disease_count.items(), key=lambda x: x[1], reverse=True):
        print(f"   • {disease}: {count} images")
        total_diseases += count
    
    # Check created directories
    print(f"\n📁 Dataset Structure Created:")
    
    for data_type in ["train", "test"]:
        dir_path = f"dataset/{data_type}"
        diseased = len(os.listdir(os.path.join(dir_path, "diseased"))) if os.path.exists(os.path.join(dir_path, "diseased")) else 0
        healthy = len(os.listdir(os.path.join(dir_path, "healthy"))) if os.path.exists(os.path.join(dir_path, "healthy")) else 0
        print(f"\n   {data_type.upper()}:")
        print(f"      Diseased: {diseased}")
        print(f"      Healthy: {healthy}")
        print(f"      Total: {diseased + healthy}")
    
    print("\n✅ Dataset organization complete!")

if __name__ == "__main__":
    organize_tomato_dataset()
