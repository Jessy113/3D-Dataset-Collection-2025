import os
import sys

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#-------------------------------------------------------------------------

# Link to file
csv_file = "Dataset-Collection\dataset_collection.csv"
save_dir = "Dataset-Statistics\Statistic-Plots"

#-------------------------------------------------------------------------

# Visualize the number of datasets per year
def plot_year_data(data, save_dir, stat=False, show=False):

    # Convert 'Year' to numeric (in case it's an object dtype)
    data['Year'] = pd.to_numeric(data['Year'], errors='coerce')

    if stat:
        # Get summary statistics
        print(data['Year'].describe())

    # Check for rows with missing year values
    missing_years = data[data['Year'].isna()]
    print(f"Number of lines without year information: {missing_years.shape[0]}")

    # Count the number of datasets per year, removing rows with missing years
    counts = data.dropna(subset=['Year'])['Year'].astype(int).value_counts().sort_index()

    # Vertical Bar chart:
    plt.figure(figsize=(12, 6))
    ax = sns.barplot(x=counts.index, y=counts.values, palette="plasma", hue=counts.index, legend=False)
    
    # show values
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.0f}', 
                    (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha='center', va='bottom',
                    color='black', fontsize=12,
                    bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.0'))

    plt.title('Number of Datasets Published per Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Datasets')

    # save plot
    plt.savefig(os.path.join(save_dir, "datasets_per_year.png"), dpi=300, bbox_inches='tight')

    if show:
        # show plot
        plt.show()

#-------------------------------------------------------------------------

# Visualize the number of datasets per publisher as pie chart
def plot_publisher_data_pie(data, save_dir, top=True, top_n=10, stat=False, show=False):

    if stat:
        # Get summary statistics
        print(data['Publisher'].describe())

    # Check for rows with missing publisher values
    missing_publishers = data[data['Publisher'].isna()]
    print(f"Number of lines without publisher information: {missing_publishers.shape[0]}")

    # Count the number of datasets per publisher, removing rows with missing publishers
    counts = data.dropna(subset=['Publisher'])['Publisher'].value_counts()

    # Sort counts in descending order for proper visualization
    counts = counts.sort_values(ascending=False)

    if top == True:

        # Sort publishers by count (descending) and take top_n
        top_publishers = counts.head(top_n)

        # Group the rest as 'Other'
        others = counts.tail(len(counts) - top_n).sum()

        # Combine the top publishers with the 'Other' category using pd.concat
        counts = pd.concat([top_publishers, pd.Series({'Other': others})])

        plt_title = f'Frequency Distribution of Top {top_n} Publishers'
        file_name = "most_frequent_publishers.png"

    else: 

        plt_title = 'Frequency Distribution of the Publishers'
        file_name = 'publishers_pie.png'

    plt.figure(figsize=(12, 12))
    
    plt.figure(figsize=(12, 12))
    counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, cmap='viridis')      
    plt.title(plt_title)
    plt.xlabel('Number of Datasets per Publisher')
    plt.ylabel('Publisher')

    # save plot
    plt.savefig(os.path.join(save_dir, file_name), dpi=300, bbox_inches='tight')

    if show:
        # show plot
        plt.show()

#-------------------------------------------------------------------------

# Visualize the number of datasets per publisher as bar chart
def plot_publisher_data_bar(data, save_dir, top=False, top_n=20, stat=False, show=False):

    if stat:
        # Get summary statistics
        print(data['Publisher'].describe())

    # Check for rows with missing publisher values
    missing_publishers = data[data['Publisher'].isna()]
    print(f"Number of lines without publisher information: {missing_publishers.shape[0]}")

    # Count the number of datasets per publisher, removing rows with missing publishers
    counts = data.dropna(subset=['Publisher'])['Publisher'].value_counts()

    # Sort counts in descending order for proper visualization
    counts = counts.sort_values(ascending=False)

    if top == True:

        # Sort publishers by count (descending) and take top_n
        counts = counts.head(top_n)

        plt_title = f'Number of Datasets Published by the Top {top_n} Publishern'
        file_name = "datasets_per_publisher_top.png"

    else: 

        plt_title = 'Number of Datasets per Publisher'
        file_name = 'datasets_per_publisher.png'

    plt.figure(figsize=(12, 12))

    ax = sns.barplot(x=counts.values, y=counts.index, palette="inferno", hue=counts.index, legend=False)
        # Note: aktivating the legend leads to an unwanted 0 in the top left corner (I do not know why)

    # show values
    for p in ax.patches:
        ax.annotate(f'{p.get_width():.0f}', 
                    (p.get_width(), p.get_y() + p.get_height() / 2),
                    ha='left', va='center',
                    color='black', fontsize=12, 
                    bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.2'))
        
    plt.title(plt_title)
    plt.xlabel('Number of Datasets per Publisher')
    plt.ylabel('Publisher')
        
    # save plot
    plt.savefig(os.path.join(save_dir, file_name), dpi=300, bbox_inches='tight')

    if show:
        # show plot
        plt.show()

#-------------------------------------------------------------------------

# Visualize the number of papers mentioning each dataset    
def plot_mention_data(data, save_dir, top=True, top_n=20, stat=False, show=False):

    # Convert 'No. Papers' to numeric (in case it's an object dtype)
    data['No. Papers'] = pd.to_numeric(data['No. Papers'], errors='coerce')

    if stat==True:
        # Get summary statistics
        print(data['No. Papers'].describe())

    # Check for rows with missing paper numbers
    missing_no_papers = data[data['No. Papers'].isna()]
    print(f"Number of lines without no. paper information: {missing_no_papers.shape[0]}")

    # Count the number of papers mentioning each dataset, removing rows with missing paper information 
    counts = data.dropna(subset=['No. Papers']).groupby('Dataset')['No. Papers'].sum()

    # Sort counts in descending order for proper visualization
    counts = counts.sort_values(ascending=False)

    if top == True:

        # Sort no. papers by count (descending) and take top_n
        counts = counts.head(top_n)

        plt_title = f'Number of Papers Mentioning the Top {top_n} Datasets'
        file_name = "no_papers_top.png"

    else: 

        plt_title = 'Number of Papers Mentioning each Dataset'
        file_name = 'no_papers.png'

    plt.figure(figsize=(12, 12))

    ax = sns.barplot(x=counts.values, y=counts.index, palette="Reds", hue=counts.index, legend=False)
        # Note: aktivating the legend leads to an unwanted 0 in the top left corner (I do not know why)

    # show values
    for p in ax.patches:
        ax.annotate(f'{p.get_width():.0f}', 
                    (p.get_width(), p.get_y() + p.get_height() / 2),
                    ha='left', va='center',
                    color='black', fontsize=12, 
                    bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.2'))
        
    plt.title(plt_title)
    plt.xlabel('Number of Papers Mentioning the Dataset')
    plt.ylabel('Dataset')
        
    # save plot
    plt.savefig(os.path.join(save_dir, file_name), dpi=300, bbox_inches='tight')

    if show:
        # show plot
        plt.show()

#-------------------------------------------------------------------------

# Visualize the number of benchmarks associated with each dataset    
def plot_benchmark_data(data, save_dir, top=True, top_n=20, stat=False, show=False):

    # Convert 'No. Benchmarks' to numeric (in case it's an object dtype)
    data['No. Benchmarks'] = pd.to_numeric(data['No. Benchmarks'], errors='coerce')

    if stat==True:
        # Get summary statistics
        print(data['No. Benchmarks'].describe())

    # Check for rows with missing benchmark numbers
    missing_no_benchmarks = data[data['No. Benchmarks'].isna()]
    print(f"Number of lines without no. benchmarks information: {missing_no_benchmarks.shape[0]}")

    # Count the number of benchmarks associated with each dataset, removing rows with missing benchmark information 
    counts = data.dropna(subset=['No. Benchmarks']).groupby('Dataset')['No. Benchmarks'].sum()

    # Sort counts in descending order for proper visualization
    counts = counts.sort_values(ascending=False)


    if top == True:

        # Sort no. benchmarks by count (descending) and take top_n
        counts = counts.head(top_n)

        plt_title = f'Number of Benchmarks Associated with the Top {top_n} Datasets'
        file_name = "no_benchmarks_top.png"

    else: 

        plt_title = 'Number of Benchmarks Associated with each Dataset'
        file_name = 'no_benchmarks.png'

    plt.figure(figsize=(12, 12))

    ax = sns.barplot(x=counts.values, y=counts.index, palette="Blues", hue=counts.index, legend=False)
        # Note: aktivating the legend leads to an unwanted 0 in the top left corner (I do not know why)

    # show values
    for p in ax.patches:
        ax.annotate(f'{p.get_width():.0f}', 
                    (p.get_width(), p.get_y() + p.get_height() / 2),
                    ha='left', va='center',
                    color='black', fontsize=12, 
                    bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.2'))
        
    plt.title(plt_title)
    plt.xlabel('Number of Benchmarks Associated with the Dataset')
    plt.ylabel('Dataset')
        
    # save plot
    plt.savefig(os.path.join(save_dir, file_name), dpi=300, bbox_inches='tight')

    if show:
        # show plot
        plt.show()

#-------------------------------------------------------------------------

# Visualize the number of indoor / outdoor datasets     
def plot_inoutdoor_data(data, save_dir, stat=False, show=False):

    if stat==True:
        # Get summary statistics
        print(data['Indoor/Outdoor'].describe())

    # Count the number of indoor / outdoor datasets 
    counts = data['Indoor/Outdoor'].str.lower().apply(lambda x: 
    'Indoor' if 'indoor' in str(x) else 'Outdoor' if 'outdoor' in str(x) 
    else 'Mixed' if 'mixed' else 'Other' if 'other' else 'Unknown'
    ).value_counts()

    # Vertical Bar chart:
    plt.figure(figsize=(12, 6))
    ax = sns.barplot(x=counts.index, y=counts.values, palette='viridis', hue=counts.index, legend=False)
        # Note: aktivating the legend leads to an unwanted 0 in the top left corner (I do not know why)

    # show values
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.0f}', 
                    (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha='center', va='bottom',
                    color='black', fontsize=12, 
                    bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.0'))

    plt.title('Number of Indoor / Outdoor Datasets')
    plt.xlabel('Dataset')
    plt.ylabel('Number of Indoor / Outdoor Datasets')

    # save plot
    plt.savefig(os.path.join(save_dir, "indoor_outdoor_datasets.png"), dpi=300, bbox_inches='tight')

    if show:
        # show plot
        plt.show()

#-------------------------------------------------------------------------

# Visualize the number of synthetic / real datasets     
def plot_synthreal_data(data, save_dir, stat=False, show=False):

    if stat==True:
        # Get summary statistics
        print(data['Real/Synthetic'].describe())

    # Count the number of synthetic / real datasets 
    counts = data['Real/Synthetic'].str.lower().apply(lambda x: 
    'Real' if 'real' in str(x) else 'Synthetic' if 'synthetic' in str(x)
    else 'Mixed' if 'mixed' else 'Other' if 'other' else 'Unknown'
    ).value_counts()

    # Vertical Bar chart:
    plt.figure(figsize=(12, 6))
    ax = sns.barplot(x=counts.index, y=counts.values, palette='cividis', hue=counts.index, legend=False)

    # show values
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.0f}', 
                    (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha='center', va='bottom',
                    color='black', fontsize=12, 
                    bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.0'))
        
    plt.title('Number of Real / Synthetic Datasets')
    plt.xlabel('Dataset')
    plt.ylabel('Number of Real / Synthetic Datasets')

    # save plot
    plt.savefig(os.path.join(save_dir, "real_synthetic_datasets.png"), dpi=300, bbox_inches='tight')

    if show:
        # show plot
        plt.show()


#-------------------------------------------------------------------------

def main ():

    # Load your CSV file into a DataFrame
    data = pd.read_csv(csv_file)

    # Print column names
    print(f'Columns: {data.columns.tolist()}')

    # Check if the save directory exists, if not create it
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Visualize the number of datasets per year
    plot_year_data(data, save_dir)

    # Visualize the number of datasets per publisher
    plot_publisher_data_pie(data, save_dir, top=True)
    plot_publisher_data_bar(data, save_dir, top=True)

    # Visualize the number of papers mentioning each dataset    
    plot_mention_data(data, save_dir, top=True)

    # Visualize the number of benchmarks associated with each dataset    
    plot_benchmark_data(data, save_dir, top=True)

    # Visualize the number of indoor / outdoor datasets    
    plot_inoutdoor_data(data, save_dir)

    # Visualize the number of synthetic / real datasets    
    plot_synthreal_data(data, save_dir)

#-------------------------------------------------------------------------

if __name__ == '__main__':
    sys.exit(main())

