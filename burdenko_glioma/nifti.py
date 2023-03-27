import numpy as np
from subprocess import check_call
from pathlib import Path
from pydicom import dcmread
from typing import Union
from dicom_csv.utils import Series


def dicom_to_nifti(source_folder: Path, target_folder: Path, name=None):
    """Converts folder of dicoms into a nii.gz file."""
    cmd = ['dcm2niix', '-z', 'y']
    if name is not None:
        cmd.append('-f')
        cmd.append(name)
    cmd.append('-o')
    cmd.append(f'{str(target_folder)}/')
    cmd.append(f'{str(source_folder)}/')
    return check_call(cmd)


def get_series_instance_uid(rtstruct_path: [str, Path]):
    """Get SeriesInstanceUID of a reference image of input RTSTRUCT."""
    dicom = dcmread(rtstruct_path)
    return dicom.ReferencedFrameOfReferenceSequence[0]\
                .RTReferencedStudySequence[0]\
                .RTReferencedSeriesSequence[0].SeriesInstanceUID


def mask_to_dicom(series: Series, mask: np.ndarray, folder: Union[Path, str]) -> Series:
    """Writes three-dimensional binary mask to series of reference DICOM files and save them to folder."""
    dtype = series[0].pixel_array.dtype
    for frame, m2 in zip(series, np.moveaxis(mask, 2, 0)):
        byte_mask = m2.astype(dtype).tobytes()
        uid = frame.SOPInstanceUID
        if len(byte_mask) % 2 != 0:
            byte_mask += b'\x00'
        frame.PixelData = byte_mask
        frame.save_as(folder / f'{uid}.dcm')
