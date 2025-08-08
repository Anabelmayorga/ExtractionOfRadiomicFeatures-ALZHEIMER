- This repository contains the code and data used in the Bachelor's Thesis (TFG) titled:
“Feature Extraction and Automatic Classification of Biomedical Brain Images for Anomaly Detection.”

- Project Description
The objective of this project is to develop a computer-aided diagnosis (CAD) system for the detection of Alzheimer’s Disease through the analysis of brain magnetic resonance imaging (MRI), using radiomics techniques to extract morphological and texture features, focusing on the hippocampus as the region of interest (ROI).

These features are subsequently classified using machine learning algorithms, specifically support vector machines (SVM), in order to identify Alzheimer’s Disease (AD) at an early stage.

The publicly available OASIS-1 (Open Access Series of Imaging Studies) database has been used, which provides brain MRI scans of both healthy individuals and patients diagnosed with Alzheimer’s Disease.

- Methodology
* Preprocessing and Segmentation:
The images were preprocessed and segmented using tools such as FreeSurfer (provided by OASIS-1), selecting the hippocampus as the ROI.

* Feature Extraction:
Radiomic features were extracted following the IBSI standard (Zwanenburg et al., 2020), including shape, intensity, and texture features (GLCM, GLSZM, etc.).

* Classification:
SVM models were trained using different combinations of radiomic feature pairs to evaluate their diagnostic performance.

* Evaluation:
Performance metrics include accuracy, precision, recall, and F1-Score, achieving promising results for both the right and left hippocampus.

The project was developed using Python 3.8.

- License
This project is published under the MIT License.
You can find the full license text in the LICENSE file.

- Author
Bachelor’s Thesis (TFG) by Anabel Mayorga Ruiz
Faculty of Sciences — University of Córdoba
Academic Year: 2025
