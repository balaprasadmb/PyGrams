'''
Created on 17-May-2023

@author: bprasad
'''
import configparser

config = configparser.ConfigParser()

'''['BOOLEAN_STATES', 'NONSPACECRE', 'OPTCRE', 'OPTCRE_NV', 'SECTCRE', '_DEFAULT_INTERPOLATION', '_MutableMapping__marker',
'_OPT_NV_TMPL', '_OPT_TMPL', '_SECT_TMPL', '__abstractmethods__', '__class__', '__contains__', '__delattr__', '__delitem__',
'__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__',
'__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
'__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__slots__', '__str__', '__subclasshook__',
'__weakref__', '_abc_cache', '_abc_negative_cache', '_abc_negative_cache_version', '_abc_registry', '_allow_no_value',
'_comment_prefixes', '_convert_to_boolean', '_converters', '_defaults', '_delimiters', '_dict', '_empty_lines_in_values',
'_get', '_get_conv', '_handle_error', '_inline_comment_prefixes', '_interpolation', '_join_multiline_values', '_optcre',
'_proxies', '_read', '_sections', '_strict', '_unify_values', '_validate_value_types', '_write_section', 'add_section',
'clear', 'converters', 'default_section', 'defaults', 'get', 'getboolean', 'getfloat', 'getint', 'has_option', 'has_section',
'items', 'keys', 'options', 'optionxform', 'pop', 'popitem', 'read', 'read_dict', 'read_file', 'read_string', 'readfp',
'remove_option', 'remove_section', 'sections', 'set', 'setdefault', 'update', 'values', 'write']'''
config.read('demo.properties')
print(config.sections())
db_url=config.get("db", "db_url")
user=config.get("db", "user")
password=config.get("db", "password")

print(db_url)
print(user)
print(password)