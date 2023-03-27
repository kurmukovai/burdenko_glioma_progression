import matplotlib.pyplot as plt
import numpy as np

def select12(image):
    n = image.shape[2]
    return [int(i) for i in np.round(np.linspace(0, n-1, 12))]

def plot_qc(image, patient_id, modality, series_instance_uid, root):
    fig, axs = plt.subplots(3, 4, figsize=(12,9))
    slices = select12(image)
    n = image.shape[2]
    
    if modality == "CT00CT":
        image = np.clip(image, 40, 120)

    for s, ax in zip(slices, axs.flatten()):
        ax.imshow(image[..., s], cmap='gray')
        ax.text(0.1, 0.8, patient_id, color='white', fontsize=8, transform=ax.transAxes)
        ax.text(0.1, 0.7, modality, color='white', fontsize=8, transform=ax.transAxes)
        ax.text(0.1, 0.6, f'{s}/{n}', color='white', fontsize=8, transform=ax.transAxes)
        ax.set_axis_off()

    plt.tight_layout()
    plt.savefig(root / f'{patient_id}_{modality}_{series_instance_uid}.jpeg', dpi=100)
    plt.close()