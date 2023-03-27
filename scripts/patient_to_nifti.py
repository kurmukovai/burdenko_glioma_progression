# patient_to_nifti(root, patient_id, target_folder)
import sys
import os
from pathlib import Path
from burdenko_glioma.nifti import dicom_to_nifti

if __name__=="__main__":
    root = sys.argv[1]
    patient_id = sys.argv[2]
    target_folder = sys.argv[3]
    
    # '/anvar/private_datasets/anvar_work/Burdenko-TCIA/manifest-1676999639835/Burdenko-GBM-Progression'
    # 'Burdenko-GBM-001'
    # '/home/anvar/home_directory/burdenko_001'
    
    for subfolder in os.listdir(Path(root) / patient_id):
        if 'Radiotherapy planning' in subfolder:
            baseline_visit = subfolder
    
    source_folder = Path(root) / patient_id / baseline_visit
    rt_folders = ['RTSTRUCT', 'RTPLAN', 'RTDOSE']
    for subfolder in source_folder.glob('*'):
        if not any([stop in subfolder.name for stop in rt_folders]):
            dicom_to_nifti(subfolder, Path(target_folder), name=subfolder.name)