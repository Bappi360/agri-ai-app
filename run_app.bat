@echo off
title AgriSathi AI - Smart Agricultural Assistant
echo =======================================================================
echo              🌱 AgriSathi AI (কৃষি সাথী এআই)
echo =======================================================================
echo.
echo  [1] PC-তে চালাতে ব্রাউজারে যাবেন: http://localhost:8501
echo  [2] Mobile-এ চালাতে: 
echo      - আপনার মোবাইল ও কম্পিউটার একই Wi-Fi বা Mobile Hotspot-এ রাখুন।
echo      - নিচের "Network URL" (যেমন: http://192.168.x.x:8501) টি মোবাইলের
echo        Chrome/Safari ব্রাউজারে টাইপ করুন।
echo.
echo =======================================================================
echo.
cd /d "%~dp0"
python -m streamlit run app.py --server.address 0.0.0.0 --server.port 8501
pause
