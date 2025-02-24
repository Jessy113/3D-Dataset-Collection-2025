# 📊 Open 3D dataset Collection: A Guideline for Choosing Relevant 3D Datasets

## 📌 Description

This repository was created as part of the publication **"[Paper Title]"**. It provides an alphabetically organized table offering an overview of various 3D datasets, along with key selection criteria such as publication year and areas of application."

- **Authors:** <br>
  M.Sc. Jessica Buchner<sup>1,2</sup>, M.Sc. Janine Buchholz<sup>2</sup>, Prof. Dr. Thomas Klauer<sup>1</sup>, Prof. Dr. Peer Neubert<sup>2</sup>, Prof. Dr.-Ing. Dietrich Paulus<sup>2</sup> 

- **Institutions:** <br>
  <sup>1</sup> Mainz University, Lucy-Hillebrand-Straße 2, 55128 Mainz, Germany <br>
  <sup>2</sup> University of Koblenz, Universitätsstraße 1, 56072 Koblenz, Germany

- **Last updated:** <br>
    2025-02-19

---

## 📂 File Structure

.
│   README.md
│
├───Dataset-Collection
│       datasets-excel.xlsx
│       datasets-full-UTF8.csv
│       datasets-short.csv
│       dataset_collection.csv
│
├───Dataset-Properties
│       dataset_properties.csv
│       properties.xlsx
│
└───Dataset-Statistics
    │   plotstatistics.py
    │
    └───Statistic-Plots
            datasets_per_publisher.png
            datasets_per_year.png
            indoor_outdoor_datasets.png
            most_frequent_publishers.png
            no_benchmarks.png
            no_papers.png
            real_synthetic_datasets.png

---

## 🔍 Dataset Table Description

| Column            | Description                                       |
| ----------------- | ------------------------------------------------- |
| `Dataset`         | Name of the dataset                               |
| `Citation`        | Citation of the corresponding paper               |
| `Year`            | Year of publication                               |
| `Publisher`       | Conference or journal where published             |
| `Description`     | Description of the dataset                        |
| `Size`            | Size of the dataset (e.g., 10 GB)                 |
| `Modality`        | Type of data (e.g., images, point clouds)         |
| `Composition`     | Composition of data (e.g., no. scenes, meshes)    |
| `Indoor/Outdoor`  | Indicates if the dataset is indoor or outdoor     |
| `Synthetic/Real`  | Indicates if the data is synthetic or real        |
| `Ground Truth`    | Availability and type of annotations              |
| `No. Classes`     | Number of semantic classes in the dataset         |
| `Classes`         | List of classes in the dataset                    |
| `Application`     | Applications areas of the dataset                 |
| `No. Papers`      | Number of papers mentioning the dataset           |
| `No. Benchmarks`  | Number of benchmarks associated with the dataset  |
| `...`             | ...                                               |

**Note on CSV Delimiters:** <br>
Please note that different regions use different delimiters for CSV files:<br>
- USA/UK: Typically use commas (,) as the delimiter.<br>
- Germany/Europe: Typically use semicolons (;) as the delimiter.<br>

The datasets.csv file is stored using commas as the separator to improve compatibility across different systems and regions.


---

## 📥 Download & Use

The dataset collection can be downloaded directly from this repository:

```bash
git clone https://github.com/Jessy113/Dataset-Collection-2025.git

```

---

## 🔗 Citation

This dataset collection is available under the **[CC BY 4.0]** license. Please cite the source when using:

> DOI and citation information will be updated upon publication.

Please review the individual dataset licenses for specific terms of use.

---

## ✉️ Contact

If you have any questions or feedback, you can reach me at jbuchner.research@gmail.com or open a GitHub issue.

