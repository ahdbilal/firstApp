def main():
    import yaml,os,sys

    param=sys.argv[1]

    current_branch=(sys.stdin.readlines())[0]

    with open("/Users/ahmedbilal/Desktop/GH-AC-Demo/dist_config.yml", 'r') as ymlfile:
        cfg = yaml.safe_load(ymlfile)

    for i in range(0,len(cfg)):
        if cfg[i]['branch'] in current_branch:
            build=cfg[i]['build']
            destinations=cfg[i]['destinations'].split(",")
            mandatory_update=cfg[i]['mandatory_update']
            notify_testers=cfg[i]['notify_testers']
            break
        else:
            build=""
            destinations=""
            mandatory_update=""
            notify_testers=""
    
    if param=="build":
        return print(build)
    elif param=="destinations":
        return print(str(destinations)[1:-1])
    elif param=="mandatory_update":
        return print(mandatory_update)
    elif param=="notify_testers":
        return print(notify_testers)
    else:
        return print(-1)
  
if __name__== "__main__":
  main()
