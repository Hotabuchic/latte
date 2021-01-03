from cx_Freeze import setup, Executable

executables = [Executable('main_py.py',
                          targetName='latte.exe',
                          base='Win32GUI',
                          icon='1.ico')]

includes = ['PyQt5', 'sys', "sqlite3"]

zip_include_packages = ['PyQt5', 'sys', "sqlite3"]

include_files = ["addEditCoffeeForm.ui",
                 "addEditCoffeeForm_py.py",
                 "coffee.sqlite",
                 "main.ui"]

options = {
    'build_exe': {
        'include_msvcr': True,
        'includes': includes,
        'zip_include_packages': zip_include_packages,
        'build_exe': 'release',
        'include_files': include_files,
    }
}

setup(name='latte',
      version='1.0.0',
      description='latte',
      executables=executables,
      options=options)