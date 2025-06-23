import pandas as pd
from fpdf import FPDF
df = pd.read_csv("data.csv")
total, avg = df["Score"].sum(), df["Score"].mean()
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, "Score Report", ln=True, align='C')
pdf.cell(0, 10, f"Total: {total}, Average: {avg:.2f}", ln=True)
for name, score in zip(df["Name"], df["Score"]):
    pdf.cell(0, 10, f"{name}: {score}", ln=True)
pdf.output("report.pdf")
