🎓 Tələbə İdarəetmə Sistemi

Python ilə yazılmış sadə, konsol əsaslı tələbə qeydiyyat proqramı. Tələbələri əlavə et, yenilə, sil və axtar. Bütün məlumat students.json faylında saxlanılır, yəni proqramı bağlasan da heç nə itmir. 💾

Bu layihə Python öyrənərkən fayllarla işləməyi, try/except istifadəsini və modulları bir-birinə bağlamağı məşq etmək üçün hazırlanıb.

✨ Nələr edə bilir?
Funksiya	Nə edir?
➕ addStudent()	Yeni tələbə əlavə edir (ad, soyad, yaş, qiymətlər)
📋 ShowAllStudent()	Bütün tələbələri göstərmək üçün nəzərdə tutulub
✏️ updateStudent()	ID-yə görə tələbənin məlumatlarını dəyişir
🗑️ removeStudent()	ID-yə görə tələbəni silir
🔍 searchStudent()	Ada görə tələbə axtarır
📁 Layihənin strukturu
📦 student-project
 ┣ 📜 student.py       → əsas proqram (funksiyalar burdadır)
 ┣ 📜 database.py      → fayldan oxuma və fayla yazma
 ┗ 📜 students.json    → məlumatlar (proqram özü yaradır)
student.py istifadəçi ilə işləyir: sual verir, yoxlayır, nəticəni göstərir.
database.py yalnız məlumat saxlama ilə məşğuldur: loadStudents() oxuyur, saveStudens() yazır.

Belə bölmək proqramı daha səliqəli və başa düşülən edir. Hər faylın öz işi var. 🧩

🚀 Necə işə salmaq olar?
Python 3 quraşdırıldığından əmin ol:
python --version
Hər iki faylı eyni qovluğa qoy.
Terminalda həmin qovluğa keç və işə sal:
python student.py

Əlavə kitabxana quraşdırmaq lazım deyil, yalnız Python-un öz json modulu istifadə olunur. 🎉

🧪 Nümunə
enter name: Aysel
enter surname: Məmmədova
enter age: 19
enter grades (məs: 80,90,75): 90,85,100
Data saved succesfuly
Student added successfully!
🗂️ Məlumat necə saxlanılır?

Hər tələbə students.json faylında belə görünür:

json
[
    {
        "id": 1,
        "name": "Aysel",
        "surname": "Məmmədova",
        "age": 19,
        "grades": [90, 85, 100]
    }
]

Hər yeni tələbənin id-si avtomatik olaraq ən böyük mövcud id-dən 1 çox olur.

🛡️ Yoxlamalar

Proqram addStudent() zamanı bunları yoxlayır:

✅ Ad və soyad boş ola bilməz
✅ Yaş 18-dən az ola bilməz
✅ Qiymətlər 0 ilə 100 arasında olmalıdır
✅ Yaş və qiymətlərə hərf yazılsa, proqram çökmür, xəbərdarlıq verir (try/except sayəsində)
📌 Hazırkı vəziyyət
if __name__ == "__main__": blokunda hələlik yalnız addStudent() və ShowAllStudent() çağırılır.
ShowAllStudent() məlumatları yükləyir, amma ekrana çıxarmır, bu hissə hələ tamamlanmayıb.
updateStudent(), removeStudent() və searchStudent() yazılıb, amma menyu olmadığı üçün onları birbaşa çağırmaq lazımdır.
🔮 Gələcək planlar (To-Do)
[ ] ShowAllStudent() funksiyasını tamamlamaq
[ ] Əməliyyatları seçmək üçün menyu əlavə etmək (1. Əlavə et, 2. Göstər, 3. Yenilə ...)
[ ] Yeniləmə zamanı yaş və qiymət yoxlamaları
[ ] Tələbənin orta qiymətini hesablamaq
[ ] Soyada görə də axtarış
[ ] Silmədən əvvəl təsdiq sualı
🛠️ İstifadə olunan texnologiyalar
🐍 Python 3
📄 JSON (məlumat saxlama)
⚠️ try / except (xəta idarəetməsi)
👨‍💻 Müəllif

Bu layihə öyrənmə məqsədilə hazırlanıb. Təkliflər və düzəlişlər üçün açıqdır! 🙌

Kod yaz, səhv et, düzəlt, təkrarla. Proqramlaşdırma belə öyrənilir. 💪
