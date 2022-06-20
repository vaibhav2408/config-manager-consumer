import subprocess
from os import path


def __getattr__(name):
    name = name.replace('_', '-')

    def callback():
        file_name = 'scripts/%s.sh' % name
        if path.exists(file_name):
            p = subprocess.Popen(['bash', file_name])
            p.wait()
            out, err = p.communicate()
            if p.returncode != 0:
                raise Exception(f"{file_name} execution failed")
                #  Problem running the script

    return callback
