import os

dir_path = r'/home/bborade/Documents/AutoPorts/Dec/'

for cur_path, cur_dir, files in os.walk(dir_path):
    for fname in files:
        if fname in ["report.html", "output.xml"]:
            print(os.path.join(cur_path, fname))
            os.remove(os.path.join(cur_path, fname))

print("Cleaned Files")
