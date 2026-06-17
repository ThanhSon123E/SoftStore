import os
import shutil

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'pc-direct-downloader-secret-key-2026')
    
    # Phát hiện xem ứng dụng có đang được chạy trên Vercel hay không
    IS_VERCEL = 'VERCEL' in os.environ or os.environ.get('VERCEL') == '1'
    
    if IS_VERCEL:
        # Trong môi trường Vercel (read-only filesystem), copy database gốc sang thư mục /tmp có quyền ghi đọc
        src_db = os.path.join(os.path.dirname(__file__), 'software.db')
        dest_db = '/tmp/software.db'
        
        # Chỉ copy một lần duy nhất khi khởi động serverless container
        if os.path.exists(src_db) and not os.path.exists(dest_db):
            try:
                # Đảm bảo thư mục đích tồn tại (dù /tmp là hệ thống)
                os.makedirs(os.path.dirname(dest_db), exist_ok=True)
                shutil.copy2(src_db, dest_db)
            except Exception as e:
                print(f"Lỗi sao chép cơ sở dữ liệu sang /tmp trên Vercel: {e}")
                
        SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/software.db'
    else:
        # Chạy cục bộ
        SQLALCHEMY_DATABASE_URI = 'sqlite:///software.db'
        
    SQLALCHEMY_TRACK_MODIFICATIONS = False
