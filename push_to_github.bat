@echo off
title Push AgriSathi AI to GitHub
echo =======================================================================
echo          🌱 Push AgriSathi AI to GitHub for Streamlit Cloud
echo =======================================================================
echo.
echo  GitHub-এ নতুন একটি পাবলিক রিপোজিটরি তৈরি করুন (যেমন: agri-ai-app)
echo  এরপর সেই রিপোজিটরির লিংকটি কপি করে নিচে পেস্ট করুন।
echo.
set /p REPO_URL="Enter your GitHub Repository URL (e.g. https://github.com/username/agri-ai-app.git): "

if "%REPO_URL%"=="" (
    echo.
    echo [ERROR] কোনো রিপোজিটরি লিংক দেওয়া হয়নি!
    pause
    exit /b
)

echo.
echo Git Remote যোগ করা হচ্ছে...
git remote remove origin 2>nul
git remote add origin %REPO_URL%

echo ব্রাঞ্চ main হিসেবে সেট করা হচ্ছে...
git branch -M main

echo GitHub-এ আপলোড করা হচ্ছে...
git push -u origin main

echo.
if %errorlevel% equ 0 (
    echo =======================================================================
    echo  [SUCCESS] কোড সফলভাবে GitHub-এ আপলোড সম্পন্ন হয়েছে!
    echo  এখন share.streamlit.io এ গিয়ে Deploy করুন।
    echo =======================================================================
) else (
    echo [NOTICE] যদি লগইন না করা থাকে, ব্রাউজারে GitHub অথেনটিকেশন দিন।
)
pause
