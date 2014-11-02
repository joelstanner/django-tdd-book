from os import path
import subprocess
THIS_FOLDER = path.dirname(path.abspath(__file__))

# try changing change fab2 to fab if it's not working. - maybe remove the
# "poolbath1@" and ":223" as well
def create_session_on_server(host, email):
    return subprocess.check_output(
        ['fab2',
         'create_session_on_server:email={}'.format(email),
         '--host=poolbath1@{}:223'.format(host),
         '--hide=everything,status',],
        cwd=THIS_FOLDER
    ).decode().strip()

def reset_database(host):
    subprocess.check_call(
        ['fab2', 'reset_database', '--host=poolbath1@{}:223'.format(host)],
        cwd=THIS_FOLDER
    )
