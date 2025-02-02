from typing import List, Dict
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


class DataVisualizer:

    def __init__(self, data):
        self.df = pd.DataFrame(data)

    def display_data(self):
        st.write("### Transaction Data")
        st.dataframe(self.df)

    def plot_line_chart(self):
        st.write("### Line Chart of Amounts")
        fig, ax = plt.subplots()
        ax.plot(self.df["Date"], self.df["Amount"], marker="o")
        ax.set_xlabel("Date")
        ax.set_ylabel("Amount")
        ax.set_title("Transaction Amounts Over Time")
        st.pyplot(fig)

    def plot_bar_chart(self):
        st.write("### Bar Chart of Amounts")
        fig, ax = plt.subplots()
        ax.bar(self.df["Date"], self.df["Amount"])
        ax.set_xlabel("Date")
        ax.set_ylabel("Amount")
        ax.set_title("Transaction Amounts Over Time")
        st.pyplot(fig)


def main():
    data = {
        "Date": ["2024-07-01", "2024-07-02", "2024-07-03", "2024-07-04", "2024-07-05"],
        "Amount": [100, 200, 150, 300, 250],
    }
    visualizer = DataVisualizer(data)
    st.title("Financial Data Visualization")
    visualizer.display_data()
    visualizer.plot_line_chart()
    visualizer.plot_bar_chart()


if __name__ == "__main__":
    main()
