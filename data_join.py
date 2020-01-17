import os
import subprocess

from settings import videos_folder, video_file

class DataJoin:

    def __init__(self):
        parts = self.findParts()
        self.joinParts(parts)

    def findParts(self):

        parts = []

        for root, dirs, files in os.walk(videos_folder):
            for file in files:
                if file.startswith('part_') and file.endswith('.mp4'):
                    parts.append(os.path.join(root, file))
        
        def order_parts(value):
            return int(value[value.index("_") + 1: value.index(".")])

        parts = sorted(parts, key = order_parts)
        return parts

    def joinParts(self, parts):
        
        txtFile = "files.txt"
        txtPath = os.path.join(videos_folder, txtFile)

        with open(txtPath, "w+") as file:

            for part in parts:
                file.write("file '" + part + "'\n")

        os.chdir(videos_folder)
        subprocess.call(["ffmpeg", "-f", "concat", "-safe", "0", "-i", txtFile, "-c", "copy", video_file], shell=True)
