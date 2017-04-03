import os
import six
import sys
import json
import tempfile
import subprocess
import urllib.request

def J3(data = None, **kwargs):
    # query github.com releases API to determine latest release
    url = None
    id = None
    
    try:
        response = urllib.request.urlopen("https://api.github.com/repos/Project-Platypus/J3/releases/latest")
        content = json.loads(response.read().decode("UTF-8"))
        
        for asset in content["assets"]:
            if asset["name"] == "J3-Full.jar":
                id = str(asset["id"])
                url = asset["browser_download_url"]
                
        if id is None or url is None:
            print("Unable to access latest release info on github.com", file=sys.stderr)
        
    except urllib.error.URLError:
        print("Unable to connect to github.com; are you connected to the internet?", file=sys.stderr)
    
    # ensure the ~/.j3 folder exists
    home_dir = os.path.expanduser("~")
    j3_dir = os.path.join(home_dir, ".j3")
    
    if not os.path.exists(j3_dir):
        os.makedirs(j3_dir)
        
    # if we could not locate the latest release on github.com, scan the ~/.j3
    # folder for existing copies
    if id is None:
        ids = [f for f in os.listdir(j3_dir) if os.path.isdir(os.path.join(j3_dir, f))]
        max_id = -1
        
        for id in ids:
            try:
                idv = int(id)
                if idv > max_id:
                    max_id = idv
            except:
                pass
            
        if max_id >= 0:
            id = str(max_id)
    
    # now attempt to locate the folder containing the latest J3 install
    install_dir = os.path.join(j3_dir, id)
    j3_path = None
    
    if os.path.exists(install_dir):
        j3_path = os.path.join(install_dir, "J3-Full.jar")
    else:
        os.makedirs(install_dir)
        
        try:
            urllib.request.urlretrieve(asset["browser_download_url"], j3_path)
            j3_path = os.path.join(install_dir, "J3-Full.jar")
        except urllib.error.URLError:
            print("Unable to download the latest J3 version from github.com", file=sys.stderr)
       
    # raise an error if we still can't locate J3     
    if j3_path is None or not os.path.exists(j3_path):
        raise RuntimeError("Unable to locate or download J3")
    
    # create a temporary file storing the plot contents
    if data is None:
        os.system(r'java -cp "%s" j3.GUI' % (os.path.abspath(j3_path),))
    else:
        if isinstance(data, six.string_types):
            filename = data
        else:
            temp = os.path.join(j3_dir, "temp")
            
            if not os.path.exists(temp):
                os.makedirs(temp)
                
            (_, filename) = tempfile.mkstemp(suffix=".csv", dir=temp)
            saved = False 
            
            try:
                import pandas as pd
                    
                if isinstance(data, pd.DataFrame):
                    data.to_csv(filename, **kwargs)
                    saved = True
            except:
                pass
            
            if not saved:
                try:
                    import numpy as np
                        
                    np.savetxt(filename, data, delimiter=",", **kwargs)
                    saved = True
                except:
                    pass
                
            if not saved:
                raise ValueError("Unsupported data type, must be a Pandas DataFrame or Numpy Array")

        os.system(r'java -cp "%s" j3.GUI "%s"' % (os.path.abspath(j3_path), os.path.abspath(filename)))
        