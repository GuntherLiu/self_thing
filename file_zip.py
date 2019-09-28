import zipfile
import os


class DoZip:

    def writeAllFileToZip(self, absDir, zipFile):
        for f in os.listdir(absDir):
            absFile = os.path.join(absDir, f)
            if os.path.isdir(absFile):
                relFile = absFile[len(os.getcwd()) + 1:]
                zipFile.write(relFile)
                self.writeAllFileToZip(absFile, zipFile)
            else:
                relFile = absFile[len(os.getcwd()) + 1:]
                zipFile.write(relFile)
        return

    def do_zip(self, file_name, goal_dir):
        zip_file_path = os.path.join(os.getcwd(), file_name)
        zip_file = zipfile.ZipFile(zip_file_path, "w", zipfile.ZIP_DEFLATED)
        abs_dir = os.path.abspath(goal_dir)
        self.writeAllFileToZip(abs_dir, zip_file)
