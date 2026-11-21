# 📐 Dự Án: Sử Dụng SymPy Để Giải Hệ Bất Phương Trình Bậc Nhất Hai Ẩn

> **Đơn vị:** Khoa Toán học – Trường Đại học Sư phạm - Đại học Huế  
> **Thực hiện:** Nhóm 9 *(Lê Thị Linh Châu, Nguyễn Thị Xuân Thi, Trần Nguyễn Uyên Thi, Trương Ngụy Minh Triết)*  
> **Thời gian:** Tháng 10/2026

---

## 📖 1. Giới thiệu dự án

Dự án khám phá và ứng dụng sức mạnh của thư viện toán học ký hiệu **SymPy** trong ngôn ngữ lập trình **Python** để giải quyết lớp bài toán **Hệ bất phương trình bậc nhất hai ẩn** và **Quy hoạch tuyến tính** trong chương trình Toán phổ thông (Toán 10).

Thông qua việc chuyển hóa mô hình toán học sang mã nguồn Python, dự án giúp:
* Tự động thiết lập và giải chính xác tuyệt đối hệ phương trình đường biên (loại bỏ sai số làm tròn).
* Tìm tọa độ các đỉnh của đa giác miền nghiệm và xác định phương án tối ưu (lợi nhuận lớn nhất / chi phí nhỏ nhất).
* Trực quan hóa sinh động miền nghiệm bằng đồ thị trực tiếp trên mặt phẳng tọa độ Oxy.

---

## 🛠️ 2. Các câu lệnh SymPy cốt lõi sử dụng

| Câu lệnh / Hàm | Chức năng trong dự án |
| :--- | :--- |
| `sp.symbols('x y')` | Khai báo các ẩn số x, y dưới dạng biến ký hiệu đại số (symbolic variables). |
| `sp.And(đk_1, đk_2, ...)` | Kết hợp nhiều bất phương trình thành một hệ điều kiện đồng thời (phép giao miền nghiệm). |
| `sp.solve([pt_1, pt_2], (x, y))` | Giải hệ phương trình đường thẳng biên để tìm tọa độ các đỉnh của đa giác miền nghiệm. |
| `expr.subs({x: x0, y: y0})` | Thay tọa độ các đỉnh vào hàm mục tiêu $F(x, y)$ để tính giá trị tối ưu. |
| `sp.plot_implicit(hệ, (x, min, max), (y, min, max))` | Quét tọa độ và tự động tô màu trực quan hóa miền nghiệm trên mặt phẳng Oxy. |

---

## 📂 3. Cấu trúc & Danh sách bài toán triển khai

Toàn bộ mã nguồn thực hành được lưu trong file `code.py`, bao gồm 6 bài toán tiêu biểu:

1. **Biểu diễn miền nghiệm hệ bất phương trình (Bài tập 2.5 - SGK Toán 10 Tập 1):**
   * Vẽ trực quan miền nghiệm cho 3 hệ bất phương trình bậc nhất hai ẩn (a, b, c).
2. **Bài toán 1 – Tối ưu lợi nhuận kinh doanh điều hòa:**
   * **Mục tiêu:** Tối đa hóa lợi nhuận F(x, y) = 3,5x + 2y với vốn tối đa 1,2 tỷ đồng và tổng nhu cầu là 100 máy.
   * **Kết quả:** Đầu tư 20 máy điều hòa hai chiều và 80 máy điều hòa một chiều. Lợi nhuận lớn nhất đạt **230 triệu đồng**.
3. **Bài toán 2 – Tối ưu chi phí khẩu phần dinh dưỡng:**
   * **Mục tiêu:** Tối thiểu hóa chi phí mua thịt bò và thịt lợn F(x, y) = 250x + 160y đảm bảo đủ Protein và Lipid.
   * **Kết quả:** Mua 0,3 kg thịt bò và 1,1 kg thịt lợn. Chi phí thấp nhất là **251 nghìn đồng**.
4. **Bài toán 3 – Tối ưu phân bổ vốn đầu tư trái phiếu:**
   * **Mục tiêu:** Tối đa hóa tiền lãi sau 1 năm từ 3 loại trái phiếu (Chính phủ, Ngân hàng, Doanh nghiệp) với tổng vốn 1200 triệu đồng.
   * **Kết quả:** Đầu tư 750 triệu (TP Chính phủ), 250 triệu (TP Ngân hàng), 200 triệu (TP Doanh nghiệp). Lợi nhuận lớn nhất **96,5 triệu đồng**.
5. **Bài toán 4 – Tối ưu hiệu quả chiến dịch quảng cáo:**
   * **Mục tiêu:** Tối đa hóa điểm hiệu quả F(x, y) = x + 8y trên đài phát thanh và truyền hình với ngân sách tối đa 160 triệu đồng.
   * **Kết quả:** Đặt 200 giây trên đài phát thanh và 360 giây trên đài truyền hình. Điểm hiệu quả tối đa **3080**.
6. **Bài toán 5 – Tối ưu kế hoạch sản xuất trên 3 nhóm máy:**
   * **Mục tiêu:** Tối đa hóa lợi nhuận F(x, y) = 30x + 50y khi phân bổ máy thuộc các nhóm A, B, C để sản xuất hai loại sản phẩm I và II.
   * **Kết quả:** Sản xuất 4 sản phẩm loại I và 1 sản phẩm loại II (x - y = 3). Lợi nhuận lớn nhất **170 nghìn đồng**.

---

## 🚀 4. Hướng dẫn cài đặt và chạy chương trình

1. **Yêu cầu môi trường:** Python 3.x
2. **Cài đặt các thư viện cần thiết** (`sympy` để tính toán đại số và `matplotlib` để hiển thị đồ thị):
   ```bash
   pip install sympy matplotlib
   ```
3. **Chạy mã nguồn:**
   ```bash
   python code.py
   ```

---

## 📚 5. Tài liệu tham khảo

* Bộ Giáo dục và Đào tạo (2022). *Sách giáo khoa Toán 10, Tập 1 (Bộ sách Kết nối tri thức với cuộc sống)*. Nhà xuất bản Giáo dục Việt Nam.
* SymPy Development Team. *SymPy Documentation* ([docs.sympy.org](https://docs.sympy.org/)).
