

def main():
    import yaml,os,sys

    current_branch=(sys.stdin.readlines())[0].split("\n")[0]

    with open("/Users/ahmedbilal/Desktop/GH-AC-Demo/dist_config.yml", 'r') as ymlfile:
        cfg = yaml.safe_load(ymlfile)

    #for i in range(0,len(cfg))
    if current_branch==cfg[0]['branch']:
        cfg[0]['branch']
        cfg[0]['build']
        group=cfg[0]['destinations'].split(",")
        cfg[0]['mandatory_update']
        cfg[0]['notify_testers']
    else:
        group=""
    return print(group[0])
  
if __name__== "__main__":
  main()
