import cx_Freeze

executables = [cx_Freeze.Executable(
    script="game.py", icon="assets/corona.ico")]

cx_Freeze.setup(
    name="A Saga da Vacina",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files": ["assets"]
        }},
    executables=executables
)