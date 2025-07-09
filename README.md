# 🚀 Bitcoin Mining Pool - Hệ Thống Đào BTC Ảo

## 📋 Mô tả dự án

Đây là một ứng dụng web mô phỏng việc đào Bitcoin với mục đích thu hút người dùng đăng ký tài khoản Binance. Ứng dụng có giao diện đẹp với hiệu ứng ma trận và hiển thị số liệu đào BTC theo thời gian thực.

## ✨ Tính năng chính

- 🎯 **Giao diện đào BTC ảo** với hiệu ứng ma trận
- 📊 **Thống kê thời gian thực**: BTC đã đào, Hash Rate, số thợ đào online
- 👥 **Hệ thống đăng ký** thu thập thông tin người dùng
- 📋 **Danh sách người dùng** đã đăng ký
- 🎨 **Giao diện responsive** tương thích mobile
- 🔗 **Liên kết trực tiếp** đến trang đăng ký Binance

## 🛠️ Cài đặt và chạy

### Bước 1: Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### Bước 2: Chạy ứng dụng
```bash
python app.py
```

### Bước 3: Truy cập ứng dụng
Mở trình duyệt và truy cập: `http://localhost:5000`

## 📁 Cấu trúc dự án

```
BTC/
├── app.py                 # File chính Flask app
├── requirements.txt       # Dependencies
├── README.md            # Hướng dẫn sử dụng
├── templates/           # Thư mục chứa HTML templates
│   ├── index.html      # Trang chủ với giao diện đào BTC
│   ├── register.html   # Trang đăng ký
│   └── success.html    # Trang thành công
└── btc_mining.db       # Database SQLite (tự động tạo)
```

## 🎨 Giao diện

### Trang chủ (`/`)
- Hiển thị thống kê đào BTC theo thời gian thực
- Hiệu ứng ma trận chạy nền
- Nút đăng ký nổi bật
- Danh sách người dùng đã đăng ký

### Trang đăng ký (`/register`)
- Form thu thập thông tin: Họ tên, Email, ID Binance
- Giao diện đẹp với theme xanh lá
- Validation form cơ bản

### Trang thành công (`/success`)
- Thông báo đăng ký thành công
- Hướng dẫn các bước tiếp theo
- Liên kết tạo tài khoản Binance

## 🔧 API Endpoints

- `GET /` - Trang chủ
- `GET /register` - Trang đăng ký
- `POST /register` - Xử lý đăng ký
- `GET /success` - Trang thành công
- `GET /api/mining-stats` - API thống kê đào BTC
- `GET /api/users` - API danh sách người dùng

## 💾 Database

Ứng dụng sử dụng SQLite với 2 bảng chính:

### Bảng `User`
- `id`: ID người dùng
- `name`: Họ tên
- `email`: Email
- `binance_id`: ID Binance (tùy chọn)
- `registered_at`: Thời gian đăng ký
- `is_active`: Trạng thái hoạt động

### Bảng `MiningStats`
- `id`: ID thống kê
- `btc_mined`: Số BTC đã đào
- `hash_rate`: Hash rate
- `miners_online`: Số thợ đào online
- `last_updated`: Thời gian cập nhật cuối

## 🎯 Mục đích sử dụng

Dự án này được thiết kế để:
1. **Thu hút người dùng** với giao diện đào BTC ảo hấp dẫn
2. **Thu thập thông tin** người dùng quan tâm
3. **Kêu gọi đăng ký** tài khoản Binance
4. **Tạo danh sách** người dùng tiềm năng

## 🔒 Lưu ý bảo mật

- Đây là dự án demo, không có tính năng bảo mật cao
- Thông tin người dùng được lưu trữ local
- Không có mã hóa dữ liệu
- Chỉ sử dụng cho mục đích demo/giáo dục

## 🚀 Phát triển tiếp

Có thể mở rộng thêm:
- Hệ thống xác thực email
- Dashboard admin
- Thống kê chi tiết
- Tích hợp API Binance thực
- Hệ thống thưởng thực tế

## 📞 Liên hệ

Nếu có câu hỏi hoặc góp ý, vui lòng liên hệ qua email hoặc tạo issue trên repository. 