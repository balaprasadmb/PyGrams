import os
import shutil

dir_path = r'/home/bborade/jenkins backup/jenkins20_21'

for cur_path, cur_dir, files in os.walk(dir_path):
    for fname in files:
        if fname in ["report.html", "output.xml", "build.xml", "changelog.xml", "log", "robot_results.xml"] or str(fname).endswith(".class"):
            print(os.path.join(cur_path, fname))
            os.remove(os.path.join(cur_path, fname))
    for dname in cur_dir:
        if dname == "CVS":
            print(os.path.join(cur_path, dname))
            shutil.rmtree(os.path.join(cur_path, dname))

print("Cleaned Files")
