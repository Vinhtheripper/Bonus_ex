import pandas as pd
import plotly.express as px
from PyQt6 import QtWidgets


def load_file(self):
    file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Choose Excel file", "", "Excel Files (*.xlsx)")
    if file_path:
        self.lineEdit.setText(file_path)


def generate_chart(self):
    file_path = self.lineEdit.text()
    if file_path:
        df = pd.read_excel(file_path)
        df = df.dropna(subset=['Học Kỳ', 'Mã học phần', 'Tên học phần'])
        df['Tín Chỉ'] = pd.to_numeric(df['Tín Chỉ'], errors='coerce')
        df = df.dropna(subset=['Tín Chỉ'])
        df['Học Kỳ'] = df['Học Kỳ'].apply(lambda x: f'Học Kỳ {int(x)}')

        self.fig = px.sunburst(
            df,
            path=['Học Kỳ', 'Bắt buộc/tự chọn', 'Tên học phần'],
            values='Tín Chỉ',
            title='Nguyen Quang Vinh-K234111460'
        )

        self.fig.show()
