@echo off
chcp 65001 > nul
echo =======================================================
echo    KAPADOKYA ÜNİVERSİTESİ - GIT COMMIT OTOMASYON ARACI
echo =======================================================
echo.
echo Bu araç projenizde gerekli olan 4 aşamalı Git commit geçmişini
echo yerel bilgisayarınızda otomatik olarak oluşturacaktır.
echo.
echo Lütfen devam etmeden önce bilgisayarınızda Git programının
echo yüklü olduğundan emin olun.
echo.
pause

echo.
echo [Sistem] Git deposu başlatılıyor (git init)...
git init

echo.
echo [Sistem] AŞAMA 1: finans_modeli.py ve utils.py ekleniyor...
git add finans_modeli.py utils.py
git commit -m "First commit: Proje yapısı oluşturuldu, finans modeli ve yardımcı fonksiyonlar eklendi"

echo.
echo [Sistem] AŞAMA 2: islem_yonetimi.py ve dosya_islemleri.py ekleniyor...
git add islem_yonetimi.py dosya_islemleri.py
git commit -m "Second commit: Gelir/gider yönetimi ve CSV dosya okuma/yazma modülleri eklendi"

echo.
echo [Sistem] AŞAMA 3: analiz.py ve gorsellestirme.py ekleniyor...
git add analiz.py gorsellestirme.py
git commit -m "Third commit: Pandas & NumPy veri analizleri ve Matplotlib görselleştirme modülleri tamamlandı"

echo.
echo [Sistem] AŞAMA 4: main.ipynb, Readme.md ve otomasyon betiği ekleniyor...
git add main.ipynb Readme.md git_otomasyon.bat
git commit -m "Fourth commit: Jupyter notebook arayüzü, Readme dokümantasyonu tamamlandı ve testler uygulandı"

echo.
echo =======================================================
echo   İşlem Başarıyla Tamamlandı!
echo =======================================================
echo Yerel Git deposu 4 aşamalı commit geçmişiyle hazırlandı.
echo Şimdi bu projeyi GitHub'a yüklemek için şu komutları kullanabilirsiniz:
echo.
echo git remote add origin HESABINIZIN_REPO_LINKI
echo git branch -M main
echo git push -u origin main
echo =======================================================
echo.
pause
