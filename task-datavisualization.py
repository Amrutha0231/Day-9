import matplotlib.pyplot as plt
import pandas as pd

def create_chart(csv_file, chart_type='bar'):
    # Read CSV file into a pandas DataFrame
    data = pd.read_csv(csv_file)

    # Display a bar chart or line chart based on user's choice
    if chart_type == 'bar':
        data.plot(kind='bar')
        plt.title('Bar Chart')
    elif chart_type == 'line':
        data.plot(kind='line')
        plt.title('Line Chart')
    else:
        print("Invalid chart type. Please choose 'bar' or 'line'.")

    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.show()

if __name__ == "__main__":
    csv_file = input("CSV File: ")
    chart_type = input("Chart Type (bar/line): ").lower()
    create_chart(csv_file, chart_type)
