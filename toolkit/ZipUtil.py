from zipfile import ZipFile

def unzip(zip_file, output="."):
    with ZipFile(zip_file, "r") as z:
        z.extractall(output)

def zip(files, output_zip):
    with ZipFile(output_zip, "w") as z:
        for file in files:
            z.write(file)

def list(zip_file):
    with ZipFile(zip_file, "r") as z:
        return z.namelist()