# patient_to_nifti(root, patient_id, target_folder)
import sys
import os
from pathlib import Path
from burdenko_glioma.nifti import dicom_to_nifti

if __name__=="__main__":
    root = sys.argv[1]
    patient_id = sys.argv[2]
    target_folder = sys.argv[3]
    
   
    for subfolder in os.listdir(Path(root) / patient_id):
        if 'Radiotherapy planning' in subfolder:
            baseline_visit = subfolder
    
    source_folder = Path(root) / patient_id / baseline_visit
    rt_folders = ['RTSTRUCT', 'RTPLAN', 'RTDOSE']
    for subfolder in source_folder.glob('*'):
        if subfolder.name in rt_folders:
            continue
        dicom_to_nifti(subfolder, Path(target_folder), name=subfolder.name)