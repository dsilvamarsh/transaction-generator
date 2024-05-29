from configparser import ConfigParser

def load_db_config(file="database.ini",section="postgresql"):
    parser = ConfigParser()
    parser.read(file)
    config={}
    if parser.has_section(section):
        for kv in parser.items(section):
            config[kv[0]]=kv[1]

    return config
