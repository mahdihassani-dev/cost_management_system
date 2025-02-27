import os
import django
import pandas as pd
from datetime import datetime

# تنظیمات Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_cost_management.settings')
django.setup()

from cost_manager.models import PurchaseItem  # مدل مربوطه را ایمپورت کنید

def import_from_excel(file_path):
    # خواندن فایل اکسل
    df = pd.read_excel(file_path)

    # حلقه برای وارد کردن داده‌ها
    for index, row in df.iterrows():
        PurchaseItem.objects.create(
            name=row['وسیله'],
            quantity=row['تعداد'],
            price=row['هزینه واحد(تومان)'],
            status=row['وضعیت خرید'],
            purchase_date=datetime.today(),  # تاریخ امروز
            purchase_link=None  # لینک خرید نال
        )
    print("داده‌ها با موفقیت وارد شدند!")

if __name__ == "__main__":
    file_path = "costs_excel.xlsx"  # مسیر فایل اکسل
    import_from_excel(file_path)