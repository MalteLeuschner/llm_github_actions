from typing import Dict, List
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


class DataVisualizer:
    """:
    DataVisualizer class for visualizing financial data.

    Args:
        data (Dict[str, List[str]]): A dictionary containing financial data.

    Raises:
        ValueError: If the input data is not in the correct format."""

    def __init__(self, data: Dict[str, List[str]]) -> None:
        """Initializes a DataVisualizer instance with the given data.

        Initializes a pandas DataFrame from the provided data.

        Args:
         data (Dict[str, List[str]]): A dictionary containing the data to be visualized.

        Returns:
         None"""
        self.df = pd.DataFrame(data)

    def display_data(self) -> None:
        """Displays the transaction data in a Streamlit dataframe.

        Displays the transaction data in a Streamlit dataframe, allowing the user to view the data.

        Args:
            self (DataVisualizer): The DataVisualizer instance.

        Returns:
            None"""
        st.write("### Transaction Data")
        st.dataframe(self.df)

    def plot_line_chart(self) -> None:
        """Plots a line chart of transaction amounts over time.

        This function generates a line chart using the provided data, with the date on the x-axis and the amount on the y-axis.

        Args:
            self (DataVisualizer): The DataVisualizer instance.

        Returns:
            None

        Raises:
            ValueError: If the data is not in the correct format."""
        st.write("### Line Chart of Amounts")
        fig, ax = plt.subplots()
        ax.plot(self.df["Date"], self.df["Amount"], marker="o")
        ax.set_xlabel("Date")
        ax.set_ylabel("Amount")
        ax.set_title("Transaction Amounts Over Time")
        st.pyplot(fig)

    def plot_bar_chart(self) -> None:
        """Plots a bar chart of transaction amounts over time.

        This function generates a bar chart using the provided data, with the x-axis
        representing the dates and the y-axis representing the amounts.

        Args:
          self (DataVisualizer): The DataVisualizer instance.

        Returns:
          None

        Raises:
          ValueError: If the data is not in the correct format."""
        st.write("### Bar Chart of Amounts")
        fig, ax = plt.subplots()
        ax.bar(self.df["Date"], self.df["Amount"])
        ax.set_xlabel("Date")
        ax.set_ylabel("Amount")
        ax.set_title("Transaction Amounts Over Time")
        st.pyplot(fig)


def main() -> None:
    """Main function of the script.

    Runs the entire data visualization process.

    Args:
        None
    Returns:
        None
    Raises:
        None"""
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
