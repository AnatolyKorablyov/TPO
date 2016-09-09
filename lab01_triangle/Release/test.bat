echo 1
lab01_triangle.exe "3" "4" "5" >> out1.txt
if ERRORLEVEL 1 goto testFailed
fc.exe "out1.txt" "standart\VersatileRectangular.txt"
if ERRORLEVEL 1 goto testFailed

echo 2
lab01_triangle.exe "4" "4.55" "2.97" >> out2.txt
if ERRORLEVEL 1 goto testFailed
fc.exe "out2.txt" "standart\VersatileAcute.txt"
if ERRORLEVEL 1 goto testFailed

echo 3
lab01_triangle.exe "2" "3" "5" >> out3.txt
if ERRORLEVEL 1 goto testFailed
fc.exe "out3.txt" "standart\VersatileObtuse.txt"
if ERRORLEVEL 1 goto testFailed

echo 4
lab01_triangle.exe "2" "3" "6" >> out4.txt
if ERRORLEVEL 1 goto testFailed
fc.exe "out4.txt" "standart\NotTriangle.txt"
if ERRORLEVEL 1 goto testFailed

echo 5
lab01_triangle.exe "0" "0" "0" >> out5.txt
if ERRORLEVEL 1 goto testFailed
fc.exe "out5.txt" "standart\ZeroSide.txt"
if ERRORLEVEL 1 goto testFailed

echo 6
lab01_triangle.exe "3" "3" "3" >> out6.txt
if ERRORLEVEL 1 goto testFailed
fc.exe "out6.txt" "standart\EquilateralAcute.txt"
if ERRORLEVEL 1 goto testFailed

echo 7
lab01_triangle.exe "3" "3" "6" >> out7.txt
if ERRORLEVEL 1 goto testFailed
fc.exe "out7.txt" "standart\IsoscelesObtuse.txt"
if ERRORLEVEL 1 goto testFailed

echo 8
lab01_triangle.exe "4" "4" "5.66" >> out8.txt
if ERRORLEVEL 1 goto testFailed
fc.exe "out8.txt" "standart\IsoscelesRectangular.txt"
if ERRORLEVEL 1 goto testFailed

echo 9
lab01_triangle.exe "4" "4" "3" >> out9.txt
if ERRORLEVEL 1 goto testFailed
fc.exe "out9.txt" "standart\IsoscelesAcute.txt"
if ERRORLEVEL 1 goto testFailed

echo 10
lab01_triangle.exe "4" "4" >> out10.txt
if ERRORLEVEL 1 goto testFailed
fc.exe "out10.txt" "standart\ErrorParameters.txt"
if ERRORLEVEL 1 goto testFailed

echo 11
lab01_triangle.exe "4" "4" "-1" >> out11.txt
if ERRORLEVEL 1 goto testFailed
fc.exe "out11.txt" "standart\ZeroSide.txt"
if ERRORLEVEL 1 goto testFailed

echo 12
lab01_triangle.exe "a" "b" "c" >> out12.txt
if ERRORLEVEL 1 goto testFailed
fc.exe "out12.txt" "standart\NotNumber.txt"
if ERRORLEVEL 1 goto testFailed

echo OK
exit /B

:testFailed
echo Testing failed
exit /B