from os import makedirs
from random import random
import glob
import os


def generate_file_data():
    lines = [f"c{u}" for u in range(10)]
    lines += [",".join([str(random()) for _ in range(10)]) for _ in range(10_000)]
    return "\n".join(lines)


def generate_random_files(nfiles=1_000, path="/content/tmp"):
    from tqdm import tqdm

    # create a local directory to save files
    makedirs(path, exist_ok=True)

    # create all files
    for i in tqdm(range(nfiles), f"Generate {nfiles} random files"):
        with open(f"{path}/data-{i:04d}.csv", "w") as handle:
            handle.write(generate_file_data())


def get_random_filenames(nfiles=1_000, force_generation=False, path="/content/tmp"):

    if force_generation:
        os.system(f"rm -rf {path}/*")

    if len(glob.glob(f"{path}/*")) == 0:
        generate_random_files(nfiles=nfiles, path=path)
    return glob.glob(f"{path}/*")
