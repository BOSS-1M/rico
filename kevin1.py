
# ملف تشغيل للوحدة المشفرة kevin1.cpython-312.so
import kevin1

# تأكد أن الدالة الرئيسية موجودة داخل الملف الأصلي
if hasattr(kevin1, 'main'):
    kevin1.main()
else:
    print("تم استيراد kevin1 بنجاح، ولكن لا توجد دالة main للتشغيل.")
