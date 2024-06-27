from pathlib import Path


def get_file(path):
    """
    returns the absolute path of a file
    :var
    str path
        the file path within the working dir
    :returns
    PureWindowsPath or PurePosixPath object
        type depends on the operating system in use
    """
    def get_project_root() -> Path:
        """Returns project root folder."""
        return Path(__file__).parent.parent.parent

    return str(get_project_root().joinpath(path))


def get_lst_path(lst_files):
    new_lst = []
    for filename in lst_files:
        new_lst.append(get_file(filename))

    return new_lst


time_files = get_lst_path(["data/control_G_01.tif", "data/control_G_33.tif", "data/control_G_66.tif",
                           "data/control_R_01.tif", "data/control_R_33.tif", "data/control_R_66.tif",
                           "data/sample_G_01.tif", 'data/sample_G_33.tif', 'data/sample_G_66.tif',
                           'data/sample_R_01.tif', 'data/sample_R_33.tif', 'data/sample_R_66.tif'])
