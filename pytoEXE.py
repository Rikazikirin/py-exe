# this is py converter to EXE
from datetime import datetime
import os,sys
import time

now = datetime.now()

def one():
	file = input('enter your file.py to convert to .EXE file >>>> ')
	
	os.system(cls)
        os.system('pip install pyinstaller')
	os.system('pyinstaller ' + file)
	time.sleep(2)
	os.system('pyinstaller -w '+ file)
	time.sleep(2)
	os.system('pyinstaller -F '+ file)
	time.sleep(3)
	FNP = input('enter your photo path + file.py to convert to .EXE file >>>> ')
	os.system('pyinstaller -i '+ FNP)
	os.system('pyinstaller -w -F -i '+ FNP)

def two():
	FNP = input('enter your photo path + file.py to convert to .EXE file >>>> ')
	os.system('pyinstaller -i '+ FNP)
	os.system('pyinstaller -w -F -i '+ FNP)

def main():
	global select
	os.system('cls')
	print("""\033[0;33m
		                                        ,;                  ,;
  t                                                    f#i                 f#i 
  ED.       f.     ;WE.                              .E#t                .E#t
  E#K:      E#,   i#G                               i#W,   :KW,      L  i#W,
  E##W;     E#t  f#f                               L#D.     ,#W:   ,KG L#D.
  E#E##t    E#t G#i           .......            :K#Wfff;    ;#W. jWi:K#Wfff;
  E#ti##f   E#jEW,            GEEEEEEf.          i##WLLLLt    i#KED. i##WLLLLt 
  E#t ;##D. E##E.                                 .E#L         L#W.   .E#L
  E#ELLE##K:E#G                                     f#E:     .GKj#K.    f#E:
  E#L;;;;;;,E#t                                      ,WW;   iWf  i#K.    ,WW;
  E#t       E#t                                       .D#; LK:    t#E     .D#; 
  E#t       EE.                               .j        tt i       tDj      tt 
            t                                 ;f.\033[0m""")
	print(now)
	print("\n")
	print("\033[0;34m[1] Convert your python file to EXE.\033[0m")
	print("\033[0;34m[2] Convert icon only\033[0m")
	select = str(input('\033[0;31mchosse one only >>> \033[0m'))

	if select == "1":
		os.system('cls')
		one()
	elif select == "2":
		os.system('cls')
		two()
	else:
		print(str("\033[0;31m select error : "+ select))
		os.system('exit')
		sys.exit()

main()
