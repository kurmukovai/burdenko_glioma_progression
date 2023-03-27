Repository to ease Burdenko Glioma Progression Dataset preparations. Start with downloading the data from TCIA portal.

# Installation

git clone git@github.com:kurmukovai/burdenko_glioma_progression.git
cd burdenko_glioma_progression
pip install -e .

# Basic usage
1. Convert single patient Radiotherapy study from DICOM to NIfTI
./scripts/python patient_to_nifti.py root_folder patient_id target_folder

