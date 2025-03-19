# 🌐 **پروژه فیلم و سریال `ApplayMovie` با جنگو**

![home page image](screenshot.png "home page")

## 📋 توضیحات
این پروژه یک وب‌سایت دانلود فیلم و سریال رایگان است که با استفاده از فریم‌ورک Django توسعه یافته است. هدف این پروژه ارائه یک پلتفرم کاربرپسند برای دسترسی به مجموعه‌ای از فیلم‌ها و سریال‌ها به صورت رایگان و آسان است.

## 🚀 ویژگی ها

`صفحات اولیه`
- <b>صفحه اصلی: </b>نمایش 6تا فیلم و سریال  به صورت رندوم و نمایش فیلم های پیشنهادی
- <b>صفحه تماس با ما: </b>امکان ثبت پیام برای مدیر

`صفحات مربوط به فیلم ها`
- <b>صفحه لیست فیلم ها: </b>نمایش تمام فیلم ها با صفحه بندی اصولی
- <b>صفحه جزئیات فیلم ها: </b>نمایش جزئیات فیلم ها و نمایش فیلم های مشابه و امکان ثبت دیدگاه و حذف آن
- <b>صفحه ژانر فیلم ها: </b>نمایش فیلم های مربوط به ژانر انتخاب شده با صفحه بندی اصولی

`صفحات مربوط به سریال ها`
- <b>صفحه لیست سریال ها: </b>نمایش تمام سریال ها با صفحه بندی اصولی
- <b>صفحه جزئیات سریال ها: </b>نمایش جزئیات سریال ها و نمایش سریال های مشابه و امکان ثبت دیدگاه و حذف آن
- <b>صفحه ژانر سریال ها: </b>نمایش سریال های مربوط به ژانر انتخاب شده با صفحه بندی اصولی

`صفحات مربوط به بازیگران`
- <b>صفحه لیست بازیگران: </b>نمایش تمام بازیگران با صفحه بندی اصولی
- <b>صفحه جزئیات بازیگران: </b>نمایش جزئیات بازیگران 

`صفحات مربوط به مقالات`
- <b>صفحه لیست مقالات: </b>نمایش لیست مقالات با صفحه بندی اصولی
- <b>صفحه جزئیات مقالات: </b>نمایش جزئیات مقالات و ثبت دیدگاه و حذف آن
- <b>صفحه دسته بندی مقالات: </b>نمایش مقالات مربوط به دسته بندی انتخاب شده با صفحه بندی اصولی

`دیگر امکانات`
- <b>سیستم ورود و ثبت نام: </b>امکان ورود و ثبت نام کاربران
- <b>جستجو فیلم ها و سریال ها: </b>قابلیت جستجوی فیلم ها و سریال ها براساس عنوان
- <b>عضویت در خبرنامه: </b>امکان عضویت کاربران در خبرنامه

## 🛠️ نصب و راه اندازی
برای نصب و راه‌اندازی این پروژه، مراحل زیر را دنبال کنید:

1. **کلون کردن مخزن:**

```bash
git clone https://github.com/arvinmaroufi/ApplayMovie
cd repo
```

2. **ایجاد محیط مجازی (اختیاری):**

```bash
python -m venv venv
source venv/bin/activate  # برای سیستم‌های Unix/Mac
venv\Scripts\activate  # برای ویندوز
```

3. **نصب وابستگی‌ها:**
   
```bash
pip install -r requirements.txt
```

4. **اجرای migrations:**

```bash
python manage.py migrate
```

5. **اجرای سرور:**

```bash
python manage.py runserver
```

6. **دسترسی به وب‌سایت:**
   در مرورگر خود به آدرس http://127.0.0.1:8000/ بروید.

## ✅ استفاده

پس از راه‌اندازی، می‌توانید پروژه رو مشاهده کنید و لذت ببرید.

## 🎯 مشارکت

اگر تمایل به مشارکت در این پروژه دارید، لطفاً مراحل زیر را دنبال کنید:

1. یک فورک از مخزن ایجاد کنید.
2. تغییرات خود را اعمال کنید.
3. یک Pull Request ارسال کنید.

## 🧾 مجوز

این پروژه تحت مجوز MIT منتشر شده است.

## 💻 برنامه نویس

**آروین معروفی** - [لینک پروفایل گیت‌هاب](https://github.com/arvinmaroufi)

## 💬 ارتباط با ما

اگر سوالی دارید یا نیاز به کمک بیشتری دارید، لطفاً با ما تماس بگیرید:

- **ایمیل**: [arvinmaroufi.dev@gmail.com](mailto:arvinmaroufi.dev@gmail.com)
- **گیت‌هاب**: [arvinmaroufi](https://github.com/arvinmaroufi/arvinmaroufi/issues)
- **اینستاگرام**: [arvinmaroufi.ir](https://instagram.com/arvinmaroufi.ir)
- **تلگرام**: [arvin_maroufi](https://t.me/arvin_maroufi)

ما خوشحال می‌شویم که از شما بشنویم 🙏

## ❤️ حمایت از ما

اگر از کار ما لذت می‌برید و می‌خواهید از ما حمایت کنید، لطفاً ما را در شبکه‌های اجتماعی دنبال کنید:

- **گیت‌هاب**: [arvinmaroufi](https://github.com/arvinmaroufi)
- **اینستاگرام**: [arvinmaroufi.ir](https://instagram.com/arvinmaroufi.ir)
- **تلگرام**: [arvinmaroufi_ir](https://t.me/arvinmaroufi_ir)

از حمایت شما سپاسگزاریم 🙏