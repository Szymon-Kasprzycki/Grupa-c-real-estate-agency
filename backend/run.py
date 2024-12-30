import os
from subprocess import check_output, call
from argparse import ArgumentParser

FIND_COMMAND = 'where' if os.name == 'nt' else 'which'
VENV_PATH = '.venv/Scripts' if os.name == 'nt' else '.venv/bin'

for entry in ['py', 'python', 'python3']:
    if 'could not find' not in check_output([FIND_COMMAND, entry]).decode('utf-8').lower():
        PYTHON_PATH = check_output([FIND_COMMAND, entry]).decode('utf-8').strip()
        break
else:
    raise Exception('Python not found!')


def main():
    parser = ArgumentParser(description='Please make sure to have python and virtualenv installed!')
    parser.add_argument('-s', '--setup', action='store_true', help='Setup clean project')
    parser.add_argument('-r', '--run', action='store_true', help='Run the server')
    parser.add_argument('-d', '--rerun-db', action='store_true', help='Recreate the database')
    args = parser.parse_args()

    check_dependencies()
    print(f'Using python from {PYTHON_PATH}')

    if args.setup:
        if not os.path.exists(VENV_PATH):
            prepare_venv()
        else:
            raise Exception('Virtual environment already exists!')
        rerun_db()
    elif args.run:
        if os.path.exists(VENV_PATH):
            call([f'{VENV_PATH}/python', 'manage.py', 'runserver'])
        else:
            raise Exception('Virtual environment not found!')
    elif args.rerun_db:
        rerun_db()
    else:
        parser.print_help()


def check_dependencies():
    # silently check if pip is installed (without printing to console)
    if 'could not find' in check_output([PYTHON_PATH, '-m', 'pip', '--no-cache-dir', '--no-python-version-warning', '--disable-pip-version-check']).decode('utf-8').lower():
        raise Exception('Python pip module not found!')

    # check if virtualenv is installed
    if 'virtualenv' not in check_output([PYTHON_PATH, '-m', 'pip', 'list']).decode('utf-8').lower():
        raise Exception('Virtualenv package not found!')


def prepare_venv():
    call([PYTHON_PATH, '-m', 'venv', VENV_PATH.split('/')[0]])
    call([f'{VENV_PATH}/pip', 'install', '-r', 'requirements.dev.txt'])
    print('Virtual environment created and dependencies installed!')


def run_server():
    call([f'{VENV_PATH}/python', 'manage.py', 'runserver'])


def rerun_db():
    if os.path.exists('db.sqlite3'):
        os.remove('db.sqlite3')
    call([f'{VENV_PATH}/python', 'manage.py', 'makemigrations'])
    call([f'{VENV_PATH}/python', 'manage.py', 'migrate'])
    call([f'{VENV_PATH}/python', 'manage.py', 'createsuperuser', '--username', 'admin', '--email', 'admin@example.com', '--noinput'])
    print('Clean database recreated!')


if __name__ == '__main__':
    main()
