@echo off

bitsadmin /transfer down /download /priority normal "http://192.168.3.16/download/%%E6%%89%%93%%E5%%8D%%B0%%E6%%9C%%BA/3060%%E9%%BB%%91%%E7%%99%%BD/win10%%2064.zip" "c:\print.zip"

cd /d C:\
if  exist print.zip (
    "%rar%" x -ad -y *.zip  C:\Users\libin\Desktop\人人 &del *.zip
)