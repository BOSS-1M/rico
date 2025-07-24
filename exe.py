
# ملف تشغيل للوحدة المشفرة exe.cpython-312.so
import exe

# تأكد أن الدالة الرئيسية موجودة داخل الملف الأصلي
if hasattr(exe, 'main'):
    exe.main()
else:
    print("تم استيراد exe بنجاح، ولكن لا توجد دالة main للتشغيل.")
