@echo off
title ejemplo4
set/p nombre= ¿ cual es tu nombre?:
echo.
pause
echo.
set/p edad= ¿ y que edad tienes?:
echo.
pause
echo.
set/p vive= ¿ y donde vives?
echo.
pause
cls
echo te llamas %nombre% y tienes %edad% anios y vives en %vive%
echo.
pause > nul
exit