from datetime import datetime
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Phần mềm Căn chỉnh Đồng tâm Trục - Rim & Face",
    layout="centered",
)

st.title("🔧 Căn chỉnh Đồng tâm Trục (Rim & Face)")
st.write(
    "Ứng dụng tính toán hiệu chỉnh tâm máy cho kỹ thuật viên bảo trì trực tiếp"
    " trên điện thoại/web."
)

# Khởi tạo session state cho vị trí input active và lịch sử
if "active_field" not in st.session_state:
  st.session_state.active_field = "a1"

if "history" not in st.session_state:
  st.session_state.history = []


def set_active(field_name):
  st.session_state.active_field = field_name


active = st.session_state.active_field


def get_color(field):
  return "red" if active == field else "black"


def get_weight(field):
  return "bold" if active == field else "normal"


# --- THÔNG TIN NGƯỜI DÙNG & GHI CHÚ ---
st.subheader("👤 Thông tin kỹ thuật viên & Ghi chú")
u_col1, u_col2 = st.columns(2)
with u_col1:
  tech_name = st.text_input("Họ tên người thực hiện:", value="Nguyễn Mạnh Hùng")
with u_col2:
  feedback_note = st.text_input(
      "Ý kiến phản hồi / Ghi chú (nếu có):", value=""
  )

# --- 0. Chọn cách gá ---
st.subheader("0. Chọn cách gá đồng hồ so")
setup_type = st.radio(
    "Chọn phương án gá đặt:",
    options=[1, 2],
    format_func=lambda x: (
        "Cách gá 1: Đồng hồ B đo mặt đầu bích phía đối diện"
        if x == 1
        else "Cách gá 2: Đồng hồ B đo mặt đầu bích cùng bên trục động"
    ),
)

# --- VẼ SƠ ĐỒ ĐỘNG (SVG) ---
svg_html = f"""
<div style="text-align: center; background-color: #f8f9fa; padding: 10px; border-radius: 10px; border: 1px solid #ddd;">
<svg width="100%" height="240" viewBox="0 0 500 220" style="max-width: 500px;">
    <g transform="translate(130, 110)">
        <circle cx="0" cy="0" r="65" fill="white" stroke="black" stroke-width="2"/>
        <text x="0" y="-80" font-size="13" font-weight="bold" text-anchor="middle" fill="#008000">Mặt đồng hồ RIM (a)</text>
        <circle cx="0" cy="-65" r="{6 if active=='a1' else 4}" fill="{get_color('a1')}"/>
        <text x="0" y="-48" font-size="{12 if active=='a1' else 10}" font-weight="{get_weight('a1')}" text-anchor="middle" fill="{get_color('a1')}">a1 (12h)</text>
        <circle cx="65" cy="0" r="{6 if active=='a2' else 4}" fill="{get_color('a2')}"/>
        <text x="75" y="4" font-size="{12 if active=='a2' else 10}" font-weight="{get_weight('a2')}" text-anchor="start" fill="{get_color('a2')}">a2 (3h)</text>
        <circle cx="0" cy="65" r="{6 if active=='a3' else 4}" fill="{get_color('a3')}"/>
        <text x="0" y="80" font-size="{12 if active=='a3' else 10}" font-weight="{get_weight('a3')}" text-anchor="middle" fill="{get_color('a3')}">a3 (6h)</text>
        <circle cx="-65" cy="0" r="{6 if active=='a4' else 4}" fill="{get_color('a4')}"/>
        <text x="-75" y="4" font-size="{12 if active=='a4' else 10}" font-weight="{get_weight('a4')}" text-anchor="end" fill="{get_color('a4')}">a4 (9h)</text>
    </g>
    <g transform="translate(370, 110)">
        <circle cx="0" cy="0" r="65" fill="white" stroke="black" stroke-width="2"/>
        <text x="0" y="-80" font-size="13" font-weight="bold" text-anchor="middle" fill="#800080">Mặt đồng hồ FACE (b)</text>
        <circle cx="0" cy="-65" r="{6 if active=='b1' else 4}" fill="{get_color('b1')}"/>
        <text x="0" y="-48" font-size="{12 if active=='b1' else 10}" font-weight="{get_weight('b1')}" text-anchor="middle" fill="{get_color('b1')}">b1 (12h)</text>
        <circle cx="65" cy="0" r="{6 if active=='b2' else 4}" fill="{get_color('b2')}"/>
        <text x="75" y="4" font-size="{12 if active=='b2' else 10}" font-weight="{get_weight('b2')}" text-anchor="start" fill="{get_color('b2')}">b2 (3h)</text>
        <circle cx="0" cy="65" r="{6 if active=='b3' else 4}" fill="{get_color('b3')}"/>
        <text x="0" y="80" font-size="{12 if active=='b3' else 10}" font-weight="{get_weight('b3')}" text-anchor="middle" fill="{get_color('b3')}">b3 (6h)</text>
        <circle cx="-65" cy="0" r="{6 if active=='b4' else 4}" fill="{get_color('b4')}"/>
        <text x="-75" y="4" font-size="{12 if active=='b4' else 10}" font-weight="{get_weight('b4')}" text-anchor="end" fill="{get_color('b4')}">b4 (9h)</text>
    </g>
</svg>
<p style="font-size: 13px; color: #555; margin-top: 5px;">💡 Vị trí đang chọn: <b style="color: red;">{active.upper()}</b></p>
</div>
"""

st.markdown(svg_html, unsafe_allow_html=True)
st.write("")

# --- 1. Thông số hình học ---
st.subheader("1. Thông số hình học (mm)")
c1, c2, c3 = st.columns(3)
with c1:
  L1_str = st.text_input("L1 (Từ khớp tới chân trước):", value="100")
with c2:
  L2_str = st.text_input("L2 (Từ khớp tới chân sau):", value="300")
with c3:
  D_str = st.text_input("D (Đường kính vòng quay / Khớp):", value="200")

# --- 2. Đồng hồ Rim ---
st.subheader("2. Đồng hồ Hướng kính (RIM - a) (mm)")
rc1, rc2 = st.columns(2)
with rc1:
  a1_str = st.text_input(
      "a1 (12h):",
      value="0",
      on_change=set_active,
      args=("a1",),
      key="input_a1",
  )
  a3_str = st.text_input(
      "a3 (6h):",
      value="0",
      on_change=set_active,
      args=("a3",),
      key="input_a3",
  )
with rc2:
  a2_str = st.text_input(
      "a2 (3h):",
      value="0",
      on_change=set_active,
      args=("a2",),
      key="input_a2",
  )
  a4_str = st.text_input(
      "a4 (9h):",
      value="0",
      on_change=set_active,
      args=("a4",),
      key="input_a4",
  )

# --- 3. Đồng hồ Face ---
st.subheader("3. Đồng hồ Mặt bích (FACE - b) (mm)")
fc1, fc2 = st.columns(2)
with fc1:
  b1_str = st.text_input(
      "b1 (12h):",
      value="0",
      on_change=set_active,
      args=("b1",),
      key="input_b1",
  )
  b3_str = st.text_input(
      "b3 (6h):",
      value="0",
      on_change=set_active,
      args=("b3",),
      key="input_b3",
  )
with fc2:
  b2_str = st.text_input(
      "b2 (3h):",
      value="0",
      on_change=set_active,
      args=("b2",),
      key="input_b2",
  )
  b4_str = st.text_input(
      "b4 (9h):",
      value="0",
      on_change=set_active,
      args=("b4",),
      key="input_b4",
  )


def parse_val(val):
  return float(val.strip().replace(",", "."))


# --- 4. Nút Tính toán & Lưu thông tin ---
if st.button("🚀 TÍNH TOÁN VÀ GHI NHẬN", type="primary", use_container_width=True):
  try:
    L1 = parse_val(L1_str)
    L2 = parse_val(L2_str)
    D = parse_val(D_str)
    a1, a2, a3, a4 = (
        parse_val(a1_str),
        parse_val(a2_str),
        parse_val(a3_str),
        parse_val(a4_str),
    )
    b1, b2, b3, b4 = (
        parse_val(b1_str),
        parse_val(b2_str),
        parse_val(b3_str),
        parse_val(b4_str),
    )

    if setup_type == 1:
      diff_b_vert = b3 - b1
      diff_b_horiz = b4 - b2
    else:
      diff_b_vert = b1 - b3
      diff_b_horiz = b2 - b4

    ya = (a3 - a1) / 2
    yb1 = ya + (diff_b_vert / D) * L1
    yb2 = ya + (diff_b_vert / D) * L2

    xa = (a2 - a4) / 2
    xb1 = xa + (diff_b_horiz / D) * L1
    xb2 = xa + (diff_b_horiz / D) * L2

    # Ghi nhận thời gian và lưu vào lịch sử phiên làm việc
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_item = {
        "Thời gian": current_time,
        "Người thực hiện": tech_name if tech_name else "Không rõ",
        "Cách gá": f"Cách gá {setup_type}",
        "L1 (mm)": L1,
        "L2 (mm)": L2,
        "D (mm)": D,
        "Chân trước đứng (mm)": round(yb1, 3),
        "Chân sau đứng (mm)": round(yb2, 3),
        "Chân trước ngang (mm)": round(xb1, 3),
        "Chân sau ngang (mm)": round(xb2, 3),
        "Phản hồi/Ghi chú": feedback_note if feedback_note else "Không có",
    }
    st.session_state.history.append(log_item)

    st.success(
        f"Đã tính toán thành công và ghi nhận lịch sử lúc {current_time}!"
    )

    # Hiển thị kết quả chi tiết
    st.markdown("### 📊 Kết quả hiệu chỉnh chi tiết")

    st.markdown("#### 1. Phương đứng (VERTICAL - Căn đệm Shim):")
    st.code(
        f"• Chân trước (L1): {yb1:+.3f} mm\n  ➔ {'Thêm lá căn dày ' + f'{abs(yb1):.3f}' if yb1 >= 0 else 'Rút bớt lá căn ' + f'{abs(yb1):.3f}'} mm\n\n• Chân sau (L2):   {yb2:+.3f} mm\n  ➔ {'Thêm lá căn dày ' + f'{abs(yb2):.3f}' if yb2 >= 0 else 'Rút bớt lá căn ' + f'{abs(yb2):.3f}'} mm"
    )

    st.markdown("#### 2. Phương ngang (HORIZONTAL - Dịch chuyển):")
    st.code(
        f"• Chân trước (L1): {xb1:+.3f} mm\n  ➔ {'Dịch chuyển sang phải ' + f'{abs(xb1):.3f}' if xb1 >= 0 else 'Dịch chuyển sang trái ' + f'{abs(xb1):.3f}'} mm\n\n• Chân sau (L2):   {xb2:+.3f} mm\n  ➔ {'Dịch chuyển sang phải ' + f'{abs(xb2):.3f}' if xb2 >= 0 else 'Dịch chuyển sang trái ' + f'{abs(xb2):.3f}'} mm"
    )

  except ValueError:
    st.error(
        "⚠️ Vui lòng kiểm tra lại dữ liệu đầu vào! Đảm bảo tất cả các ô đều"
        " là số hợp lệ."
    )

# --- HIỂN THỊ LỊCH SỬ VÀ TẢI XUỐNG BÁO CÁO ---
if st.session_state.history:
  st.markdown("---")
  st.subheader("📋 Lịch sử ghi nhận trong phiên làm việc")
  df_history = pd.DataFrame(st.session_state.history)
  st.dataframe(df_history, use_container_width=True)

  # Nút tải xuống file CSV
  csv_data = df_history.to_csv(index=False).encode("utf-8-sig")
  st.download_button(
      label="📥 Tải xuống lịch sử báo cáo (CSV)",
      data=csv_data,
      file_name=f"lich_su_can_chinh_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
      mime="text/csv",
  )
