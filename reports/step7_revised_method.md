# Method

## Participants

We recruited participants through the SAPA (Synthetic Aperture Personality Assessment) online platform (Condon & Revelle, 2014). A total of 23,679 individuals participated in the study. After quality control procedures, data from 23,647 participants were included in the final analyses. We excluded 32 participants based on the following criteria: (a) insufficient responses (fewer than 10 items answered), and (b) straight-lining patterns (identical responses across consecutive items), which indicate low-quality or non-engaged responding.

For state-level analyses, we included 9 states with sample sizes of at least 100 participants each, resulting in a final sample of 7,308 respondents. We selected this minimum threshold to ensure stable estimates with standard errors (SE) less than 0.1 for each state-scale combination. The states included were California (n = 1,713), Michigan (n = 860), Illinois (n = 820), Texas (n = 711), Pennsylvania (n = 700), Florida (n = 696), New York (n = 684), Washington (n = 599), and Virginia (n = 525).

We note that the online recruitment method may introduce sampling biases, as participants were self-selected and may not be fully representative of the general population in each state. However, the large sample sizes help mitigate some concerns about generalizability.

## Measures

Personality traits were assessed using items from the International Personality Item Pool (IPIP). The assessment included 696 personality items, which were scored to create 131 scale scores. All items were rated on a 6-point Likert scale ranging from 1 (very inaccurate) to 6 (very accurate).

**Big Five Personality Factors.** We measured five broad personality domains using NEO domain scores: Openness to Experience (NEO_O), Conscientiousness (NEO_C), Extraversion (NEO_E), Agreeableness (NEO_A), and Neuroticism (NEO_N). Each domain score was calculated as the mean of items assigned to that domain in the scoring key (superKey696.csv). Items marked with -1 in the scoring key were reverse-coded (7 - original score) before averaging.

**Ideology.** Conservative ideology scores were computed as the mean of two standardized components: MPQ Traditionalism and NEO Liberalism (reversed). Specifically, we calculated z-scores for MPQ Traditionalism and NEO Liberalism using only participants with valid data on both components, then averaged them with NEO Liberalism multiplied by -1 to align the direction with conservatism.

**Honesty-Humility.** Honesty-Humility scores were computed as the mean of three standardized components: NEO Morality (A2), NEO Modesty (A4), and HEXACO Honesty-Humility. Each component was standardized (z-scored) before averaging, using only participants with complete data on all three components.

## Procedure

The SAPA project employed a planned missingness design (Revelle et al., 2016), in which each participant responded to a randomly selected subset of items rather than the full 696-item pool. This design reduces participant burden while maintaining statistical power through appropriate missing data handling. On average, participants responded to 86 items (range: 0 to 311 items), resulting in an item-level missing rate of 87.6%. This high missing rate is expected and appropriate given the planned missingness design.

## Data Analysis

All analyses were conducted using Python 3.9 with pandas 1.5.0, numpy 1.23.0, scipy 1.9.0, and scikit-learn 1.1.0. Analysis code and data files are available at [repository URL to be added]. We performed quality control checks to identify and exclude low-quality responses. Specifically, we excluded participants who answered fewer than 10 items or showed straight-lining patterns (identical responses across consecutive items).

Scale scores were calculated as the mean of items assigned to each scale in the scoring key. Reverse-coded items (marked with -1) were transformed by subtracting the original score from 7 before averaging. For composite scales (Ideology and Honesty-Humility), we computed z-scores for each component using only participants with valid data on all components, then averaged the z-scores while preserving the original index to ensure proper alignment with the dataset.

For state-level analyses, we calculated Critical Ratios (CR) to identify states with significantly high or low scores on each personality scale. The CR was computed as:

CR = (State Mean - Grand Mean) / SE

where SE is the standard error of the state mean. Given the 63 comparisons (7 scales × 9 states), we used |CR| > 3.0 as a conservative threshold, corresponding to p < .003 under normal approximation. This threshold provides conservative control for multiple comparisons, as it corresponds to a Bonferroni-corrected significance level of approximately p < .05/63 ≈ .0008, ensuring that the family-wise error rate remains low while maintaining reasonable statistical power.

We note that state-level comparisons were conducted relative to the grand mean across all analyzed states, without explicit control for demographic covariates. While this approach allows for straightforward interpretation of regional differences, future research should examine whether these patterns persist after controlling for age, education, and other demographic factors that may vary across states.
