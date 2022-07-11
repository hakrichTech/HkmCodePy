import os
import argparse

def hkm_config_file_yaml(conf:str = 'none'):
    confFile = "configuration.yaml"
    parent_dir = os.getcwd()
    pathFile = os.path.join(parent_dir, confFile)
    if os.path.isfile(pathFile):
        if conf != 'none':
            with open(pathFile, 'a') as f:
                f.write("""
# {0}

{1}:
#    configProperty: value
                """.format(conf.upper(),conf))
                f.close()


    else:
        with open(pathFile, 'a') as f:
            if conf == 'none':

                f.write("""# APPLICATION
App:
    baseURL: http://localhost
    port: 8080
    defaultLocale: fr
                """)
            else:
                f.write("""
# {0}
{1}:
#    configProperty: value
                """.format(conf.upper(),conf))
            f.close()

def hkm_config_file(filename:str):
    # Directory
    directory = "Hkm_Bin"
    initFile = "{0}.py".format(filename)
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, directory)
    pathFile = os.path.join(path, initFile)
    if os.path.isfile(pathFile):
        print('{0} File exists in this CWD!'.format(initFile))
    else:
        with open(pathFile, 'x') as f:
            f.write("""from hkmConfig.Base import Config

class {0}(Config):
    def RUN(self):
        self.config_file = '{0}'
            """.format(filename))
            f.close()
        




def hkm_bin():
    # Directory
    directory = "Hkm_Bin"
    initFile = "__init__.py"
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, directory)
    pathFile = os.path.join(path, initFile)
    # mode
    mode = 0o666
    try: 
        if os.path.isdir(path):
            print('Hkm_Bin Directory exists in this CWD!')
        else:
            os.mkdir(path,mode) 
            if os.path.isfile(pathFile):
                print('Hkm_Bin/__init__.py File exists in this CWD!')
            else:
                with open(pathFile, 'x') as f:
                    f.write('#Create a new text file!')
                    f.close()
                
        
    except OSError as error: 
        print(error)  

    hkm_config_file_yaml()

def main():
    # Create the parser

    hkmconfig_parser = argparse.ArgumentParser(
        prog='hkmconfig',
        usage='%(prog)s [options] init',
        description='hkmconfig configuration system: The best way to configure your project settings',
        epilog='Enjoy the program! :)',
        allow_abbrev=True,
        fromfile_prefix_chars='@')
    hkmconfig_parser.version = '0.0.3'

    hkmconfig_parser.add_argument(
        '-c',
        '--configuration',
        action='store',
        type=str,
        help='Initializing the configuration file',
        default="none")

    hkmconfig_parser.add_argument('-i',
                       '--init',
                       action='store_true',
                       help='Initializing the configuration file')



    # Execute parse_args()
    args = hkmconfig_parser.parse_args()

    if args.init :
        hkm_bin()
    if args.configuration != 'none':
        confFilename = args.configuration.capitalize()
        hkm_config_file(confFilename)
        hkm_config_file_yaml(confFilename)

