from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


FUNCTION_CHOICES = [("None", "None"), ("center", "Center"), ("split_tcr", "Split TCR"),
                    ("clean_docking_count_non_tcr", "Clean Count"), ("clean_tcr_count_trim", "Trim TCR"),
                    ("split_mhc", "Split MHC"), ("split_p", "Split Peptide"), ("split_pmhc", "Split pMHC"),
                    ("clean_pdb", "Full Clean")]

PDB_CHOICES = []

with open("app/20221031_0310870_summary.tsv", "r") as f:
    for line in f:
        pdb = line.split("\t")[0]
        if pdb == "pdb":
            pass
        else:
            PDB_CHOICES.append((pdb, pdb))

PDB_CHOICES = sorted(PDB_CHOICES, key=lambda x: x[0])


class TcrRequest(models.Model):
    pdb = models.CharField(max_length=4, choices=PDB_CHOICES, blank=False)
    action1 = models.CharField(max_length=50, choices=FUNCTION_CHOICES, blank=False)
    action2 = models.CharField(max_length=50, choices=FUNCTION_CHOICES, blank=False)
    action3 = models.CharField(max_length=50, choices=FUNCTION_CHOICES, blank=False)

    def __str__(self):
        return self.pdb + " " + self.action1
