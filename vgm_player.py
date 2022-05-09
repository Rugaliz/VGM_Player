import os
import sys
from random import randrange

try:
    work_dir = sys.argv[1]
except:
    work_dir = "."

print('work_dir (absolute) = ' + os.path.abspath(work_dir))
vgm_list = []

for root, subdirs, files in os.walk(work_dir):
    list_file_path = os.path.join(root, 'my-directory-list.txt')
    # print('list_file_path = ' + list_file_path)

    for filename in files:
        file_path = os.path.join(root, filename)
        if ".vgz" in file_path or ".vgm" in file_path:
            # print(file_path)
            vgm_list.append(file_path)

nsong = len(vgm_list)

if nsong == 0:
    exit("No songs to play!")

while nsong > 0:
    song_index = randrange(nsong)
    print(f"Playing {vgm_list[song_index]}")
    os.system(f"env SDL_VIDEODRIVER=dummy mame vgmplay -quik \"{vgm_list[song_index]}\"  -video none -seconds_to_run 180")
    vgm_list.remove(vgm_list[song_index])
    nsong = len(vgm_list)
    print(f"{nsong} songs remaining")
