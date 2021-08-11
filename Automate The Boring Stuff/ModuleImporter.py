# Safely import third party modules
import importlib, os, sys

def module_importer(module_name, package_name):
    '''(str, str) -> ModuleType
    Read the module name as a string and try to import it normally,
    failing which tries to download required package and return the module.
    '''
    try:
        return importlib.import_module(module_name)
    except ModuleNotFoundError:
        print('Resolving dependencies...')
        print(f'Required Module: {package_name}')
        try:
            os.system('pip install ' + package_name)
            return importlib.import_module(module_name)
        except Exception as e:
            sys.exit(str(e))
