import os
import re
import sys
import logging as lg

from core.utils import setup_logger, validate_semver
from argparse import ArgumentParser, Namespace
from logging import DEBUG, INFO
from core.tui import TerminalUserInterface

def parse_args() -> Namespace:
    argparser = ArgumentParser(description='Handler, Helper, Manager for all your\'s awesome projects')
    custom_subparsers = argparser.add_subparsers(dest='command', help='Handle commands', required=True)
    
    init_parser = custom_subparsers.add_parser('init', help='Initialize new project')
    init_parser.add_argument('-N', '--name', default='New Project', type=str, help='New project name')
    init_parser.add_argument('-V', '--version', default='0.1.0', type=str, help='New project version')
    init_parser.add_argument('-L', '--languages', default='Python3,C++', type=str, help='New project languages')
    init_parser.add_argument('-F', '--frameworks', default='flask,tkinter', type=str, help='New project frameworks')
    init_parser.add_argument('-D', '--description', default='Empty description', type=str, help='New project description')
    
    info_parser = custom_subparsers.add_parser('info', help='Get project info')
    
    argparser.add_argument('-v', '--verbose', action='store_true', help='Verbose mode')
    
    return argparser.parse_args()

def main() -> int | None:
    
    args = parse_args()
    logger = setup_logger(name='projectshandler', level=(DEBUG if args.verbose else INFO))
    
    # INIT command parse
    if args.command == 'init':
        args.name = str(args.name).strip()
        args.path = sys.path[0]
        
        if not validate_semver(args.version):
            logger.warning(f'Version {args.version} seems like incorrect (SemVer)')
            
        languages = args.languages.split(',')
        if not languages or ((len(languages) == 1) and (not languages[0])):
            args.languages = ['None']
            
        frameworks = args.frameworks.split(',')
        if not frameworks or ((len(frameworks) == 1) and (not frameworks[0])):
            args.frameworks = ['None']
        
        TerminalUserInterface(args).init_command()
    
if __name__ == '__main__':
    sys.exit(main())