# 파일 다루기, 파일과 폴더 다루기
# 파일 기본
import os
# print(os.getcwd()) # current working directory 현재 작업공간
# os.chdir("1_excel") # 1_excel 으로 작업공간 이동
# print(os.getcwd())
# os.chdir("..") # 부모 폴더로 이동
# print(os.getcwd())
# os.chdir("../..") # 조부모 폴더로 이동
# print(os.getcwd())
# os.chdir("c:/" ) # 주어진 절대경로로 이동
# print(os.getcwd())

# 파일 경로
# file_path = os.path.join(os.getcwd(),"my_file.txt") # 파일 절대 경로 만들기
# print(file_path)
# 파일 경로에서 폴더정보 가져오기
# file_path = os.path.dirname(r"C:\Users\ljj33\OneDrive\바탕 화면\rpa\my_file.txt") # r은 문자 그대로 찍어준다는것(역슬래쉬때문)
# print(file_path)
# 파일 이름은 빠진채로 폴더 정보만 가져왔다.

# 파일 정보 가져오기
# import time
# import datetime
# # 파일 생성 날짜
# ctime = os.path.getctime("2_window/10_log.py")
# print(ctime)
# # 실제 날짜로 바꾸기 strftime없어도 알아볼수 있음
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 수정 날짜.
# mtime = os.path.getmtime("2_window/10_log.py")
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 마지막 접근 날짜
# atime = os.path.getatime("2_window/10_log.py")
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

# # 파일 크기
# file_size = os.path.getsize("2_window/10_log.py")
# print(file_size) # byte\

# 파일 목록 가져오기
# print(os.listdir()) # 모든 폴더, 파일 목록 가져오기
# print(os.listdir("..")) # 주어진 폴더 밑에서 모든 폴더와 파일 목록 가져오기

# 하위폴더, 파일 포함해서 가져오기
# result = os.walk(r"C:\Users\ljj33\OneDrive\바탕 화면\rpa") # 주어진 폴더 밑에있는 모든 폴더와 파일 목록 가져오기
# for root, dirs, files in result:
#     print(root, dirs, files)

# result = os.walk(".") # 현재폴더로부터 가져오기
# for root, dirs, files in result:
#     print(root, dirs, files)

# 만약 폴더 내에서 특정 파일들을 찾으려면
# name = "11_file_system.py"
# result = []
# for root,dirs, files in os.walk("."): # os.getcwd()는 절대경로
#     if name in files:
#         result.append(os.path.join(root, name))

# print(result)

# 어떤 형태의 파일 찾기. * 이용
# 파일 이름이 일치하는지 보기 위해 import fnmatch
# import fnmatch
# pattern = "*.png" # .py로 끝나는 모든 파일 "check*.png" 와 같이 사용가능.  check로 시작하는 png파일 찾기
# result = []
# for root,dirs, files in os.walk("."):
#     # [a.txt, b.txt, c.txt, ...]
#     for name in files:
#         if fnmatch.fnmatch(name, pattern): # 이름과 패턴이 일치하면
#             result.append(os.path.join(root,name))
# print(result)


# 주어진 경로가 파일인지 폴더인지 확인
# print(os.path.isdir("3_web"))
# print(os.path.isfile("3_web"))

# 만약 지정된 경로에 해당하는 파일 및 폴더가 없다면
# print(os.path.isfile("3_we22b"))

# # 주어진 경로가 존재하는지 
# if os.path.exists("3_web"):
#     print("yes")
# else:
#     print("no")

# 파일과 폴더 만들어보기
# 파일 만들기
# open("new_file.txt", "a").close() # 빈파일을 생성

# # 파일명 변경
# os.rename("new_file.txt","new_file_rename.txt")

# 파일을 삭제
# os.remove("new_file_rename.txt")

# 현재경로 기준 폴더 만들기
# os.mkdir("new_folder")
# 절대경로 기준
# os.mkdir(r"C:\Users\ljj33\test") # 절대경로 기준으로 폴더 생성

# os.mkdir("new_folders/a/b/c") #하위 폴더를 가지는 폴더 생성 시도
# # 안된다.
# os.makedirs("new_folders/a/b/c") # 이렇게 해야 된다. 중간 폴더들까지 생성된다.

# 폴더명 변경하기
# os.rename("new_folder","rename")

# 폴더 지우기
# os.rmdir("rename")
# 해당 폴더 안에 내용이 있는 경우 import shutil
import shutil # shell utilities
# shutil.rmtree("rename") # 비어있지 않아도 삭제가능
# 지울폴더 없으면 에러발생

# 파일 복사하기
# 어떤 파일을 폴더안으로 복사하기
# shutil.copy("img.png", "test_folder") # 원본경로, 대상경로
# shutil.copy("img.png", "test_folder/copied_img.png") #이름 바꾸어 복사

# shutil.copyfile("img.png","test_folder/copied2_img.png") # 항상 대상경로가 아닌 파일명만 가능.

# shutil.copy2("img.png", "test_folder/copied3_img.png") # 원본 파일 경로, 대상폴더& 파일경로
# 차이
# copy, copyfile: 메타정보 복사 x
# copy2 : 메타정보 복사
# 메타정보란 수정한 날짜, 생성 날짜와 같은 정보들을 말함.

# 폴더 복사
# shutil.copytree("test_folder","test_folder2") # 안에 있는 내용도 복사

# 폴더 이동
shutil.move("test_folder","test_folder2")
# 이동 대상 폴더가 없으면 폴더명이 변경되는 효과








































