#파일의 기본
import os
#print(os.getcwd()) #current working directory 현재 작업 공간
#os.chdir("..") 상위폴더로 이동하기

#파일 경로 만들기
#file_path = os.path.join(os.getcwd(), "my_file.txt") #절대 경로 생성
#print(file_path)


# 파일 경로에서 폴더 정보 가져오기
#print(os.path.dirname(r"C:\jin\my_file.txt")) # 파일 이름까지가 아니고 폴더까지 가지고옴.

# 파일 정보 가져오기
#import time
#import datetime

#파일의 생성 날짜
#ctime = os.path.getctime(r"C:\jin\10_log.py")
#print(ctime)

# 날짜 정보를 strftime을 통해서 연월일 시분초 형태로 출력
#print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

#파일의 수정 날짜
#mtime = os.path.getmtime(r"C:\jin\10_log.py")
#print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

#파일의 접근 날짜
#atime = os.path.getatime(r"C:\jin\10_log.py")
#print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

#파일 크기
#size = os.path.getsize(fr"C:\jin\10_log.py")
#print(size) # 바이트 단위로 파일 크기 가져오기


#파일 목록 가져오기
#print(os.listdir()) #작업공간 밑에 있는 모든 폴더, 파일 목록들을 가지고와줌
#print(os.listdir("경로"))

#파일 목록 가져오기 (하위 폴더 모두 포함)
#result = os.walk("jin") #주어진 폴더 밑에 있는 폴더, 파일 목록을 가져와줌

#for root, dirs, files in result:
#    print(root, dirs, files)


#만약 폴더 내에서 특정 파일들을 찾으려면?
#name = "11_file_system.py"
#result = []
#for root, dirs, files in os.walk("."):
#    if name in files:
#        result.append(os.path.join(root, name))
#
#print(result)

# 정규표현식을 이용한 파일 찾기 (특정 패턴을 가진 파일들 찾기)
#import fnmatch
#pattern = "*.py" #.py로 끝나는 모든 파일
#result = []
#for root, dirs, files in os.walk("."):
#    for name in files:
#        if fnmatch.fnmatch(name, pattern):  # 이름이 패턴과 일치
#            result.append(os.path.join(root, name))
#print(result)
            


#주어진 경로가 파일인지 폴더인지 확인하기
#print(os.path.isdir("C:\jin")) #jin은 폴더인가?
#print(os.path.isfile("C:\jin")) #jin은 파일인가?

#print(os.path.isdir("11_file_system.py"))
#print(os.path.isfile("11_file_system.py"))


#주어진 경로가 존재하는지
#if os.path.exists("C:\jin"):
#    print("파일 또는 폴더가 존재합니다.")
#else:
#    print("존재하지 않습니다.")


#파일 만들기
#open("new_file.txt","a").close() # 빈파일 생성


#파일명 변경하기
#os.rename("new_file.txt", "new_file_rename.txt") #이름 변경

#파일 삭제하기
#os.remove("new_file_rename.txt")

#폴더 만들기
#os.mkdir("new_folder")

#하위폴더들 만들기
#os.makedirs("new_folders/a/b/c")
 

#폴더명 변경하기
#os.rename("new_folder", "new_folder_rename")

#폴더 지우기
#os.rmdir("new_folder") #폴더 안이 비었을 때만 삭제가능

#파일이 들어있는 폴더들 지우기
import shutil #shell utilities
#shutil.rmtree("new_folders") # 폴더 안이 비어있지 않아도 완전 삭제 가능
#모든 파일이 삭제될 수 있으므로 주의!


#어떤 파일을 폴더 안으로 복사하기
#shutil.copy("11_file_system.py", "test_folder") #원본경로, 대상경로
#shutil.copy("11_file_system.py", "test_folder\copied_11_file_system.py") #변경된 파일명까지 복사
#shutil.copyfile("11_file_system.py", "test_folder\copied_11_file_system.py") #파일만 쓸 수 있음.

#copy, copyfile : 메타정보 복사 x
#copy2 : 메타정보 복사 o
#shutil.copy2("11_file_system.py", "test_folder\copy2.py")


#폴더 복사
#shutil.copytree("test_folder", "test_folder2") #원본 폴더 경로, 대상 폴더 경로 (폴더 경로만 적어줘야 함.)

#폴더 이동 (폴더 명이 변경되는 효과도 낼 수 있음.)
#shutil.move("test_folder", "test_folder2")
