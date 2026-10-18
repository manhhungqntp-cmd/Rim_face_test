# Tạo mã SVG cho mặt đồng hồ và sơ đồ (Đã mở rộng khung nhìn để không bị cắt chữ)
svg_html = f"""
<div style="text-align: center; background-color: #f8f9fa; padding: 10px; border-radius: 10px; border: 1px solid #ddd;">
<svg width="100%" height="240" viewBox="0 0 500 220" style="max-width: 500px;">
    <!-- Mặt đồng hồ RIM (a) -->
    <g transform="translate(130, 110)">
        <circle cx="0" cy="0" r="65" fill="white" stroke="black" stroke-width="2"/>
        <text x="0" y="-80" font-size="13" font-weight="bold" text-anchor="middle" fill="#008000">Mặt đồng hồ RIM (a)</text>
        
        <!-- a1 (12h) -->
        <circle cx="0" cy="-65" r="{6 if active=='a1' else 4}" fill="{get_color('a1')}"/>
        <text x="0" y="-48" font-size="{12 if active=='a1' else 10}" font-weight="{get_weight('a1')}" text-anchor="middle" fill="{get_color('a1')}">a1 (12h)</text>
        
        <!-- a2 (3h) -->
        <circle cx="65" cy="0" r="{6 if active=='a2' else 4}" fill="{get_color('a2')}"/>
        <text x="75" y="4" font-size="{12 if active=='a2' else 10}" font-weight="{get_weight('a2')}" text-anchor="start" fill="{get_color('a2')}">a2 (3h)</text>
        
        <!-- a3 (6h) -->
        <circle cx="0" cy="65" r="{6 if active=='a3' else 4}" fill="{get_color('a3')}"/>
        <text x="0" y="80" font-size="{12 if active=='a3' else 10}" font-weight="{get_weight('a3')}" text-anchor="middle" fill="{get_color('a3')}">a3 (6h)</text>
        
        <!-- a4 (9h) -->
        <circle cx="-65" cy="0" r="{6 if active=='a4' else 4}" fill="{get_color('a4')}"/>
        <text x="-75" y="4" font-size="{12 if active=='a4' else 10}" font-weight="{get_weight('a4')}" text-anchor="end" fill="{get_color('a4')}">a4 (9h)</text>
    </g>

    <!-- Mặt đồng hồ FACE (b) -->
    <g transform="translate(370, 110)">
        <circle cx="0" cy="0" r="65" fill="white" stroke="black" stroke-width="2"/>
        <text x="0" y="-80" font-size="13" font-weight="bold" text-anchor="middle" fill="#800080">Mặt đồng hồ FACE (b)</text>
        
        <!-- b1 (12h) -->
        <circle cx="0" cy="-65" r="{6 if active=='b1' else 4}" fill="{get_color('b1')}"/>
        <text x="0" y="-48" font-size="{12 if active=='b1' else 10}" font-weight="{get_weight('b1')}" text-anchor="middle" fill="{get_color('b1')}">b1 (12h)</text>
        
        <!-- b2 (3h) -->
        <circle cx="65" cy="0" r="{6 if active=='b2' else 4}" fill="{get_color('b2')}"/>
        <text x="75" y="4" font-size="{12 if active=='b2' else 10}" font-weight="{get_weight('b2')}" text-anchor="start" fill="{get_color('b2')}">b2 (3h)</text>
        
        <!-- b3 (6h) -->
        <circle cx="0" cy="65" r="{6 if active=='b3' else 4}" fill="{get_color('b3')}"/>
        <text x="0" y="80" font-size="{12 if active=='b3' else 10}" font-weight="{get_weight('b3')}" text-anchor="middle" fill="{get_color('b3')}">b3 (6h)</text>
        
        <!-- b4 (9h) -->
        <circle cx="-65" cy="0" r="{6 if active=='b4' else 4}" fill="{get_color('b4')}"/>
        <text x="-75" y="4" font-size="{12 if active=='b4' else 10}" font-weight="{get_weight('b4')}" text-anchor="end" fill="{get_color('b4')}">b4 (9h)</text>
    </g>
</svg>
<p style="font-size: 13px; color: #555; margin-top: 5px;">💡 Vị trí đang chọn: <b style="color: red;">{active.toUpperCase()}</b> (Đang nhấp sáng trên sơ đồ)</p>
</div>
"""
