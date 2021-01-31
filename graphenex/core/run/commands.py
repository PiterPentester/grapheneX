#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from graphenex.core.run.helpers import check_os, get_modules, \
    mod_json_file, get_forbidden_namespaces, get_mod_json, get_presets
from graphenex.core.utils.logcl import GraphenexLogger
#from graphenex.core.cli.help import Help

from terminaltables import AsciiTable
from PyInquirer import prompt, Validator, ValidationError
import textwrap
import secrets
import random
import json
import os
import re

logger = GraphenexLogger(__name__)

class ShellCommands():


    def do_harden(self, arg):
        argument = arg.split("/")
        self.namespace = argument[0]
        self.module = argument[1]
        self.modules = get_modules()

        """Execute the hardening command"""

        if not (self.module and self.namespace):
            logger.error('Select a module/namespace.')
        else:
            try:
                hrd = self.modules[self.namespace][self.module]
                out = hrd.execute_command()
                print(out)
                logger.info("Hardening command executed successfully.")
            except PermissionError:
                err_msg = "Insufficient permissions for hardening."
                if check_os():
                    err_msg += " Get admin rights and rerun the grapheneX."
                else:
                    err_msg += " Try running the grapheneX with sudo."
                logger.error(err_msg)
            except Exception as e:
                logger.error("Failed to execute hardening command. " + str(e))
