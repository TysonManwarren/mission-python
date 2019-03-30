import cx_Freeze

executables = [cx_Freeze.Executable("escape.py")]

cx_Freeze.setup(
    name="Escape Space Adventure",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["racecar.png"]}},
    executables = executables

    )