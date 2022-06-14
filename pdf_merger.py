"""
this program is merging pdf files into one pdf file using these modules
"""
import os
from tkinter import Tk
from tkinter import filedialog
from PyPDF2 import PdfFileMerger


class MergePdfFiles:
    """
    class for merging pdf files into one pdf file
    """
    def __init__(self) -> None:
        self.pdfs = []

    def merge(self):
        """
        this function is merging pdf files into one pdf file

        """
        try:
            for file in os.listdir(target_folder):

                if file.lower().endswith('pdf'):
                    self.pdfs.append(os.path.join(target_folder, file))
            merger = PdfFileMerger()
            choice = input("Are You Sure To Merge PDFS (Y/N) ?")
            if choice == "y":
                for pdf in self.pdfs:
                    merger.append(pdf)
                merger.write(os.path.join(target_folder + '/merged.pdf'))
                print("PDF Merged")
                merger.close()
            elif choice == "n":
                exit()
            else:
                print("Enter valid character")
                exit(1)
        except TypeError:
            print('Not Valid ')


if __name__ == '__main__':
    choice2 = input("\nPress 1 for pdf merging:\n press 2 for exit")
    try:
        if choice2 == "1":
            root = Tk()
            root.withdraw()
            target_folder = filedialog.askdirectory()
            obj = MergePdfFiles()
            obj.merge()
        elif choice2 == "2":
            exit(1)
        else:
            print("Something went Wrong")
    except KeyboardInterrupt:
        exit(1)
