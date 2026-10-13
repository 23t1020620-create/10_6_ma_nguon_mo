from flask import Flask, jsonify, request, url_for, make_response
import csv
import io
from markupsafe import escape

app = Flask(__name__)
STUDENTS = {

    "23T1020001": {"name": "Nguyễn Văn An", "lop": "K47A",
    "scores": {"PMMNM": 8.5, "CSDL": 7.0,"MMT": 9.0}},

    "23T1020002": {"name": "Trần Thị Bình", "lop": "K47A",
    "scores": {"PMMNM": 6.0, "CSDL": 5.5, "MMT": 7.0}},

    "23T1020003": {"name": "Lê Hoàng Cường", "lop": "K47B",
    "scores": {"PMMNM": 9.5, "CSDL": 9.0}},

    "23T1020004": {"name": "Phạm Minh Dũng","lop": "K47B",
    "scores": {"PMMNM": 4.0, "CSDL": 3.5, "MMT": 5.0}},

    "23T1020005": {"name": "Hoàng Thu Hà", "lop": "K47A",
    "scores": {}},


    "23T1020006": {"name": "Võ Quốc Khánh", "lop": "K47C",
    "scores": {"PMMNM": 7.5,"MMT": 8.0}},
}

@app.route("/")
def home():

    tong_sv = len(STUDENTS)

    ds_lop = set()

    for sv in STUDENTS.values():
        ds_lop.add(sv["lop"])

    so_lop = len(ds_lop)

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Quản lý sinh viên</title>

        <style>
            * {
                box-sizing: border-box;
            }

            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f4f7fb;
                color: #333;
            }

            .container {
                width: 90%;
                max-width: 1000px;
                margin: 50px auto;
            }

            .header {
                background: #2563eb;
                color: white;
                padding: 35px;
                border-radius: 18px;
                text-align: center;
            }

            .header h1 {
                margin: 0 0 10px;
                font-size: 32px;
            }

            .header p {
                margin: 0;
                font-size: 16px;
            }

            .cards {
                display: flex;
                gap: 20px;
                margin: 25px 0;
            }

            .card {
                flex: 1;
                background: white;
                padding: 25px;
                border-radius: 15px;
                text-align: center;
                box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            }

            .card h2 {
                margin: 0;
                color: #2563eb;
                font-size: 30px;
            }

            .card p {
                margin: 8px 0 0;
                color: #666;
            }

            .search-box {
                background: white;
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.08);
                margin-bottom: 25px;
            }

            .search-box h2 {
                margin-top: 0;
                color: #333;
            }

            .search-form {
                display: flex;
                gap: 10px;
            }

            .search-form input {
                flex: 1;
                padding: 13px 15px;
                border: 1px solid #d1d5db;
                border-radius: 8px;
                font-size: 16px;
                outline: none;
            }

            .search-form input:focus {
                border-color: #2563eb;
            }

            .search-form button {
                padding: 13px 25px;
                background: #2563eb;
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 16px;
                cursor: pointer;
            }

            .search-form button:hover {
                background: #1d4ed8;
            }

            .menu {
                background: white;
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            }

            .menu h2 {
                margin-top: 0;
            }

            .menu a {
                display: inline-block;
                text-decoration: none;
                background: #eff6ff;
                color: #2563eb;
                padding: 12px 18px;
                margin: 5px;
                border-radius: 8px;
                font-weight: bold;
            }

            .menu a:hover {
                background: #2563eb;
                color: white;
            }
        </style>
    </head>

    <body>

        <div class="container">

            <div class="header">
                <h1>HỆ THỐNG QUẢN LÝ SINH VIÊN</h1>
                <p>Quản lý thông tin và kết quả học tập</p>
            </div>

            <div class="cards">

                <div class="card">
                    <h2>""" + str(tong_sv) + """</h2>
                    <p>Tổng số sinh viên</p>
                </div>

                <div class="card">
                    <h2>""" + str(so_lop) + """</h2>
                    <p>Số lớp</p>
                </div>

            </div>

            <!-- THANH SEARCH CÂU 6 -->

            <div class="search-box">

                <h2>Tìm kiếm sinh viên</h2>

                <form class="search-form" action="/search" method="GET">

                    <input
                        type="text"
                        name="q"
                        placeholder="Nhập họ tên hoặc MSSV..."
                        autocomplete="off"
                    >

                    <button type="submit">
                        Tìm kiếm
                    </button>

                </form>

            </div>

            <div class="menu">

                <h2>Chức năng</h2>

                <a href="/students">
                    Danh sách sinh viên
                </a>

                <a href="/api/students">
                    API sinh viên
                </a>

            </div>

        </div>

    </body>
    </html>
    """

    tong_sv = len(STUDENTS)

    ds_lop = set()

    for sv in STUDENTS.values():
        ds_lop.add(sv["lop"])

    so_lop = len(ds_lop)

    return f"""
    <h1>Quản lý sinh viên</h1>
    <p>Tổng số sinh viên: {tong_sv}</p>
    <p>Số lớp: {so_lop}</p>

    <a href="{url_for('student_list')}">
        Danh sách sinh viên
    </a>

    <br><br>

    <a href="{url_for('search')}">
        Tìm kiếm sinh viên
    </a>
    """



@app.route("/api/students")
def api_students():
    return jsonify(STUDENTS)


# =========================
# TÍNH ĐIỂM TRUNG BÌNH
# =========================

def diem_tb(scores):

    if len(scores) == 0:
        return None

    return sum(scores.values()) / len(scores)


def xep_loai(dtb):

    if dtb is None:
        return "-"

    if dtb >= 8:
        return "Giỏi"

    elif dtb >= 6.5:
        return "Khá"

    elif dtb >= 5:
        return "Trung bình"

    else:
        return "Yếu"



@app.route("/students")
def student_list():

    lop = request.args.get("lop")

    ds_lop = sorted(set(
        sv["lop"] for sv in STUDENTS.values()
    ))

    result = []

    for mssv, sv in STUDENTS.items():

        if lop is None or sv["lop"].lower() == lop.lower():

            dtb = diem_tb(sv["scores"])

            result.append({
                "MSSV": mssv,
                "name": sv["name"],
                "lop": sv["lop"],
                "diem_tb": dtb,
                "xep_loai": xep_loai(dtb)
            })

    if len(result) == 0:

        return """
        <div style="
            text-align:center;
            margin-top:100px;
            font-family:Arial;
        ">

            <h2>Không có sinh viên phù hợp.</h2>

            <a href="/students">
                Quay lại danh sách
            </a>

        </div>
        """

    html = """
    <!DOCTYPE html>

    <html>

    <head>

        <meta charset="UTF-8">

        <title>Danh sách sinh viên</title>

        <style>

            * {
                box-sizing: border-box;
            }

            body {
                margin: 0;
                font-family: Arial;
                background: #f4f7fb;
                color: #333;
            }

            .container {
                width: 92%;
                max-width: 1100px;
                margin: 40px auto;
            }

            .header {
                background: #2563eb;
                color: white;
                padding: 25px 30px;
                border-radius: 15px;
                margin-bottom: 25px;
            }

            .filter {
                background: white;
                padding: 18px;
                border-radius: 12px;
                margin-bottom: 20px;
            }

            .filter a {
                display: inline-block;
                padding: 8px 15px;
                margin: 4px;
                border-radius: 20px;
                text-decoration: none;
                color: #2563eb;
                background: #eff6ff;
                font-weight: bold;
            }

            .filter a:hover {
                background: #2563eb;
                color: white;
            }

            .table-box {
                background: white;
                padding: 20px;
                border-radius: 12px;
                overflow-x: auto;
            }

            table {
                width: 100%;
                border-collapse: collapse;
            }

            th {
                background: #2563eb;
                color: white;
                padding: 14px;
                text-align: left;
            }

            td {
                padding: 13px;
                border-bottom: 1px solid #ddd;
            }

            tr:hover {
                background: #f8fafc;
            }

            .mssv {
                color: #2563eb;
                font-weight: bold;
                text-decoration: none;
            }

            .class {
                background: #dbeafe;
                color: #1d4ed8;
                padding: 5px 10px;
                border-radius: 15px;
                font-weight: bold;
            }

            .good {
                color: #16a34a;
                font-weight: bold;
            }

            .average {
                color: #ca8a04;
                font-weight: bold;
            }

            .weak {
                color: #dc2626;
                font-weight: bold;
            }

            .back {
                display: inline-block;
                margin-top: 20px;
                color: #2563eb;
                text-decoration: none;
            }

        </style>

    </head>

    <body>

        <div class="container">

            <div class="header">

                <h1>Danh sách sinh viên</h1>

                <p>
                    Quản lý thông tin và kết quả học tập
                </p>

            </div>

            <div class="filter">

                <b>Lọc theo lớp:</b>

                <a href="/students">
                    Tất cả
                </a>
    """

    for l in ds_lop:

        html += f"""
                <a href="{url_for('student_list', lop=l)}">
                    {l}
                </a>
        """

    html += """
            </div>

            <div class="table-box">

                <table>

                    <tr>
                        <th>MSSV</th>
                        <th>Họ tên</th>
                        <th>Lớp</th>
                        <th>Điểm TB</th>
                        <th>Xếp loại</th>
                    </tr>
    """

    for sv in result:

        link = url_for(
            "student_detail",
            mssv=sv["MSSV"]
        )

        if sv["diem_tb"] is None:
            dtb = "-"
        else:
            dtb = f'{sv["diem_tb"]:.2f}'

        if sv["xep_loai"] in ["Giỏi", "Khá"]:
            loai_class = "good"

        elif sv["xep_loai"] == "Trung bình":
            loai_class = "average"

        else:
            loai_class = "weak"

        html += f"""

                    <tr>

                        <td>
                            <a class="mssv" href="{link}">
                                {sv["MSSV"]}
                            </a>
                        </td>

                        <td>
                            {sv["name"]}
                        </td>

                        <td>
                            <span class="class">
                                {sv["lop"]}
                            </span>
                        </td>

                        <td>
                            {dtb}
                        </td>

                        <td class="{loai_class}">
                            {sv["xep_loai"]}
                        </td>

                    </tr>

        """

    html += """

                </table>

            </div>

            <a class="back" href="/">
                ← Về trang chủ
            </a>

        </div>

    </body>

    </html>
    """

    return html



@app.route("/students/<mssv>")
def student_detail(mssv):

    if mssv not in STUDENTS:

        return (
            f"Không có sinh viên với MSSV = {escape(mssv)}.",
            404
        )

    sv = STUDENTS[mssv]

    dtb = diem_tb(sv["scores"])

    if dtb is None:
        dtb_hien_thi = "-"
    else:
        dtb_hien_thi = f"{dtb:.2f}"

    html = f"""

    <!DOCTYPE html>

    <html>

    <head>

        <meta charset="UTF-8">

        <title>Chi tiết sinh viên</title>

        <style>

            body {{
                font-family: Arial;
                background: #f4f7fb;
                margin: 0;
            }}

            .container {{
                width: 90%;
                max-width: 800px;
                margin: 50px auto;
            }}

            .card {{
                background: white;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            }}

            h1 {{
                color: #2563eb;
            }}

            .info {{
                padding: 10px 0;
                border-bottom: 1px solid #eee;
            }}

            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }}

            th {{
                background: #2563eb;
                color: white;
                padding: 12px;
            }}

            td {{
                padding: 12px;
                border-bottom: 1px solid #ddd;
            }}

            a {{
                color: #2563eb;
                text-decoration: none;
                font-weight: bold;
            }}

            .button {{
                display: inline-block;
                margin-top: 20px;
                padding: 10px 15px;
                background: #2563eb;
                color: white;
                border-radius: 8px;
            }}

        </style>

    </head>

    <body>

        <div class="container">

            <div class="card">

                <h1>Chi tiết sinh viên</h1>

                <div class="info">
                    <b>MSSV:</b> {escape(mssv)}
                </div>

                <div class="info">
                    <b>Họ tên:</b> {escape(sv["name"])}
                </div>

                <div class="info">
                    <b>Lớp:</b>
                    <a href="{url_for('student_list', lop=sv['lop'])}">
                        {escape(sv["lop"])}
                    </a>
                </div>

                <div class="info">
                    <b>Điểm trung bình:</b> {dtb_hien_thi}
                </div>

                <div class="info">
                    <b>Xếp loại:</b> {xep_loai(dtb)}
                </div>

                <h2>Bảng điểm</h2>

                <table>

                    <tr>
                        <th>Học phần</th>
                        <th>Điểm</th>
                    </tr>
    """

    for mon, diem in sv["scores"].items():

        html += f"""
                    <tr>
                        <td>{escape(mon)}</td>
                        <td>{diem}</td>
                    </tr>
        """

    html += f"""

                </table>

                <a class="button"
                   href="{url_for('export_csv', mssv=mssv)}">
                    Tải bảng điểm CSV
                </a>

                <br>

                <a href="{url_for('student_list')}">
                    ← Quay lại danh sách
                </a>

            </div>

        </div>

    </body>

    </html>

    """

    return html



@app.route("/sv/<mssv>")
def short_student(mssv):

    if mssv not in STUDENTS:

        return (
            f"Không có sinh viên với MSSV = {escape(mssv)}.",
            404
        )

    return (
        "",
        301,
        {
            "Location": url_for(
                "student_detail",
                mssv=mssv
            )
        }
    )



@app.route("/students/<mssv>/export")
def export_csv(mssv):

    if mssv not in STUDENTS:

        return (
            f"Không có sinh viên với MSSV = {escape(mssv)}.",
            404
        )

    sv = STUDENTS[mssv]

    output = io.StringIO()

    writer = csv.writer(output)

    writer.writerow(["hoc_phan", "diem"])

    for mon, diem in sv["scores"].items():

        writer.writerow([mon, diem])

    response = make_response(
        output.getvalue()
    )

    response.headers["Content-Type"] = (
        "text/csv; charset=utf-8"
    )

    response.headers["Content-Disposition"] = (
        f"attachment; filename=diem_{mssv}.csv"
    )

    return response



@app.route("/search")
def search():

    q = request.args.get("q", "")

    q_lower = q.lower()

    result = []

    for mssv, sv in STUDENTS.items():

        # Tìm trong MSSV hoặc họ tên
        if (
            q_lower in mssv.lower()
            or q_lower in sv["name"].lower()
        ):

            result.append({
                "MSSV": mssv,
                "name": sv["name"],
                "lop": sv["lop"]
            })

    html = f"""
    <!DOCTYPE html>

    <html>

    <head>

        <meta charset="UTF-8">

        <title>Tìm kiếm sinh viên</title>

        <style>

            * {{
                box-sizing: border-box;
            }}

            body {{
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f4f7fb;
            }}

            .container {{
                width: 90%;
                max-width: 900px;
                margin: 50px auto;
            }}

            .header {{
                background: #2563eb;
                color: white;
                padding: 25px;
                border-radius: 15px;
                margin-bottom: 25px;
            }}

            .search-box {{
                background: white;
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.08);
                margin-bottom: 25px;
            }}

            form {{
                display: flex;
                gap: 10px;
            }}

            input {{
                flex: 1;
                padding: 12px 15px;
                border: 1px solid #d1d5db;
                border-radius: 8px;
                font-size: 16px;
            }}

            button {{
                padding: 12px 22px;
                border: none;
                border-radius: 8px;
                background: #2563eb;
                color: white;
                font-weight: bold;
                cursor: pointer;
            }}

            button:hover {{
                background: #1d4ed8;
            }}

            .result {{
                background: white;
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            }}

            .student {{
                padding: 15px;
                border-bottom: 1px solid #eee;
            }}

            .student:last-child {{
                border-bottom: none;
            }}

            .student a {{
                color: #2563eb;
                font-weight: bold;
                text-decoration: none;
                font-size: 17px;
            }}

            .student a:hover {{
                text-decoration: underline;
            }}

            .not-found {{
                text-align: center;
                padding: 30px;
                color: #666;
            }}

            .back {{
                display: inline-block;
                margin-top: 20px;
                color: #2563eb;
                text-decoration: none;
            }}

        </style>

    </head>

    <body>

        <div class="container">

            <div class="header">

                <h1>Tìm kiếm sinh viên</h1>

                <p>
                    Tìm theo họ tên hoặc MSSV
                </p>

            </div>

            <div class="search-box">

                <form method="GET"
                      action="{url_for('search')}">

                    <input
                        type="text"
                        name="q"
                        value="{escape(q)}"
                        placeholder="Nhập họ tên hoặc MSSV..."
                    >

                    <button type="submit">
                        Tìm kiếm
                    </button>

                </form>

            </div>
    """

    if q == "":

        html += """
            <div class="result">

                <div class="not-found">
                    Nhập từ khóa để tìm sinh viên.
                </div>

            </div>
        """

    elif len(result) == 0:

        html += f"""
            <div class="result">

                <div class="not-found">

                    Không tìm thấy sinh viên với từ khóa:
                    <b>{escape(q)}</b>

                </div>

            </div>
        """

    else:

        html += f"""
            <div class="result">

                <h2>
                    Tìm thấy {len(result)} kết quả
                    cho "{escape(q)}"
                </h2>
        """

        for sv in result:

            link = url_for(
                "student_detail",
                mssv=sv["MSSV"]
            )

            html += f"""
                <div class="student">

                    <a href="{link}">
                        {escape(sv["MSSV"])}
                    </a>

                    <br>

                    <span>
                        {escape(sv["name"])}
                        - Lớp {escape(sv["lop"])}
                    </span>

                </div>
            """

        html += """
            </div>
        """

    html += f"""

            <a class="back"
               href="{url_for('student_list')}">
                ← Về danh sách sinh viên
            </a>

        </div>

    </body>

    </html>
    """

    return html


if __name__ == "__main__":
    app.run(debug=True)
