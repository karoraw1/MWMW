import os
import pandas as pd

q_fs = [(i.split(".")[0], pd.read_csv(i,sep="\t", index_col=0)) for i in sorted(os.listdir(os.getcwd())) if i.endswith(".quant.counts")]
for i, j in q_fs:
    j.columns = [i]
full_df = pd.concat(zip(*q_fs)[1], 1)
full_df.to_csv("gene_abundances_raw.tsv", sep="\t", index_label="Gene_Sequence")