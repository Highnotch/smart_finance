import matplotlib.pyplot as plt
import numpy as np

def visualize_performance(investment_performance, progress):
    plt.figure(figsize=(10, 6))
    plt.plot(investment_performance)
    plt.xlabel('Time')
    plt.ylabel('Portfolio Value')
    plt.title('Investment Performance Over Time')
    plt.show()
    
    plt.figure(figsize=(8, 5))
    plt.bar(progress.keys(), progress.values(), color='skyblue')
    plt.xlabel('Financial Goals')
    plt.ylabel('Progress (%)')
    plt.title('Progress Towards Financial Goals')
    plt.xticks(rotation=45)
    plt.show()
