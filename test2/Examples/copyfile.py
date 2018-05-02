
from shutil import copyfile

src = "The file source"
dst = "The file destination"

copyfile(src, dst)
"""
Copy the contents of the file named src to a file named dst. The destination location must be writable; otherwise, an IOError exception will be raised. If dst already exists, it will be replaced. Special files such as character or block devices and pipes cannot be copied with this function. src and dst are path names given as strings.
"""









import shutil
shutil.copy2('/src/dir/file.ext', '/dst/dir/newname.ext') # complete target filename given
shutil.copy2('/src/file.ext', '/dst/dir') # target filename is /dst/dir/file.ext



""" 
---------------------------------------------------------------------------
| Function          |Copies Metadata|Copies Permissions|Can Specify Buffer|
---------------------------------------------------------------------------
| shutil.copy       |      No       |        Yes       |        No        |
---------------------------------------------------------------------------
| shutil.copyfile   |      No       |         No       |        No        |
---------------------------------------------------------------------------
| shutil.copy2      |     Yes       |        Yes       |        No        |
---------------------------------------------------------------------------
| shutil.copyfileobj|      No       |         No       |       Yes        |
---------------------------------------------------------------------------
"""




