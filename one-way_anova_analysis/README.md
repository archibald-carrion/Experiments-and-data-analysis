# Laboratory: One-Way ANOVA Analysis
## Database Motor Response Time Comparison

This repository contains an R Markdown script that performs a comprehensive one-way Analysis of Variance (ANOVA) to compare response times across different database motors.

## Overview

The analysis compares the performance of four database motors (PostgreSQL, MySQL, MongoDB, and Redis) by analyzing their response times in milliseconds. This study helps determine if there are statistically significant differences in performance between these database systems.

## Data Requirements

### Input File
- **File**: `bd_server.csv`
- **Structure**: 
  - `motor`: Database motor type (PostgreSQL, MySQL, MongoDB, Redis)
  - `respuesta`: Response time in milliseconds
- **Sample Size**: 12 observations per database motor (48 total observations)
- **Encoding**: UTF-8

### Data Format Example
```
motor,respuesta
PostgreSQL,250.5
MySQL,180.2
MongoDB,320.1
Redis,95.8
...
```

## Prerequisites

### Required R Packages
The script will automatically install missing packages, but you can install them manually:

```r
install.packages(c("dplyr", "car", "lsr"))
```

### Package Functions Used
- **dplyr**: Data manipulation and summary statistics
- **car**: Levene's test for homogeneity of variances
- **lsr**: Effect size calculation (eta squared)

## Analysis Components

### 1. Data Loading and Preparation
- Loads the CSV file with proper encoding
- Converts the `motor` variable to a factor
- Displays data structure and first 6 rows

### 2. Descriptive Statistics
- Calculates mean and standard deviation for each database motor
- Creates boxplots to visualize response time distributions

### 3. ANOVA Model
**Mathematical Model:**
```
Y_ij = μ + τ_i + ε_ij
```
Where:
- `Y_ij`: Response time for motor i, observation j
- `μ`: Overall mean
- `τ_i`: Effect of motor i
- `ε_ij`: Random error term

**Hypotheses:**
- H₀: τ₁ = τ₂ = τ₃ = τ₄ = 0 (no difference between motors)
- H₁: At least one τᵢ ≠ 0 (at least one motor differs)

### 4. Assumption Validation
The script checks three critical ANOVA assumptions:

#### 4.1 Normality of Residuals
- **Visual**: Q-Q plot
- **Statistical**: Shapiro-Wilk test
- **Interpretation**: p > 0.05 indicates normal distribution

#### 4.2 Homogeneity of Variances
- **Visual**: Residuals vs. Fitted values plot
- **Statistical**: Bartlett test and Levene test
- **Interpretation**: p > 0.05 indicates equal variances

#### 4.3 Independence of Observations
- **Visual**: Residuals vs. observation order plot
- **Assumption**: Random sampling and experimental design

### 5. Post-Hoc Analysis
If ANOVA is significant (p < 0.05):
- **Tukey HSD test**: Pairwise comparisons between all database motors
- **Confidence intervals**: 95% confidence intervals for mean differences
- **Visualization**: Plot of Tukey HSD results

### 6. Effect Size and Power Analysis
- **Eta squared (η²)**: Proportion of variance explained by database motor
- **Power analysis**: Probability of detecting true differences

## How to Run the Analysis

### Step 1: Prepare Your Environment
1. Ensure R and RStudio are installed
2. Place `bd_server.csv` in your working directory
3. Open the R Markdown file (`lab_4.Rmd`)

### Step 2: Execute the Analysis
```r
# In RStudio or VSCode
# Click "Knit" button to generate PDF report (or run button depending on your VSCode instalation)
# Or run chunks individually for interactive analysis
```

### Step 3: Interpret Results
1. **ANOVA Table**: Check F-statistic and p-value
2. **Assumption Tests**: Verify p-values > 0.05 for validity
3. **Post-Hoc Tests**: Identify which motors differ significantly
4. **Effect Size**: Assess practical significance

## Output Interpretation

### ANOVA Results
- **F-statistic**: Ratio of between-group to within-group variance
- **p-value < 0.05**: Reject H₀, motors have different response times
- **p-value ≥ 0.05**: Fail to reject H₀, no significant differences

### Tukey HSD Results
- **Difference**: Mean difference between motor pairs
- **p adj**: Adjusted p-value for multiple comparisons
- **Confidence Interval**: Range of plausible values for the difference

### Effect Size Interpretation
- **Small effect**: η² ≈ 0.01
- **Medium effect**: η² ≈ 0.06
- **Large effect**: η² ≈ 0.14

## Troubleshooting

### Common Issues
1. **File not found**: Ensure `bd_server.csv` is in the working directory
2. **Package errors**: Install missing packages manually
3. **Encoding issues**: Verify CSV file uses UTF-8 encoding
4. **Factor conversion**: Ensure `motor` column contains text, not numbers

### Assumption Violations
- **Non-normality**: Consider data transformation or non-parametric tests
- **Unequal variances**: Use Welch's ANOVA or robust methods
- **Non-independence**: Review experimental design and data collection

## Statistical Significance Level
- **Alpha level**: 0.05 for all tests
- **Confidence level**: 95% for all intervals

