from dicom_csv import join_tree

df = join_tree('./Burdenko-GBM-Progression', verbose=1, ignore_extensions=['.zip'])
df.to_csv('./meta.csv')