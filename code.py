import sympy as sp

# 1. Khai báo 2 ẩn x và y
x, y = sp.symbols('x y')

# 2. BIỂU DIỄN MIỀN NGHIỆM CHO HỆ a)
# y - x < -1; x > 0; y < 0
he_a = sp.And(y - x < -1, x > 0, y < 0)
do_thi_a = sp.plot_implicit(
    he_a, (x, -2, 6), (y, -6, 2),
    title="Mien nghiem he a", show=False
)

# 3. BIỂU DIỄN MIỀN NGHIỆM CHO HỆ b)
# x >= 0; y >= 0; 2x + y <= 4
he_b = sp.And(x >= 0, y >= 0, 2*x + y <= 4)
do_thi_b = sp.plot_implicit(
    he_b, (x, -2, 5), (y, -2, 6),
    title="Mien nghiem he b", show=False
)

# 4. BIỂU DIỄN MIỀN NGHIỆM CHO HỆ c)
# x >= 0; x + y > 5; x - y < 0
he_c = sp.And(x >= 0, x + y > 5, x - y < 0)
do_thi_c = sp.plot_implicit(
    he_c, (x, -2, 8), (y, -2, 10),
    title="Mien nghiem he c", show=False
)

# 5. HIỂN THỊ CÁC ĐỒ THỊ RA MÀN HÌNH
do_thi_a.show()
do_thi_b.show()
do_thi_c.show()
# ==========================================
# BÀI TIẾP THEO: TỐI ƯU LỢI NHUẬN ĐIỀU HÒA
# ==========================================
x, y = sp.symbols('x y')
he_dieu_kien = sp.And(20*x + 10*y <= 1200, x + y <= 100, x >= 0, y >= 0)

# 1. TÍNH TOÁN VÀ IN KẾT QUẢ RA TRƯỚC
diem_toi_uu = sp.solve([20*x + 10*y - 1200, x + y - 100], (x, y))
loi_nhuan = 3.5*x + 2*y
max_loi_nhuan = loi_nhuan.subs({x: diem_toi_uu[x], y: diem_toi_uu[y]})

print(f"Để đạt lợi nhuận lớn nhất, cửa hàng cần đầu tư:")
print(f"- {diem_toi_uu[x]} máy điều hòa hai chiều")
print(f"- {diem_toi_uu[y]} máy điều hòa một chiều")
print(f"Tổng lợi nhuận lớn nhất sẽ là: {max_loi_nhuan} triệu đồng.")

# 2. ĐỒ THỊ
sp.plot_implicit(he_dieu_kien, (x, -10, 110), (y, -10, 130), title="Mien nghiem bai toan")
# ==========================================
# BÀI TIẾP THEO: TỐI ƯU CHI PHÍ DINH DƯỠNG
# ==========================================
x, y = sp.symbols('x y')

# Hàm mục tiêu: Chi phí mua thịt (nghìn đồng)
chi_phi = 250*x + 160*y

# Hệ điều kiện dinh dưỡng và khối lượng mua
he_dieu_kien = sp.And(
    800*x + 600*y >= 900,  # Protein tối thiểu
    200*x + 400*y >= 400,  # Lipid tối thiểu
    x >= 0, x <= 1.6,      # Giới hạn thịt bò
    y >= 0, y <= 1.1       # Giới hạn thịt lợn
)

# Tìm tọa độ các đỉnh của miền nghiệm (giao điểm các đường biên)
d1 = 800*x + 600*y - 900
d2 = 200*x + 400*y - 400
d3 = x - 1.6
d4 = y - 1.1

A = sp.solve([d1, d2], (x, y))  # Giao điểm của 2 đường dinh dưỡng
B = sp.solve([d2, d3], (x, y))  # Giao điểm lipid và giới hạn bò
C = sp.solve([d3, d4], (x, y))  # Giao điểm giới hạn bò và lợn
D = sp.solve([d1, d4], (x, y))  # Giao điểm protein và giới hạn lợn

# Tính và in chi phí tại các đỉnh để tìm giá trị nhỏ nhất
print("CHI PHÍ TẠI CÁC ĐỈNH CỦA MIỀN NGHIỆM:")
print(f"- Mua {A[x]}kg bò, {A[y]}kg lợn => Chi phí: {chi_phi.subs({x: A[x], y: A[y]})} nghìn đồng")
print(f"- Mua {B[x]}kg bò, {B[y]}kg lợn => Chi phí: {chi_phi.subs({x: B[x], y: B[y]})} nghìn đồng")
print(f"- Mua {C[x]}kg bò, {C[y]}kg lợn => Chi phí: {chi_phi.subs({x: C[x], y: C[y]})} nghìn đồng")
print(f"- Mua {D[x]}kg bò, {D[y]}kg lợn => Chi phí: {chi_phi.subs({x: D[x], y: D[y]})} nghìn đồng")

print("\nKẾT LUẬN: Phương án tiết kiệm nhất là mua 0.3 kg thịt bò và 1.1 kg thịt lợn với chi phí 251 nghìn đồng.")

# Vẽ đồ thị miền nghiệm
sp.plot_implicit(he_dieu_kien, (x, -0.5, 2.5), (y, -0.5, 2), title="Mien nghiem bai toan dinh duong")
# ==========================================
# BÀI TIẾP THEO: TỐI ƯU LỢI NHUẬN ĐẦU TƯ TRÁI PHIẾU
# ==========================================
# 1. Khai báo biến (Đơn vị: triệu đồng)
# x là tiền mua TP chính phủ, y là tiền mua TP ngân hàng
x, y = sp.symbols('x y')

# 2. Hàm lợi nhuận: 7% x + 8% y + 12% (1200 - x - y)
loi_nhuan = 0.07*x + 0.08*y + 0.12*(1200 - x - y)

# 3. Hệ điều kiện (để vẽ đồ thị)
he_dieu_kien = sp.And(
    x >= 3*y,            # TP chính phủ >= 3 lần TP ngân hàng
    x + y >= 1000,       # TP doanh nghiệp (1200 - x - y) <= 200
    x + y <= 1200,       # Tổng tiền x, y không quá 1200
    x >= 0,
    y >= 0
)

# 4. Tìm các đỉnh của đa giác miền nghiệm
d1, d2, d3, d4 = (x - 3*y), (x + y - 1000), (x + y - 1200), y
danh_sach_dinh = [
    sp.solve([d1, d2], (x, y)), sp.solve([d1, d3], (x, y)),
    sp.solve([d4, d2], (x, y)), sp.solve([d4, d3], (x, y))
]

# 5. So sánh lợi nhuận tại các đỉnh
max_loi_nhuan = 0
phuong_an = None
for dinh in danh_sach_dinh:
    if dinh:
        tien_lai = loi_nhuan.subs({x: dinh[x], y: dinh[y]})
        if tien_lai > max_loi_nhuan:
            max_loi_nhuan = tien_lai
            phuong_an = dinh

# 6. In kết quả
z_toi_uu = 1200 - phuong_an[x] - phuong_an[y]
print("=== KẾT QUẢ ===")
print(f"Lợi nhuận lớn nhất: {max_loi_nhuan} triệu đồng.")
print(f"Cần đầu tư:\n- {phuong_an[x]} triệu vào TP Chính phủ\n- {phuong_an[y]} triệu vào TP Ngân hàng\n- {z_toi_uu} triệu vào TP Doanh nghiệp\n")

# 7. Vẽ đồ thị miền nghiệm
sp.plot_implicit(he_dieu_kien, (x, -100, 1300), (y, -100, 500), title="Mien nghiem")
# ==========================================
# BÀI TIẾP THEO: TỐI ƯU HIỆU QUẢ QUẢNG CÁO
# ==========================================
# 1. Khai báo biến
# x: thời gian quảng cáo đài phát thanh, y: truyền hình
x, y = sp.symbols('x y')

# 2. Hàm hiệu quả
hieu_qua = x + 8*y

# 3. Hệ điều kiện (để vẽ đồ thị)
# Chi phí: 80x + 400y <= 160000 -> rút gọn thành x + 5y <= 2000
he_dieu_kien = sp.And(
    x + 5*y <= 2000,
    x <= 900,
    y <= 360,
    x >= 0,
    y >= 0
)

# 4. Tìm tọa độ các đỉnh của đa giác miền nghiệm
d1, d2, d3, d4, d5 = (x + 5*y - 2000), (x - 900), (y - 360), x, y
cac_dinh = [
    sp.solve([d1, d2], (x, y)), sp.solve([d1, d3], (x, y)),
    sp.solve([d2, d5], (x, y)), sp.solve([d4, d3], (x, y)),
    sp.solve([d4, d5], (x, y))
]

# 5. Lọc các đỉnh hợp lệ và tìm mức hiệu quả cao nhất
max_hq = 0
phuong_an_qc = None
for d in cac_dinh:
    if d and (0 <= d[x] <= 900) and (0 <= d[y] <= 360) and (d[x] + 5*d[y] <= 2000):
        hq = hieu_qua.subs({x: d[x], y: d[y]})
        if hq > max_hq:
            max_hq = hq
            phuong_an_qc = d

# 6. In kết quả
print("=== KẾT QUẢ ===")
print(f"Để đạt hiệu quả lớn nhất (Điểm số hiệu quả: {max_hq}), công ty cần đặt:")
print(f"- {phuong_an_qc[x]} giây trên đài phát thanh")
print(f"- {phuong_an_qc[y]} giây trên đài truyền hình\n")

# 7. Vẽ đồ thị miền nghiệm
sp.plot_implicit(he_dieu_kien, (x, -100, 1000), (y, -50, 450), title="Mien nghiem")
# ==========================================
# BÀI 5: TỐI ƯU LỢI NHUẬN SẢN XUẤT SẢN PHẨM
# ==========================================
# 1. Khai báo biến
x, y = sp.symbols('x y')

# 2. Hàm lợi nhuận
F = 30*x + 50*y

# 3. Khai báo các đường thẳng ranh giới từ hệ bất phương trình
d1 = x + y - 5
d2 = y - 2
d3 = x + 2*y - 6
d4 = x
d5 = y

# 4. Tìm giao điểm của các cặp đường thẳng
cac_giao_diem = [
    sp.solve([d1, d2], (x, y)), sp.solve([d1, d3], (x, y)),
    sp.solve([d1, d4], (x, y)), sp.solve([d1, d5], (x, y)),
    sp.solve([d2, d3], (x, y)), sp.solve([d2, d4], (x, y)),
    sp.solve([d3, d5], (x, y)), sp.solve([d4, d5], (x, y))
]

# 5. Lọc ra các đỉnh nằm trong miền nghiệm (thỏa mãn TẤT CẢ điều kiện)
dinh_hop_le = []
for diem in cac_giao_diem:
    if diem and (diem[x] + diem[y] <= 5) and (diem[y] <= 2) and (diem[x] + 2*diem[y] <= 6) and (diem[x] >= 0) and (diem[y] >= 0):
        if diem not in dinh_hop_le:
            dinh_hop_le.append(diem)

# 6. Tính lợi nhuận tại các đỉnh để tìm phương án tối ưu
max_F = 0
x_toi_uu = 0
y_toi_uu = 0
for diem in dinh_hop_le:
    loi_nhuan = F.subs({x: diem[x], y: diem[y]})
    if loi_nhuan > max_F:
        max_F = loi_nhuan
        x_toi_uu = diem[x]
        y_toi_uu = diem[y]

# 7. In kết quả tính toán
print("=== KẾT QUẢ BÀI 5 ===")
print(f"Số sản phẩm loại I cần sản xuất (x): {x_toi_uu}")
print(f"Số sản phẩm loại II cần sản xuất (y): {y_toi_uu}")
print(f"Lợi nhuận lớn nhất đạt được: {max_F} nghìn đồng")
print(f"Giá trị của biểu thức x - y = {x_toi_uu - y_toi_uu}\n")

# 8. Vẽ đồ thị trực quan
he_dieu_kien = sp.And(x + y <= 5, y <= 2, x + 2*y <= 6, x >= 0, y >= 0)
sp.plot_implicit(he_dieu_kien, (x, -1, 7), (y, -1, 4), title="Mien nghiem Bai 5")
