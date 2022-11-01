import os
from PDBS.PDB_Tools_V3 import PdbTools3
from TCRpdbTools.settings import BASE_DIR
from pypdb.clients.pdb.pdb_client import *


def get_pdb(pdb_id):
    pdb_loc = pdb_id + ".pdb"
    with open(pdb_loc, "w") as f:
        pdb_file = get_pdb_file(pdb_id, compression=False)
        f.write(pdb_file)
    return pdb_loc


def process_modification(context):
    # Change working directory while processing PDB
    os.chdir(str(BASE_DIR) + "/PDBS/")

    # Grab PDB from RCSB DB
    pdb = context["pdb"]
    pdb_loc = get_pdb(pdb)

    # Perform actions
    tool = PdbTools3(pdb_loc)
    for action in context["actions"]:
        if action == "center":
            tool.center(pdb_loc)
        if action == "clean_docking_count_non_tcr":
            tool.clean_docking_count(pdb_loc)
        if action == "split_tcr":
            tool.split_tcr(pdb_loc)
        if action == "clean_tcr_count_trim":
            tool.clean_tcr_count_trim()
        if action == "split_mhc":
            tool.split_mhc()
        if action == "split_p":
            tool.split_p()
        if action == "split_pmhc":
            tool.split_pmhc(pdb_loc)
        if action == "clean_pdb":
            tool.clean_pdb()

    os.chdir(str(BASE_DIR))
    return str(BASE_DIR) + "/PDBS/" + pdb_loc
