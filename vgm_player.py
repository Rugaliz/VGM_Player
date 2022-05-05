import os
import sys
from random import randrange

walk_dir = sys.argv[1]

# print('walk_dir = ' + walk_dir)

# If your current working directory may change during script execution, it's recommended to
# immediately convert program arguments to an absolute path. Then the variable root below will
# be an absolute path as well. Example:
# walk_dir = os.path.abspath(walk_dir)
print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))
vgm_list = []
for root, subdirs, files in os.walk(walk_dir):
    # print('--\nroot = ' + root)
    list_file_path = os.path.join(root, 'my-directory-list.txt')
    # print('list_file_path = ' + list_file_path)

    with open(list_file_path, 'wb') as list_file:
        # for subdir in subdirs:
            # print('\t- subdirectory ' + subdir)

        for filename in files:
            file_path = os.path.join(root, filename)
            if ".vgz" in file_path or ".vgm" in file_path:
                # print('\t- file %s (full path: %s)' % (filename, file_path))
                print(file_path)
                vgm_list.append(file_path)
            # with open(file_path, 'rb') as f:
            #     f_content = f.read()
            #     list_file.write(('The file %s contains:\n' % filename).encode('utf-8'))
            #     list_file.write(f_content)
            #     list_file.write(b'\n')
nsong = len(vgm_list)

if nsong == 0:
    exit("No songs to play!")

while nsong > 0:
    song_index = randrange(nsong)
    os.system(f"env SDL_VIDEODRIVER=dummy mame vgmplay -quik '{vgm_list[song_index]}'  -video none -seconds_to_run 180")
    vgm_list.remove(vgm_list[song_index])
    nsong = len(vgm_list)
