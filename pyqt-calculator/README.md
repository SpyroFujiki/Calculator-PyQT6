# Máy tính Python + PyQt6

Ứng dụng desktop lấy cảm hứng từ ảnh mẫu: nền đen, nút tròn xám và dấu bằng cam. Không cần Qt Designer.

## 1. Chuẩn bị trên Windows

Cài Python 3.10 trở lên từ https://www.python.org/downloads/ và Git từ https://git-scm.com/downloads . Nếu trình cài Python có tùy chọn Add Python to PATH, hãy chọn nó. Mở terminal mới rồi kiểm tra:

```powershell
py --version
git --version
```

Giải nén bộ mã nguồn, mở thư mục `pyqt-calculator` bằng VS Code, chọn Terminal > New Terminal. Tất cả lệnh dưới đây chạy trong thư mục chứa `main.py`.

## 2. Tạo môi trường ảo và cài thư viện

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Dùng trực tiếp Python của môi trường ảo nên không cần kích hoạt hay sửa Execution Policy của PowerShell. Chỉ có một thư viện bên ngoài là PyQt6; pip cài cả các phụ thuộc Qt cần thiết.

## 3. Chạy ứng dụng

```powershell
.\.venv\Scripts\python.exe main.py
```

Trong VS Code: Ctrl+Shift+P > Python: Select Interpreter > chọn `.venv` nếu muốn chạy bằng nút Run Python File.

Trên macOS/Linux có giao diện desktop:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python main.py
```

## 4. Sử dụng

- Bấm chuột hoặc nhập số, dấu chấm, +, -, *, / trên bàn phím.
- Enter: tính kết quả. Backspace: xóa ký tự đang nhập. Escape/Delete: xóa toàn bộ.
- AC: đặt lại. 00: nhập hai số 0. %: chia số hiện tại cho 100 (50% = 0.5).
- Tính từ trái sang phải: 2 + 3 × 4 = 20. Chưa có ưu tiên nhân chia, ngoặc hoặc chế độ khoa học.
- Dấu trừ tạo kết quả âm; nhập số âm bằng 0 − số đó. Chưa có nút đổi dấu.
- Dấu bằng không lặp phép tính trước đó. Nhập số sau dấu bằng sẽ bắt đầu số mới.
- Dùng Decimal, độ chính xác 28 chữ số; phép chia vô hạn được làm tròn. Số dài có thể cuộn ngang trong màn hình.

## 5. Cấu trúc và giải thích

```text
pyqt-calculator/
    main.py             Giao diện PyQt6 và sự kiện
    calculator.py       Lớp Calculator xử lý phép tính
    test_calculator.py  Kiểm tra logic
    requirements.txt    Thư viện cần cài
    .gitignore          Bỏ qua môi trường ảo và file phát sinh
    README.md           Hướng dẫn này
```

`CalculatorWindow` kế thừa `QWidget`, là cửa sổ chính. `QVBoxLayout` xếp màn hình và bàn phím theo chiều dọc; `QGridLayout` xếp 20 nút thành 5 hàng, 4 cột. `QPushButton.clicked` gọi `press()` với nhãn nút. `Calculator` lưu số hiện tại, tổng và toán tử chờ, rồi trả kết quả để giao diện cập nhật. Không sử dụng eval(). Khối `if __name__ == '__main__'` tạo QApplication, hiển thị cửa sổ và chạy vòng lặp sự kiện.

Chạy kiểm tra:

```powershell
.\.venv\Scripts\python.exe -m unittest -v
```

## 6. Tạo repository Git tại máy

Trong terminal ở thư mục dự án:

```powershell
git init
git add .
git commit -m "Initial commit: PyQt6 calculator"
git branch -M main
```

Nếu Git báo chưa có thông tin tác giả, đặt tên/email cho repository này rồi chạy lại commit (thay thông tin ví dụ bằng của bạn):

```powershell
git config user.name "Ten cua ban"
git config user.email "email-cua-ban@example.com"
git commit -m "Initial commit: PyQt6 calculator"
```

## 7. Đưa repository lên GitHub

Đăng nhập https://github.com và tạo repository mới tên `pyqt-calculator`. Chọn Public hoặc Private theo nhu cầu. Để repository trống: không thêm README, .gitignore hoặc license trên GitHub vì mã nguồn đã có ở máy.

Thay YOUR_USERNAME bằng tên tài khoản thật:

```powershell
git remote add origin https://github.com/YOUR_USERNAME/pyqt-calculator.git
git push -u origin main
```

Đăng nhập qua trình duyệt khi Git yêu cầu. Nếu đã có remote origin, kiểm tra bằng `git remote -v` trước khi thêm. Bộ ZIP chưa liên kết hay tạo repository trong tài khoản GitHub của bạn.

Các lần cập nhật sau:

```powershell
git add .
git commit -m "Update calculator"
git push
```

## 8. Tùy chọn: đóng gói thành EXE

Chạy các lệnh sau trên Windows:

```powershell
.\.venv\Scripts\python.exe -m pip install pyinstaller
.\.venv\Scripts\python.exe -m PyInstaller --onefile --windowed --name Calculator main.py
```

File tạo ra ở `dist/Calculator.exe`. Bước này là tùy chọn, chưa đóng gói sẵn trong bộ nguồn.

## Nguồn thư viện

Hướng dẫn cài PyQt6 chính thức: https://www.riverbankcomputing.com/software/pyqt/download
