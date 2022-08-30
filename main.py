import os
import time
import wmi

def scanFolder(selectDrive):
    path = selectDrive.upper() + ":"
    for root, dirs, files in os.walk(path):
        print(root)
        tenThuMuc = root[2:].split("\\")[-1]
        if len(tenThuMuc) == 0 and root[0:1] == selectDrive.upper():
            tenThuMuc = getDriveName(selectDrive)
        print("ten thu muc: " + tenThuMuc)
        for name in files:
            xulyFile(root, name, tenThuMuc)
        for name in dirs:
            xulyFolder(root,name)
            print("\t" + name)
        time.sleep(1)
        print("--------")

def xulyFile(root, name, tenThuMuc):
    a = name.split(".")
    b = len(name) - len(a[-1]) - 1
    if b>30:
        print("\t-" + name[:30] + "...(" + a[-1] + ")",end=" ")
    else:
        print("\t-" + name[:b].ljust(33,'-') + "(" + a[-1] + ")", end=" ")
    print(os.path.getsize(root + "\\" + name), end=" ")
    print("byte")
    if name[:b] == tenThuMuc:
        if a[-1].lower() == "lnk" \
                or a[-1].lower() == "exe":
            print("\t" + "--->xu ly no")
            xulydelcmd(root+"\\"+name)
            try:
                ghiFileLog(root, name)
            except:
                print("khuc nay loi a nha")
    if name =="New Folder.exe" or name=="system3_.exe":
        print("\t" + "--->xu ly no")
        xulydelcmd(root + "\\" + name)
        try:
            ghiFileLog(root, name)
        except:
            print("khuc nay loi a nha")

def ghiFileLog(root,name):
    file=open("Log.txt", "a")
    print("\t---"+"Luu file log")
    file.writelines(time.strftime("%m/%d/%Y, %H:%M:%S",time.localtime())+ " "+ root + " | " +name+ "\n")
    file.close()
def getDriveName(selectDrive):
    c = wmi.WMI()
    a = c.Win32_LogicalDisk()
    for drive in c.Win32_LogicalDisk():
        if drive.Caption[0] == selectDrive.upper():
            b = drive.VolumeName
    return b
def xulypath(path):
    path1=""
    j=0
    for i in path:
        path1=path1+i
        j=j+1
        if i=="\\":
            path1=path1+"\\"
    return path1
def xulydelcmd(path):
    kiemtrafile(path)
    cmd="del \""+path+"\""
    print(cmd)
    os.system(cmd)
    kiemtrafile(path)
def kiemtrafile(path):
    if(os.path.exists(path)==True):
        print("TON TAI")
    else:
        print("KHONG TON TAI")
def xulyFolder(root,name):
    pass
# path="d:\\new text document.txt"
# path="d:\\new folder.exe"
# print("size: ")
# print(os.path.getsize(path))
# path="d:\\system3_.exe"
# print("size: ")
# print(os.path.getsize(path))
# print("path: "+path)
# cmd=xulydelcmd(path)
# os.system("md d:\\testFolder2")
# os.system("del \"d:\\New Text Document.txt\"")
# os.system("del \"d:\\new text document.txt\"")
print(time.strftime("%m/%d/%Y, %H:%M:%S",time.localtime()))
c = wmi.WMI()
for drive in c.Win32_LogicalDisk():
    # print(drive)
    print(drive.Caption, drive.VolumeName)

a = c.Win32_LogicalDisk()
selectDrive = input("Enter your select disk: ")
print('selectDrive is: ', selectDrive)
scanFolder(selectDrive)
