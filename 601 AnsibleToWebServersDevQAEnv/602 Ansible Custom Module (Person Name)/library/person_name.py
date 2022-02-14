#!/bin/env python

from ansible.module_utils.basic import *
import os

def personName(name):
  name = "Hello and Welcome " + name
  return name

def main():

  fields = {
  "name": {"required": True, "type": "str"}
  }
  module = AnsibleModule(argument_spec=fields)
  name = os.path.expanduser(module.params['name'])
  newPersonName = personName(name)
  module.exit_json(msg=newPersonName)

if __name__ == '__main__':
    main()