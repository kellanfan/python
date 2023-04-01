import os
from multiprocessing import Pool,Manager

def findDir(rootDir, targetDir, q):
    for root, _, _ in os.walk(rootDir):
        if targetDir in root and root.endswith(targetDir):
            q.put(root)

def delFiles(q):
    for root, dirs, files in os.walk(q.get()):
        for name in files:
            os.remove(os.path.join(root,name))
            print('delete file [{}] done'.format(os.path.join(root,name)))
        for name in dirs:
            os.remove(os.path.join(root,name))
            print('delete dir [{}] done'.format(os.path.join(root,name)))

def main():
    rootDirs = [r'C:\Users\Administrator\Documents\WeChat Files', r'C:\Users\Administrator\Documents\WXWork']
    targetDirs = ['File', 'Image', 'Video']
    q = Manager().Queue()
    mypool = Pool()
    for targetDir in targetDirs:
        for rootDir in rootDirs:
            mypool.apply(findDir,(rootDir, targetDir, q,))
    mypool.apply(delFiles, (q,))
    mypool.close()
    mypool.join()
    read(q)
    
if __name__ == '__main__':
    main()