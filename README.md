# Pop-Up Translator
A simple Program to translate the words in clipboard and shows it in a pop-up window.

**Possibility to use the primary clipboard added (you don't need copy the text in your clipboard, anymore. you should just select the text by your mouse!)**
**Possibility show translated text in notification added**

to use, first you should install some libraries:

`sudo pip3 install python-bidi googletrans arabic-reshaper clipboard argparse`

also you should install some packages from your Distribution's repository. (`tk`, `xsel`)

Fedora:

`sudo dnf install tk xsel`

Arch Linux:

`sudo pacman -S tk xsel`

Debian and Ubuntu:

`sudo apt install tk xsel`

## how to use
you should run the `run.py` file with two flags and their arguments. we have two flags:

`-m`, `--mode`: set how to display. (we have 2 display modes, notify and popup)

`-c`, `clipboard`: set the type of clipboard (we have 2, primary and secondary)

This Program Translates English to Persian and It'll Translate all other languages to English and shows it in a Pop-Up Window or shows the result to notification as well, if you select popup mode the window will destroy Itself after 5 seconds.

You can make a keyboard shortcut for Run the Program and anytime you want to translate anything just do it by keyboard shortcuts easily.
**screenshots:**

![ENG to FA](/images/screenshot1.png)

![FA to ENG](/images/screenshot2.png)

![Gif Shot](/images/screenshot3.gif)


<h1 dir="rtl">
مترجم پاپ آپ
</h1>
<p dir="rtl">
یک برنامه‌ی ساده برای ترجمه‌ی کلمات درون کلیپ‌بورد، و نمایش آن به صورت یک پنجره‌ی پاپ‌آپ
</p>
<p>
<b>
امکان استفاده از کلیپ‌بورد اولیه اضافه شد. (دیگر نیاز نیست متن را در کلیپ‌بورد خود کپی کنید، فقط کافیست آن‌ها را با موس انتخاب کنید!)
</b>
</p>

<p>
<b>
امکان نمایش متن ترجمه شده در اعلان‌ها اضافه شد.
</b>
</p>

<p dir="rtl">
جهت اجرای درست و استفاده از برنامه، ابتدا نیاز دارید چند کتابخانه را نصب کنید که در زیر نام آن‌ها به همراه دستور نصب وجود دارد:
</p>
<code>
sudo pip3 install python-bidi googletrans arabic-reshaper clipboard argparse
</code>
<p dir="rtl">

همچنین نیاز است بسته‌های tk و xsel را از مخازن توزیع خود نصب کنید.
</p>
<p dir="rtl">
فدورا:
</p>
<code>
sudo dnf install tk xsel
</code>
<p dir="rtl">
آرچ لینوکس:
</p>
<code>
sudo pacman -S tk xsel
</code>
<p dir="rtl">
دبیان و اوبونتو:
</p>
<code>
sudo apt install tk xsel
</code>
<p dir="rtl">
  پس از نصب پیش‌نیازها کافیست این مخزن را clone یا دانلود کنید و سپس فایل <code>run.py</code> را با دو پرچم و آرگومان مورد نظر  اجرا کنید. در این برنامه دو آرگومان داریم:
</p>

<p dir="rtl">
-m , --mode : این آرگومان حالت نمایش ترجمه را مشخص می‌‌کند (دو حالت notify جهت نمایش در نوتیفیکیشن و popup جهت نمایش در پنجره‌ی پاپ‌آپ، موجود است.
</p>
<p dir="rtl">
-c , --clipboard : این آرگومان کلیپ بورد مورد نظر شما را مشخص می‌کند (دو حالت primary برای کلیپ بورد ابتدایی (متن‌هایی که با موس انتخاب می‌کنید) و secondary جهت متن‌های کپی شده در کلیپ‌بورد شما موجود است.
</p>

<p dir="rtl">
همچنین می‌توانید هر زمان با استفاده از پرچم -h‌ راهنمای برنامه را مشاهده کنید.
</p>

<p dir="rtl">
در صورتی که محتویات کلیپ‌بورد شما به زبان انگلیسی باشد، ترجمه‌ی آن به زبان فارسی را مشاهده خواهید کرد و در صورتی که محتویات کلیپ‌بورد هر زبانی به جز انگلیسی باشد ترجمه‌ی آن به زبان انگلیسی تحویل خواهید گرفت. چناچه حالت نمایش را پاپ‌آپ انتخاب کنید، پنجره‌ی باز شده پس از مدت 5 ثانیه بسته خواهد شد.
</p>
<p dir="rtl">
کافیست در تنظیمات میزکار خود یک میانبر کیبرد برای اجرای برنامه با پرچم‌ها و آرگومان‌های مورد نظر بسازید و هر زمان نیاز داشتید متنی را ترجمه کنید آن را به سادگی با میانبرهای کیبرد انجام دهید.
</p>

<h3 dir="rtl">
اسکرین شات‌ها 
</h3>
<div style="text-align:center">
  <img src ="/images/screenshot1.png" />
</div>
<div style="text-align:center">
  <img src ="/images/screenshot2.png" />
</div>
<div style="text-align:center">
  <img src ="/images/screenshot3.gif" />
</div>
