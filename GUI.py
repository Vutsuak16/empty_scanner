import Tkinter,tkFileDialog
import file_removal
root = Tkinter.Tk()
dir = tkFileDialog.askdirectory(parent=root,title='Choose a directory')
file_removal.put_path(dir)