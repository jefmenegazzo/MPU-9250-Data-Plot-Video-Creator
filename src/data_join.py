import os
import subprocess

from settings import video_file, videos_folder

class DataJoin:

    """ This class concatenate all the generated video parts, transforming all parts into a single MP4 file. """

    def run(self):
        """ Perform the process to find video parts and joining them. """

        parts = self.__findParts()
        parts = self.__orderParts(parts)
        self.__joinParts(parts)

    def __findParts(self):
        """ 
        Find the video parts. 
    
        Returns:
            list: a list with full path of each video part file.
        """

        parts = []

        for root, dirs, files in os.walk(videos_folder):
            for file in files:
                if file.startswith('part_') and file.endswith('.mp4'):
                    full_path = os.path.join(root, file)
                    parts.append(full_path)

        return parts

    def __orderParts(self, parts):
        """ 
        Sort the video parts by sequence. 

        Args:
            parts (list): list with full path of each video part file.
    
        Returns:
            list: a sorted list with full path of each video part file.
        """

        def orderFiles(value):
            return int(value[value.rindex("_") + 1:value.rindex(".")])

        parts = sorted(parts, key=orderFiles)
        return parts

    def __joinParts(self, parts):
        """
        Join the video parts into a single MP4 file. 
        The output is saved in **settings.videos_folder** with filename **settings.video_file**.

        Args:
            parts (list): list with full path of each video part file.
        """

        txtFile = "files.txt"
        txtPath = os.path.join(videos_folder, txtFile)

        with open(txtPath, "w+") as file:
            for part in parts:
                file.write("file '" + part + "'\n")

        os.chdir(videos_folder)
        subprocess.call(["ffmpeg", "-f", "concat", "-safe", "0", "-i", txtFile, "-c", "copy", video_file], shell=True)
