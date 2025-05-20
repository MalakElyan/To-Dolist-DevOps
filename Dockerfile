# استخدم صورة بايثون الرسمية
FROM python:3.10-slim

# تعيين مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ الملفات إلى الحاوية
COPY . .

# تثبيت المتطلبات
RUN pip install --no-cache-dir -r requirements.txt

# تعيين البورت
EXPOSE 5000

# أمر تشغيل التطبيق
CMD ["python", "run.py"]
