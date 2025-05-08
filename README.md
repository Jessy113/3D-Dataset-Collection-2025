# 📊 Open 3D dataset Collection: A Guideline for Choosing Relevant 3D Datasets

## 📌 Description

This repository was created as part of the publication **"[Paper Title]"** (see citation below). 

It provides an alphabetically organized collection of various published 3D datasets, along with comparable dataset characteristics 
to support researchers in selecting suitable datasets for application-specific machine learning tasks. 

⚠️ **Note:** This repository does *not* host any 3D datasets.  
> It only includes references to external sources where the original datasets can be accessed.

The repository is divided into three main folders: 

- **[Dataset-Collection](./Dataset-Collection)**:  
  Contains an overview of datasets, along with comparable dataset characteristics  
  _(e.g., S3DIS, ScanNet, KITTI)_.

- **[Dataset-Properties](./Dataset-Properties)**:  
  Defines and describes key dataset characteristics and their relevance  
  _(e.g., publication year, indoor/outdoor)_.

- **[Dataset-Statistics](./Dataset-Statistics)**:  
  Includes statistical analyses and plots based on the dataset collection  
  _(e.g., distribution by publication year)_.

**Last updated:** <br>
2025-05-07

---

## 📂 File Structure

```
.
├─ Dataset-Collection                                       
│   ├── dataset_collection.csv               # Overview of 3D datasets
│   └── README.md                            # Describes Dataset-Collection folder
├─ Dataset-Properties
│   ├── dataset_properties.csv               # Overview of dataset characteristics
│   ├── README.md                            # Describes Dataset-Properties folder
├─ Dataset-Statistics
│   ├── Statistic-Plots                      # Visualization of dataset statistics
│   │   ├── datasets_per_publisher.png
│   │   ├── datasets_per_year.png
│   │   ├── indoor_outdoor_datasets.png
│   │   └── ...
│   ├── plot_statistics.py                   # Script for generating statistics plots
│   └── README.md                            # Describes Dataset-Statistics folder  
└── README.md                                # Describes the repository and its contents
```

---

## 📥 Download & Use

The dataset collection can be downloaded directly from this repository:

```bash
git clone https://github.com/Jessy113/Dataset-Collection-2025.git

```

---

## 🔗 Citation

This dataset collection is available under the **[CC BY 4.0]** license. Please cite the source when using:

> Buchner, J., Buchholz, J., Klauer, T., Neubert, P., & Paulus, D. (2025). *[Title]*. [Journal Name], [Volume(Issue)], [pages]. [https://doi.org/xxx]

Please review the individual dataset licenses for specific terms of use.

---

## ✉️ Contact

If you have any questions or feedback, you can reach me at jbuchner.research@gmail.com or open a GitHub issue.

