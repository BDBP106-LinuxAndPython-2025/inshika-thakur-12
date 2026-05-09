#!/usr/bin/python3

"""Work on NCI data - build classification model after reducing
the gene expression features using hierarchical clustering.
Compare this with the PCA approach."""

import numpy as np
from ISLP import load_data
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


"""STEP 1: LOAD THE DATA"""
#Loads the NCI60 data from ISLP
NCI60 = load_data("NCI60")
X = NCI60["data"]
y = NCI60["labels"]
X = np.asarray(X)
#converts x into a numpy array
y = np.asarray(y).ravel()
#.ravel() makes it one-dimensional
print("X shape:", X.shape)
print("y shape:", y.shape)
print("Number of classes:", len(np.unique(y)))
#Here np.unique() finds all the different cancer classes and len will count them and prints how many cancer types are present.


"""STEP 2: SCALE THE DATA"""
#This standardizes the dataset.
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


"""STEP 3: HIERARCHICAL CLUSTERING ON GENES"""
#The original shape of this dataset is samples*genes (64*6830) But here we want to cluster the genes and not the samples
X_transpose = X_scaled.T
hcluster = AgglomerativeClustering(n_clusters=40,linkage="ward")
#Creates a hierarchical clustering model
gene_clusters = hcluster.fit_predict(X_transpose)
#Here we are applying hierarchical clustering on genes, and it returns the cluster number of each gene.


"""STEP 4: SELECT ONE REPRESENTATIVE GENE FROM EACH CLUSTER"""
#Creates an empty list
selected_features = []
for cluster_id in np.unique(gene_clusters):
    gene_indices = np.where(gene_clusters == cluster_id)[0]
    #finds all genes that belong to the current cluster
    selected_features.append(gene_indices[0])

X_hcluster = X_scaled[:, selected_features]
#Creates a reduced dataset using only the selected genes
print("Shape after hierarchical feature selection:", X_hcluster.shape)
#The previous shape was (64, 6830) but then after Hierarchical clustering the shapr we (64, 40)


"""STEP 5: PCA DIMENSIONALITY REDUCTION"""
pca = PCA(n_components=50)
#Creates a PCA objects
X_pca = pca.fit_transform(X_scaled)
#Applies PCA to the scaled data
print("Shape after PCA:", X_pca.shape)
#The previous shape was (64, 6830) and after PCA the shape is (64,50)


"""STEP 6: TRAIN CLASSIFIER USING HIERARCHICAL FEATURES"""
X_train_hc, X_test_hc, y_train_hc, y_test_hc = train_test_split(X_hcluster,y,test_size=0.2,random_state=42)
#Splits the hierarchical clustering reduced data into test and train data
model_hc = LogisticRegression(max_iter=10000)
#Creates a logistic regression model
model_hc.fit(X_train_hc, y_train_hc)
#trains the model using hierarchical clustering features
y_pred_hc = model_hc.predict(X_test_hc)
#Uses the trained model to predict cancer classes for the test data
hc_accuracy = accuracy_score(y_test_hc, y_pred_hc)
#Compares the actual labels with predicted labels and calculates accuracy.


"""STEP 7: TRAIN CLASSIFIER USING PCA FEATURES"""
X_train_pca, X_test_pca, y_train_pca, y_test_pca = train_test_split(X_pca,y,test_size=0.2,random_state=42)
#SPlits the PCA reduced data into training and testing data
model_pca = LogisticRegression(max_iter=10000)
#Creates another logistic regression model for PCA features
model_pca.fit(X_train_pca, y_train_pca)
#Now here model is trained using PCA reduced features
y_pred_pca = model_pca.predict(X_test_pca)
#Predicts cancer classes for the PCA test data
pca_accuracy = accuracy_score(y_test_pca, y_pred_pca)
#Calculates accuracy for PCA based classification


"""STEP 8: FINAL COMPARISON"""
print("\n========== FINAL COMPARISON ==========")
print("Hierarchical Clustering Accuracy:", hc_accuracy)
print("PCA Accuracy:", pca_accuracy)

if pca_accuracy > hc_accuracy:
    print("PCA performed better.")
elif hc_accuracy > pca_accuracy:
    print("Hierarchical clustering performed better.")
else:
    print("Both methods gave the same accuracy.")