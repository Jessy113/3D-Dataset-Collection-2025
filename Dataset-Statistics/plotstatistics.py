import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#-------------------------------------------------------------------------

# Link to file
csv_file = "Dataset-Table\datasets.csv"

#-------------------------------------------------------------------------

# Visualize the number of datasets per year
def plot_year_data(data, stat=False):

    if stat==True:
        # Get summary statistics
        print(data['Year'].describe())

    # Count the number of datasets per year
    counts = data['Year'].value_counts().sort_index()

    # Vertical Bar chart:
    plt.figure(figsize=(12, 6))
    sns.barplot(x=counts.index, y=counts.values, palette='viridis')
    plt.title('Number of Datasets Published per Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Datasets')
    plt.show()

#-------------------------------------------------------------------------

# Visualize the number of datasets per publisher
def plot_publisher_data(data, stat=False):

    if stat==True:
        # Get summary statistics
        print(data['Publisher'].describe())

    # Count the number of datasets per publisher
    counts = data['Publisher'].value_counts().sort_index()

    # Pie Chart
    plt.figure(figsize=(8, 8))
    counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, cmap='viridis')
    plt.title('Frequency Distribution of Publishers')
    plt.ylabel('')  # Hide the ylabel to make it cleaner
    plt.show()

#-------------------------------------------------------------------------

# Visualize the number of papers mentioning each dataset    
def plot_mention_data(data, stat=False):

    if stat==True:
        # Get summary statistics
        print(data['No. Papers'].describe())

    # Count the number of papers mentioning each dataset 
    counts = data.groupby('Dataset')['No. Papers'].sum()

    # Holizontal Bar chart:
    plt.figure(figsize=(12, 6))
    sns.barplot(x=counts.values, y=counts.index, palette='viridis')
    plt.title('Number of Papers Mentioning each Dataset')
    plt.xlabel('Number of Papers Mentioning the Dataset')
    plt.ylabel('Dataset')
    plt.show()


#-------------------------------------------------------------------------

# Visualize the number of benchmarks associated with each dataset    
def plot_benchmark_data(data, stat=False):

    if stat==True:
        # Get summary statistics
        print(data['No. Benchmarks'].describe())

    # Count the number of benchmarks associated with each dataset 
    counts = data.groupby('Dataset')['No. Benchmarks'].sum()

    # Holizontal Bar chart:
    plt.figure(figsize=(12, 6))
    sns.barplot(x=counts.values, y=counts.index, palette='viridis')
    plt.title('Number of Benchmarks Associated with each Dataset')
    plt.xlabel('Number of Benchmarks Associated with the Dataset')
    plt.ylabel('Dataset')
    plt.show()

#-------------------------------------------------------------------------

# Visualize the number of indoor / outdoor datasets     
def plot_inoutdoor_data(data, stat=False):

    if stat==True:
        # Get summary statistics
        print(data['Indoor/Outdoor'].describe())

    # Count the number of indoor / outdoor datasets 
    counts = data['Indoor/Outdoor'].str.lower().apply(lambda x: 
    'Indoor' if 'indoor' in str(x) else 'Outdoor' if 'outdoor' in str(x) else 'Unknown'
    ).value_counts()

    # Vertical Bar chart:
    plt.figure(figsize=(12, 6))
    sns.barplot(x=counts.index, y=counts.values, palette='viridis')
    plt.title('Number of Indoor / Outdoor Datasets')
    plt.xlabel('Dataset')
    plt.ylabel('Number of Indoor / Outdoor Datasets')
    plt.show()

#-------------------------------------------------------------------------

# Visualize the number of synthetic / real datasets     
def plot_synthreal_data(data, stat=False):

    if stat==True:
        # Get summary statistics
        print(data['Synthetic/Real'].describe())

    # Count the number of synthetic / real datasets 
    counts = data['Synthetic/Real'].str.lower().apply(lambda x: 
    'Synthetic' if 'synthetic' in str(x) else 'Real' if 'real' in str(x) else 'Unknown'
    ).value_counts()

    # Vertical Bar chart:
    plt.figure(figsize=(12, 6))
    sns.barplot(x=counts.index, y=counts.values, palette='viridis')
    plt.title('Number of Synthetic / Real Datasets')
    plt.xlabel('Dataset')
    plt.ylabel('Number of Synthetic / Real Datasets')
    plt.show()

#-------------------------------------------------------------------------

def main ():

    # Load your CSV file into a DataFrame
    data = pd.read_csv(csv_file)

    # Print column names
    print(f'Columns: {data.columns.tolist()}')

    # Visualize the number of datasets per year
    plot_year_data(data)
    
    # Visualize the number of datasets per publisher
    plot_publisher_data(data)
    
    # Visualize the number of papers mentioning each dataset    
    plot_mention_data(data)

    # Visualize the number of benchmarks associated with each dataset    
    plot_benchmark_data(data)

    # Visualize the number of indoor / outdoor datasets    
    plot_inoutdoor_data(data)

    # Visualize the number of synthetic / real datasets    
    plot_synthreal_data(data)

#-------------------------------------------------------------------------

if __name__ == '__main__':
    sys.exit(main())

